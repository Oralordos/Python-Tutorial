# Code packages

Create a Python package with at least three modules. The package itself counts as a module.

* The package root should have a function for saying hello and a function for saying goodbye to a user.
* One of the modules should have at least three math related functions.
* One of the modules should have at least two string related functions.

Each module should run its functions when it is the main module, and print the results. When it is imported, it should be silent.
Each function should have documentation explaining the expected inputs and outputs.
At least one function should use another module in its calculations. Good candidate functions are below.

After the package is made, activate setuptools develop mode or install the package,
and write a main package which uses at least one function from each module.

Good functions in other modules:
* math.sqrt
* math.sin
* math.cos
* math.tan
* time.cTime
* time.sleep
* random.randint
* random.choice
* random.shuffle
* getpass.getuser
