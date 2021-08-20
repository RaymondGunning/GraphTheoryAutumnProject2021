#imports
import argparse

parser = argparse.ArgumentParser(description='This program allows the user to enter a regular expression and a file as command line arguments and out puts the number of matches found ')
#regular expression command line arguments
parser.add_argument('regex', type=str, metavar='R', action='store', 
                    help='Enter a regular expression in the command line. Example: f.a.b')
#input file command line arguments
parser.add_argument('input', type=str, metavar='I', action='store', 
                    help='Enter a Text file containing what you want to search in the command line. Example: Text.txt')
#-verbose enhancements attempt
#parser.add_argument("-v", "--verbose", action="store_true", help="Flag to display a list of matches found")

args = parser.parse_args()

# The shunting yard algorithm
def shunt(infix):
    """Convert infix to postfix."""
    # The output.
    postfix = ""
    # Shunting operator stack.
    stack = ""
    # Operator priority.
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop the input one character at a time.
    for c in infix:
        # Adding c as an operator.
        if c in {'*', '.', '|'}:
            # Check to see what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Attach operator at top of the stack to output.
                postfix = postfix + stack[-1]
                # Remove the operator from the stack.
                stack = stack[:-1]
            # Add c to the stack.
            stack = stack + c
        elif c == '(':
            # Add c to the stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Attach operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
                # c is a non-special.
        else:
            # Push it to the output.
            postfix = postfix + c

    # Empty the stack.
    while len(stack) != 0:
        # Attach operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove the operator from the stack.
        stack = stack[:-1]
    # Return the postfix version of infix.
    return postfix

# Thomson's Construction
class State:
    """State and Arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.self is to include the stae in the returned set
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept
    
    def followes(self):
        """ Set of states that are acquired from following this state
           and its e arrows."""
        
        states = {self}
        # if statement to check if the state has e arrows if not then it has none 
        if self.label is None:
            # loops through the states arrows
            for state in self.arrows:
                states = (states | state.followes())
        #return states
        return states

# NFA - A non-deterministic finite automaton.
class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end
# Matching
    def match(self, s):
        """Return True iff this NFA (instance) matches the string s."""
        # A list of previous states.
        previous = self.start.followes()
        # Loop through the string, One character at a time.
        for c in s:
            # Start with an empty set of current states.
            current = set()
            # Loop throuth the previous states.
            for state in previous:
                # Check if there is a c arrow.
                if state.label == c:
                    # Add followes for next state.
                    current = (current | state.arrows[0].followes())
            # Replace previous with current.
            previous = current
        # If the final state is in previous, then return True. if not return False. 
        return (self.end in previous)

#NFA Stack
def re_to_nfa(postfix):
    stack = []
    for c in postfix:
        if c == '.':
            # To Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Accept state of NFA1 non-accept.
            nfa1.end.accept = False
            # point at start state of nfa2.
            nfa1.end.arrows.append(nfa2.start)
            # A new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':
            #To Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # New start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # A new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':
            # Pop one NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old end state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end) 
            # Make old end state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        else:
            # NFA for the non-special character c.
            # Create the end and start state.
            end = State(None, [], True)
            start = State(c, [], False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # NFA with the start and end state.
            nfa = NFA(start, end)
            # Add the NFA to the NFA stack.
            stack.append(nfa)
    
    # There should only be one NFA on the stack if not return 0.
    if len(stack) != 1:
        return None
    else:
        return stack[0]

#main
if __name__ == "__main__":
    
    # saves input file to variable
    filereader = open(args.input)
    # saves expression from command line
    infix = args.regex

    counter = 0
    #converting infix to postfix
    postfix = shunt(infix)
    
    #converting postfix to nfa
    nfa = re_to_nfa(postfix)
    # loops through textfile
    for s in filereader:
        #checking for a match
        match = nfa.match(s)
        #if there is a match add to the counter
        if(match == True):
            counter+=1
    #output counter
    print(counter)
    #close input file
    filereader.close()