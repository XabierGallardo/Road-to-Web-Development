# Programming Questions

### Is JavaScript single thread or multi thread?
It’s not multi threaded. Tough JavaScript is single threaded, it is asynchronous in nature, which means unlike other languages it doesn’t wait for external operations and pick next task from loop and come back to old task when external operations are finished

*Ex. If you are making an HTTP request or reading from database, JavaScript will initiate the task and move on to other task without waiting for compleition of http/database request*

JavaScript implements a concept called event loop which you can visualize as queue which stores all pending tasks to be done, and it executes tasks from this queue one by one.
When any task starts waiting for any external operation to complete, JavaScript just jumps to another task from queue. When the external operation is completed, task is pushed again to the even queue for execution

### Can you enumerate and explain the various types of errors that can occur during the execution of a computer program?
-** Logical errors**: This occurs in the scenario of a computer program implementing the wrong logic. There are no reports generated for these types of programming errors and they are the most difficult ones to dealt with

- **Runtime errors**: Occurs when the program contains an illegal operation (dividing a number by 0). These are the only errors that are displayed instantly during the program execution. The program execution is stopped and a diagnostic message is displayed

- **Syntax errors**: Occurs when one or more grammatical rules of the pgoramming language being used is violated, such errors are detected during compile time

### Explain an algorithm
An algorithm can be defined as a set of finite steps that when followed helps in accomplishing a particular task
Important features of an algorighm are clarity, efficiency and finiteness

### What do you understand by maintaining and updating a computer program?
The maitenance and updating process of a computer program starts post its succesful installation
While program maintenance is the continuous process of monitoring the computer program for bugs and errors, updating the computer program means making it better with minor and major changes over time

### Provide a brief explanation on variables
Variables are used for storing the input of a program as well as the computational results during program execution
These are actually named memory locations, the value stored in a variable can change during the program execution

### Every programming language has reserved words, what are they?
Reserved word, also known as keywords are the words that have predefined meaning in a particular programming language
These reserved words can't be used for redefined for serving other purposes
In **Java** we have *abstract, boolean, catch, class, const, double, enum, finally, implements*

### What do you understand by loops?
A loops is a structure in programming that can repeat a defined set of statements for a set of number of times or untila a particular condition is satisfied

### Explain program documentation, why is it important?
Program documentation is the written description of the algorighm, coding method, design, testing and proper use of a particular computer program
It is valiable for those who use the program on a day-to-day basis and also for the programmers who are meant to corrent, modify and update the computer program

The main focus of program documentation is development, maintenance and knowledge transfer to other developers

### What are constants?
A constant is a programming entity whose value can't be changed or modified during program execution

### Explain the operators
Operators are used for performing certain operations on data in a computer program
These are represented by symbols
- **Arithmetic**: Used for carrying out mathematical operations
- **Assignment**: Used for storing computational results, strings and values in variables
- **Logical**: Used for allowing a computer program to make a decision based on multiple conditionals. Logical operators allow combining simple conditions to form more complex conditions
- **Relational**: Used for defining or testing some kind of relation between two entities. These operators evaluate to either true or false and produce a non-zero value

### Explain arrays
Arrays are programming structures that are a collection of several data values

### Explain program execution
Program execution is the process of carrying out instructions innate to the program by the computer
Before execution, the computer program is required to be loaded into the memory (RAM) of the computer

### What do you understand by program implementation?
Post the successful completion of software testing of a computer program, it needs to be installed and put into operation on the targeted computer
This process of installing and setting up the computer program to be used by end-users is termed as program implementation

### What is debugging?
During the testing of a computer program, a number of issues are discovered, these are called errors and bugs
Debugging is teh process of correcting them, in other words, debugging is the process of correcting the failures discovered in the implemented code

### What is a recursive function?
A function that calls itself is called a recursive function
It's based on a terminating condition and uses a stack, the phenomenon is called recursion

