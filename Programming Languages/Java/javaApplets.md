# Java Applets
*It is important to know that Java applets are deprecated from Java in 2017 and have been completely removed from Java SE 11 released in September 2018*

## What is an Applet?
An applet is a Java Program that can be embedded into a web page
It runs inside the web browser and works at client-side
An applet is embedded in an HTML page using the APPLET or OBJECT tag and hosted on a web server
Applets are used to make website more dynamic and entertaining

## Important points for a Java developer
1. All applets are sub-classes of *java.applet.Applet* class
2. Applets are not stand-alone programs. Instead they run within either a web browser or an applet viewer. JDK provides a standard applet viewer tool called applet viewer
3. In general, execution of an applet does not begin at *main()* method
4. Output of an applet window is not performed by *System.out.println()*. Rather it is handled with various AWT methods, such as *drawString()*

## Life cycle of an applet
*When an applet begins, the following methods are called*
1. init()
2. start()
3. paint()

*When an applet is terminated, the following sequence of methods calls take place*
1. stop()
2. destroy()

## Example of a Hello World applet
```java
import java.applet.Applet;
import java.awt.Graphics;

public class HelloWorld extends Applet {
	@Override
	public void paint (Graphics g) {
		g.drawString("Hello World", 20, 20);
	}
}
```
