# Equivalent Circuit
#### Video Demo:  <https://www.youtube.com/watch?v=Of_91h3m_2E&feature=youtu.be>
#### Description: A Web Application developed in python to assist in calculating the equivalent resistance of transformers from measurements made in open circuit and short circuit tests.To determine the internal resistances of a transformer, we need to do tests with it at no load and at full load. For this, we apply voltage in the primary or secondary while the other side is shorted or with an open circuit, then we measure the voltages and currents. With the voltage and current data, we can calculate the internal resistances, and this is what my application does. 

**`application.py`**  

In application.py is my python code.  
It starts by importing Flask, render_template to use templates and flask.  
Then, it imports 'math' for the use of advanced mathematical operations.  
A function called 'decimal' is declared now, but it is quite simple: it just formats the final output to a number with two places after the comma and adds k or m for better reading.  
```
app = Flask(__name__)
```  
Inicializes flask.
The first **route**, '/', uses the **get** and **post** methods. Note that if the method is **get**, it immediately returns the **index.html** template.  
When the method is **post**, it means that the user has submitted the form data contained in **index.html**. The program will then handle the data, transforming them all into float, make all the mathematical calculations and deliver the new variables already formatted to be displayed in **results.html**.  

**`index.html`**   

This is the first page to which the user will be directed when opening the link. It starts by setting the language and characters. Imports **bootstrap**, the CSS stylesheet and favicon.  
Inside **main** are the bootstrap form codes. They are all **required** and accept only positive numbers. Each of them sends a variable to the **back-end**.  

**`results.html`**   

**results.html** starts with the same settings as **index.html**.
In main, there is a script that will be explained later.

In **main** there are also **nav-menus** with their specific content.
Each of them is hidden by the **hidden** class.
Nav-menus are configured so that when clicked, they call Javascript functions.

Each of these functions is in the initial **script** and has the navigation effect that Nav-menus have.  
Each of them displays one of the contents while hiding all the others.  

**`static`**   

Here are the static files: images, CSS stylesheet, and the favicon.ico.
