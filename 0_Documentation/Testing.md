# Python Programming: Variables, Data Types, and Control Flow

## Short Answer Quiz

Instructions: Answer the following questions in 2-3 sentences each.

### 1.  What is a variable in Python, and how is it used?

    A variable is a named location in memory that stores a value. It is used to represent and manipulate data within a program. For example, name = "Alice" creates a variable named "name" and assigns the value "Alice" to it.

### 2.  Explain the purpose of an assignment statement in Python. Provide an example.

    An assignment statement creates a variable and assigns a value to it using the assignment operator (=). The value on the right side of the operator is assigned to the variable on the left side. For example, age = 25 assigns the value 25 to the variable "age".

### 3.  Describe three rules for naming variables in Python.

    (1) Variable names cannot be Python keywords, such as if, else, or while. 
    (2) Variable names cannot contain spaces. 
    (3) The first character of a variable name must be a letter or an underscore. Other characters in the name can be letters, digits, or underscores. For example, my_variable and _variable1 are valid variable names.

### 4.  What is the difference between the int and float data types in Python?

    The int data type represents whole numbers (integers), while the float data type represents numbers with decimal points (floating-point numbers). For example, 10 is an int and 3.14 is a float.

### 5.  How can you read input from the keyboard in Python?

    You can read input from the keyboard using the built-in input() function. This function pauses the program and waits for the user to type input and press enter. For example, name = input("Enter your name: ") prompts the user to enter their name and stores the input in the variable "name".

### 6.  What is an f-string and how is it used to format output in Python?

    An f-string is a string literal prefixed with the letter 'f'. It allows you to embed expressions within the string using curly braces {}. These expressions are evaluated and inserted into the string during runtime. For example, f"My name is {name}" would replace {name} with the value of the variable name.

### 7.  Explain the purpose of format specifiers in Python. Provide an example.

    Format specifiers are used to control how values are displayed within f-strings. They are placed after a colon within the curly braces. For example, f"{num:.2f}" displays the value of the variable num as a floating-point number rounded to two decimal places.

### 8.  What is a decision structure in programming?
    
    A decision structure is a programming construct that allows the program to choose between different paths of execution based on a condition. It allows for conditional execution of code, meaning that certain blocks of code will only run if specific conditions are met.

### 9.  Describe the difference between a single-alternative and a dual-alternative decision structure.

    A single-alternative decision structure, like an if statement, executes a block of code only if a condition is true. A dual-alternative decision structure, like an if-else statement, provides two paths: one block executes if the condition is true, and another block executes if the condition is false.

### 10. What is a loop in programming, and what are the two main types of loops?

    A loop is a programming construct that repeatedly executes a block of code until a specific condition is met. The two main types of loops are condition-controlled loops, which repeat as long as a condition is true (e.g., while loops), and count-controlled loops, which repeat a specific number of times (e.g., for loops).

## Essay Questions

Explain the concept of data types in programming, and discuss the importance of using appropriate data types for different kinds of information. Use examples from Python to illustrate your points.

**Describe the role of the print() function in Python, and explain how you can use it to display multiple items and format the output using escape characters, item separators, and f-strings. Provide specific examples.**

**Discuss the concept of decision structures in programming. Explain the syntax and behavior of the if, if-else, and if-elif-else statements in Python, providing examples for each.**

**Explain the concept of loops in programming. Compare and contrast condition-controlled loops (while loops) and count-controlled loops (for loops) in Python, discussing their syntax, use cases, and how they are controlled.**

**Discuss the importance of modular programming. Explain the benefits of using functions and modules, and describe how to define and call functions in Python, as well as how to import and use modules.**

## Glossary of Key Terms

Term/Definition

**Variable**  A named location in memory used to store a value.

**Data Type**  A classification of data that determines how it is stored and manipulated (e.g., integer, floating-point, string).

**Assignment Statement**  A statement that creates a variable and assigns a value to it.

**Assignment Operator**  The equal sign (=) used to assign a value to a variable.KeywordA reserved word in a programming language that has a special meaning and cannot be used as a variable name.

**Numeric Literal**  A number written directly in the code (e.g., 10, 3.14).

**String**  A sequence of characters enclosed in quotation marks.

**f-string**  A formatted string literal that allows embedding expressions using curly braces.

**Format Specifier**  A code used within an f-string to control the display of a value.

**Decision Structure**  A programming construct that allows the program to execute different blocks of code based on conditions.

**Condition**  An expression that evaluates to either true or false.

**Boolean Expression**  An expression that results in a Boolean value (true or false).

**Loop**  A programming construct that repeatedly executes a block of code.

**Condition-Controlled Loop**  A loop that repeats as long as a condition is true (e.g., while loop).

**Count-Controlled Loop**  A loop that repeats a specific number of times (e.g., for loop).

**Function**  A block of reusable code that performs a specific task.

**Module**  A file containing Python code that can be imported and used in other programs.

**Import Statement**  A statement used to bring code from a module into the current program.

**Argument**  A value passed to a function when it is called.

**Parameter**  A variable in a function definition that receives the value of an argument.

**Scope**  The region of a program where a variable can be accessed.

**Global Variable**  A variable that can be accessed from anywhere in the program.

**Local Variable**  A variable that can only be accessed within the function where it is defined.

**Return Statement**  A statement used to send a value back from a function to the code that called it.

Key takeaways

1. Python supports the following logical operators:

and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.

2. You can use bitwise operators to manipulate single bits of data. The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
<< does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

* -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.


