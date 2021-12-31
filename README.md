# Coding Practice: Valid Subsequence Solution 2
This project is meant for me to practice coding interview questions with Python.
In this project, I am presented with the following task: given two 
non-empty arrays of integers, write a function that determines whether the 
second array is a subsequence of the first array. 

Important information to note: a subsequence of an array is a set of numbers 
that aren't necessarily adjacent in the array but that are in the same order 
as they appear in the array. For example, the numbers [1, 3, 4] are a 
subsequence of the array [1, 2, 3, 4]. A single number in an array and the 
array itself are both subsequences.

## Running The Project
**NOTE: Your IDE may configure the project implicitly as a module. BE SURE TO 
RUN STEP 4 BELOW BEFORE SUBMITTING LABS** 

1. Download and install Python on your computer
2. Navigate to the [ValidateSubsequnceSol1.Mod1]() directory
3. Run the program as a module: `python -m Mod1 -h`. This will print the help 
   message.
4. Run the program as a module (with real inputs): `python -m Mod1 <random 
   input file> <random output file>`
   a. IE: `python -m Mod1 input.txt output.txt`

The program's output will be displated in the output.txt file.

### Lab1 Usage:

```commandline
usage: python -m Mod1 [-h] 

optional arguments:
  -h, --help  show a help message and exits the program
```

Usage statements are very formalized

| Symbol    | Meaning   |
| ---           | ---       |
| [var]         | variable var is optional. |
| var           | variable var is required. All positional arguments are required.|
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values |
| *             | This argument consumes 0 or more values |

### Project Layout

The following was my project's package layout:

* TwoNumberSum.Mod1/: `The parent or "root" folder containing all of the 
  projecs files`
    * README.md:
      `The README files that describes my programs and the nuances needed 
      to run the program`
    * Mod1/: 
      `The module of my program (per requirement).`
      * __init__.py 
        `This python file details critical functions, variables, and 
        classes that are exposed when scripts import the Lab1 module.`
      * __main__.py 
        `The starting point when the program runs, it handles command line 
        arguments.`
      * *.py 
        `Holds the scripts that perform the code.`