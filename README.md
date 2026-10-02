# GradeTracker
Basic Grade Tracker that calculates your grades based on assignments.

## Installation

Clone the github repository

```bash
git clone git@github.com:CrChromium/GradeTracker
```

## Usage

To use the program, run the following commands

```bash
cd GradeTracker
python main.py
```

The program has 6 operable functions:

### add

This function lets you add grades to a class

It first will ask for the number of assignments to add  
For each assignment, it requires a class name, assignment name, assignment category, and assignment grade

### add_class

This function lets you add a new class to grades.json

It requires class name as an input.

### calculate

This function returns the grade average for a specified class.

Any categories with no assignments are assumed to be 100%

It requires class name as an input.

### view

This function lets you view the grades for a class.

It requires class name as an input.

### remove

This function lets you remove an assignment from a class.

It requires class name and assignment name as an input.

### exit

exit terminates the function.
