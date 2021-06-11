# Java Questions

### What is Java
Java is a high-level, object-oriented, robust, secure programming language, platform-independent, high performance, multithreaded and portable programming language
It was developed by James Gosling in June 1991, it can also be known as the platforms as it provides its own JRE and API

### Difference between JVM, JDK and JRE
**JVM** stands for **Java Virtual Machine**, its a specification that providees a runtime environment in which Java bytecode can be executed. It can also run those programs which are written in other languages and compiled to Java bytecode

JVMs are available form many hardware and software platforms. JVM, JRE and JDK are platform dependent becausse the configuration of each OS is different from each other. However Java is platform independent
The JVM performs 
- Loads code
- Verifies code
- Executes code
- Provides runtime environment


**JRE** stands for **Java Runtime Environment**, which is a set of software tools which are used for developing Java applications
It's used to provide the runtime environment, it's the implementation of JVM, it physically exists, it contains a set of libraries + other files that JVM uses at runtime


**JDK** stands for **Java Development Kit**, is a software development environment which is used to develop Java applications and applets
It physically exists, contains JRE + development tools

JDK is an implementation of any one of the below given Java Platforms released by Oracle Corporation
The JDK contains a private JVM (Java Virtual Machine) and a few other resources such as an interpreter/loader (java), a compiler (javac), an archiver (jar) a documentation generator (Javadoc), etc to complete the development of a Java Application

### What is a Java Applet
An applet is a program written in the Java programming language that can be included in an HTML page, much in the same way an image is included in a page

When you use a Java technology-enabled browser to view a page that contains an applet, the applet's code is transferred to your system and executed by the browser's Java Virtual Machine (JVM)

An applet is a program written in Java, that it's include inside of an HTML file, the idea is to provide a functionality that HTML alone cannot provide

The idea of an applet is to be small enough to provide an specific and defined functionality


### Features of Java Programming language
- **Simple**: Java is easy to learn, its syntax is based on C++ which makes easier to write the program in it
- **Object-Oriented**: Java follows the object-oriented paradigm which allows us to maintain our code as the combination of different type of objects that incorporates both data and behavious
- **Portable**: Java supports read-once-write-anywhere approach. We can execute the Java program on every machine. Java program *.java* is converted to bytecode *.class* which can be easily run on every machine
- **Platform independent**: Java is a platform independent programming language. It's different from other pgoramming languages like C and C++ which needs a platform to be executed. Java comes with its platform on which its code is executed. Java doesn't depend upon the OS to be executed
- **Secured**: Java is secured because it doesn't use explicit pointers. Java also provides the concept of ByteCode and Exception whandling which makes it more secured
- **Robust**: Java is a strong programming language as it uses strong memory management. The concepts like Automatic garbage collection, Exception hanlding, etc, make it more robust
- **Architecture neutral**: Java is architectural neutral as it's not dependent on the architecture (32 or 64 bits)
- **Interpreted**: Java uses the Just-in-time (JIT) interpreter along with the compiler for the program execution
- **High Performance**: Jav is faster than other traditional interpreted programming languages because Java bytecode is "close" to native code, it's still a bit slower than a compiled language like C++
- **Multithreaded**: We can write Java programs that deal with many tasks at once by defining multiple threads. The main advantage of multi-threading is that it doesn't occupy memory for each thread, it shares a common memory area. Threads are important for multimedia, web apps, etc
- **Distributed**: Java is distributed because it facilitates users to create distributed applications in Java
- **Dynamic**: Java is a dynamic language. It supports dynamic loading of classes, which means classes are loaded on demand. It also supports functions from its native languages

### What is JIT compiler?
*Just-In-Time Compiler* (JIT) it's used to improve the performance. JIT compiles parts of the bytecode that have similar functionality at the same time, and hence reduces the amount of time needed for compilation. Here the term "compiler" refers to a translator from the instruction set of a Java virtual machine (JVM) to the instruction set of a spectific CPU

### What is the platform?
A platform is the hardware or software environment in which a piece of software is executed. There are two types of platforms, software-based and hardware-based. Java provides the software-based platform

### What are the main differences between the Java platform and other platforms>
- Java is the software-based platform whereas other platforms may be the hardware platforms or software-based platforms
- Java is executed on the top of other hardware platforms whereas other platforms can only have the hardware components

### What gives Java is 'write once and run anywhere' nature?
The bytecode. Java compiler converts the Java programs into the class file (byte code) which is the intermediate language between source code and machine code. This bytecode is not platform specific and can be executed on any computer

### Is emplty .java file name a valid source file name?
Yes, Java allows to save our java file by  *.java* only, we need to compile it by *javac* and run by *java classname*
```sh
# save by .java only
class A{
	public static void main(String args[]) {
		System.out.println("Hello Java");
	}
}

# Compile by javac .java
# Run by java A
```

### What if I write static public void instead of public static void?
The program compiles and runs correctly because the order of specifiers doesn't matter in Java

### What are the various access specifiers in Java?
In Java, access specifiers are the keywords which are used to define the access scope of the method, class or variable. In Java, there are four access specifiers give below
- **Public** The classes, methods or variables which are defined as public can be accessed by any class or method
- **Protected** Protected can be accessed by the class of the same package, or by the sub-class of this class, or within the same class
- **Default** Default are accesible within the package only. By default, all the classes, methods and variables are of default scope
- **Private** The private class, methods or variables defined as private can be accessed within the class only

### What is the purpose of static methods and variables?
The methods or variables defined as static are shared among all the objects of the class. The static is the part of the class and not of the object. The static variables are stores in the class area, and we don't need to create the object to access such variables. Therefore, static is used in the case, where we need to define variables or methods which are common to all the objects of the class

*For example, in the class simulationg the collection of the students in a college, the name of the college is the common attribute to all the students. Therefore, the college name will be defined as static*

### What is the output of the following Java program?
```sh
    class Test   
    {  
        public static void main (String args[])   
        {  
            System.out.println(10 * 20 + "Javatpoint");   
            System.out.println("Javatpoint" + 10 * 20);  
        }  
    }  
```
200Javatpoint
Javatpoint1020