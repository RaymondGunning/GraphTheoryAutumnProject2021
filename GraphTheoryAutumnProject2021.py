# The shunting yard algorithm
def shunt(infix):
    """Convert infix to postfix."""
    # The output.
    postfix = ""
    # Shunting operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop the input one character at a time.
    for c in infix:
        # c is an operator.
        if c in {'*', '.', '|'}:
            # Check to see what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator at top of the stack to output.
                postfix = postfix + stack[-1]
                # Remove the operator from the stack.
                stack = stack[:-1]
            # Push c to the stack.
            stack = stack + c
        elif c == '(':
            # Push c to the stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output.
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
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove the operator from the stack.
        stack = stack[:-1]
    # Return the postfix version of infix.
    return postfix

# Thomson's Construction
class State:
    """A state and its arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept
    
    def followes(self):
        """The set of states that are gotten from following this state
           and all its e arrows."""
        
        states = {self}
        if self.label is None:
            for state in self.arrows:
                states = (states | state.followes())
        return states