# Introduction

This code provides two failure criterion plots - Tresca and von Mises, based on user input of yield strength and principal stresses. This code can be useful for materials engineers or mechanical designers who are interested in understanding whether a material will fail or not under certain loading conditions.

## Code Structure

The code is written in Python and consists of a single file. The code has a class called MaterialFailure which contains two methods TrescaCriterionPlot() and vonMisesCriterionPlot(). These methods take the user input of yield strength and principal stresses and plot the corresponding failure criterion.

The code uses the numpy and matplotlib libraries to perform numerical calculations and create plots respectively.
User Input

## The user needs to input the following parameters:

    sy: Yield strength (in MPa)
    s1: Principal stress 1 (in MPa)
    s2: Principal stress 2 (in MPa)

## Methods
MaterialFailure class

This class initializes the input values of yield strength and principal stresses.
__init__(self,sy,s1,s2)

This method takes three arguments - sy, s1, and s2 and initializes them as instance variables.
TrescaCriterionPlot()

This method plots the Tresca failure criterion. It takes no arguments and returns a plot.
vonMisesCriterionPlot()

This method plots the von Mises failure criterion. It takes no arguments and returns a plot.
## Libraries Used

The code uses the following libraries:
numpy

This library is used to perform numerical calculations.
matplotlib

This library is used to create plots.
## Usage

To use this code, follow these steps:

    Install the numpy and matplotlib libraries using the following commands:

pip install numpy
pip install matplotlib

    Copy the code into a file with a .py extension.

    Import the MaterialFailure class from the file:

python

from <filename> import MaterialFailure

    Create an instance of the MaterialFailure class with the user input values:

python

x = MaterialFailure(sy,s1,s2)

    Call the TrescaCriterionPlot() and vonMisesCriterionPlot() methods on the instance:

python

x.TrescaCriterionPlot()
x.vonMisesCriterionPlot()

    The code will display two plots showing the Tresca and von Mises failure criteria.



## Authors
This tool was created by UG Aerospace Engineering students at R.V College of Engineering,
under the guidance of Prof. Benjamin Rohit (Department of Aeropace Engineering, RVCE) as part of their Experinential Learning.

## License
This tool is licensed under the MIT License. See the LICENSE file for more details.
