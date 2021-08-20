# Graph Theory Autumn Project 2021


**Student ID:** G00372370


# Instructions on How to Run

Once you have cloned the repository and have python installed on your computer open visual studio code terminal and begin to type in the command line these commands - python3 GraphTheoryAutumnProject2021.py a.b input.txt. If you have entered all of this correctly then the program will output the number of matches it has found in the text file. You can also enter once again in the command line the command - python3 GraphTheoryAutumnProject2021.py -h for help or some info on the program.

# Explanation of Algorithm

Edsger Dijkstra developed his "Shunting Yard" algorithm to convert an infix expression into a postfix expression. In computer science, the shunting-yard algorithm is a method for resolving mathematical expressions in most commonly infix notations. the shunting yard algorithm is stack-based. Infix expressions are the form of mathematical notation most people are used to, for instance "3 + 4" or "3 + 4 × (2 − 1). For the conversion there are two text variables the input and the output. There is also a stack that holds elements and sorts them into a que where some elements may have a higher priority than others this is implemented by moving aside less important elements so that more important elements can be handles first. Thomson’s algorithm is another that I used is a method of transforming a regular expression into an equivalent nondeterministic finite automaton. This NFA can be used to match strings against the regular expression. For this project i Read in a text file that i used a Nfa stack to loop through, We also had to ouput the number of matches that were relavent to the contents in a text file . This algorithm is credited to Ken Thompson.


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

    When talking about or programming with irregular languages also known as non regular languages the goal is to assume that the languages at question or the ones that we are unsure about are regular.How does one prove that a language is not regular? We could try proving that there is no DFA or NFA that accepts it, or no Regular Expression or Regex for short that generates it, but this kind of testing is generally rather difficult to make. It is hard to rule out all possible automata and possible regular expressions. Instead, we will look at a property that all regular languages have; proving that a given language does not have this property then becomes a way of proving that that language is not regular. Another problem we have with regex is that given an expression of the non-regualr sort but the parameter value is a constant then the language is regular. To prove that a language is not regular, we use proof by contradiction keeping in mind that all regualr languages can be designed using finite state machines and we know most of the properties for these and we also know there limitations and becasue of their limitations some languages that cannot be designed using finite state machines and this is where we can classify these languages ans non regular this is where The Pumping lemma technique comes in handy becasue it can be only used to prove if a language is irregular using this Method - 
    
    If 'A' is a regular language then 'A' has a puming length of 'P' such that any string 'S' where the length of the string is greater than or equal to the pumping length may be divided into 3 parts S = x y z such as the following conditions must be true

                            (1) If you increase Y any number of times and the string you obtain after increasing Y must also belong to A that is the language.

                            (2) The length of Y should be greater than zero
                            (3) X and Y must be less than or equal to P The pumping length

    So in conclusion for a language to be regular all 3 of these conditions conditions must be true if not and cannot satisfy all the conditions at the same time that means S cannot be pumped in the result of this their is a Contradiction and it become irregular.
    
# Refrences

Q1 - http://www.cs.man.ac.uk/~pjj/cs212/fix.html

Q2 - https://en.wikipedia.org/wiki/Thompson%27s_construction

     https://en.wikipedia.org/wiki/Regular_expression

Q3 - https://www.youtube.com/watch?v=Ph7Z9YttM0Q&ab_channel=lydia