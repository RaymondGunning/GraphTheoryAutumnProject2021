# Graph Theory Autumn Project 2021


**Student ID:** G00372370


# Instructions on How to Run

Once you have cloned the repository and have python installed on your computer open visual studio code terminal and begin to type in the command line these commands - python3 GraphTheoryAutumnProject2021.py a.b input.txt. If you have entered all of this correctly then the program will output the number of matches it has found in the text file. You can also enter once again in the command line the command - python3 GraphTheoryAutumnProject2021.py -h for help or some info on the program.

# Explanation of Algorithm



# Question 1

- Explain the difference between regular expressions in infix notation and those in postfix notation?

    In computing, a regular expression is a sequence of characters that forms a search pattern, mainly for use in pattern matching with strings, or string matching.Each character in a regular expression is either understood to be a metacharacter with its special meaning, or a regular character with its literal meaning. Together, they can be used to identify text material of a given pattern, or process a number of details of it that can vary from being very alike to a very general similarity of the pattern.For example find and replace feature on microsoft word is a tool almost everyone is familar with it finds words that are similar or identical to the key word given and replaces it with what ever the user chooses. 
    
    Infix and Postfix notations are two different but at the same time similar ways of writing expressions. Though postfix expressions are easily and efficiently evaluated by computers, they can be difficult for users to read. Complex expressions using standard or normal parenthesized infix notation are often more readable than the corresponding postfix expressions. commonly users tend to work with infix notations and the convert them into postfix notation for easier computer processing vice versa if we recive a posfix notation we convert it to infix for the average user to understand. Computers are likely to use a stack to evaluate expressions and this is why postfix is often used as it is a great way to simply the expression using a stack-based processor or virtual machine for the computer. One advantage that postfix has over infix is that it is very easily implemented and does not have overhead of parentheses. Evaluating an expression in postfix notation requires scanning from left to right so you know what to do as soon as you encounter an operator in the expression string. Also, with postfix there is no complication of precedence or priorities of one operator over the other.To go into more detail Infix notations require precedence and rules to decypher and make the expressions clearer, or addition of extra parentheses that are not usually considered part of the notation. These expressions are the form of mathematical or arithmetic notation like most people are used to, for example A + B * C . In postfix, the expression would be A B C * +. Again, the order of operations is preserved since the * comes immediately after the B and the C, indicating that * has precedence, with + coming after.




# Question 2

- Explain how Thompson's construction for regular expressions works?

    When working in Programming or computer science environment, Thompson's construction algorithm also called the McNaughton–Yamada–Thompson algorithm, is a method for converting regular expressions to their respective nondeterministic finite automaton. For this perticular technique we are to send a postfix expression into the algorithm to be processed by the computer to convert the expression into our output a nondeterministic finite automata or NFA for short.    
    
    To go into more detail we do this by reducing the regular expression into its smallest regular expression where some special characters for example the ( . * | )  have different functions and priority levels the precedence in which these caracters go by is Kleene Star -> ' * ' first, Then followed by Concatenation -> ' . ' and then lastly the Union/Or  -> ' | ' symbol. Thompson's construction always has a single start state and a single end state these two states are joined by an arrow that is labeled what ever the character is used. When Kleene Star, Concatenation and Union/Or are conjoined with some metacharacters this gives the programmer alot of freedom, For instance searching trough a text documment that might have 50,000 words in it they can use somthing like 'a.b' to seach for any word that has an 'A' followed by a 'B' in it, This is only one example there are many other combinations that can be utilized for different sinarios or what ever the user is tasked to do. 

    Regular expressions and NFA’s portray as two different methods of formal languages. For example, Text processing uses regular expressions to find or find and replace these are advanced search patterns and for NFA’s this is best suited to be processed on a computer as they are more complex also the computer can be more efficient with the process rather than the average user trying to understand them.


# Question 3

- Explain what is meant by the term irregular language in the context of regular expressions?


