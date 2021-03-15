"""
(c) Microsoft. All rights reserved.
"""
import sys
sys.path.append("./src")
from src.paramvalidator import ParameterValidator, ParameterValidationException

"""
This file tests ParameterValidator on standalone Python methods.
"""


"""
In this case our method pre-defines all of it's parameters, i.e. 

int, string, list

The int and string are required, but the list is not.

ParameterValidator inputs line up directly against the defined parameters 
in the method signature. 
"""    
@ParameterValidator((int, False, (3,5)), (str, False), (list, True))
def myfunc(num, str, list):
    print("Hello from standalone function")


# Splatting
single_args = [3, "hey", None]
print("Standalone Args Splatting - success")
myfunc(*single_args)


# Standard call but make first parameter None where it's not allowed
try:
    print("Standalone Args Standard - failure on invalid type for parameter")
    myfunc("1", "hey", None)
except ParameterValidationException as ex:
    print("\tException caught", ex.__class__.__name__)
    print("\t",str(ex))

# Standard call but make first parameter None where it's out of range
try:
    print("Standalone Args Standard - failure on range of parameter")
    myfunc(1, "hey", None)
except ParameterValidationException as ex:
    print("\tException caught", ex.__class__.__name__)
    print("\t",str(ex))

"""
In this case our method pre-defines all of it's parameters, i.e. 

int, string, list

The int and string are required, but the list is not (as with the above function).

ParameterValidator inputs are defined as any kwargs would be for any other entry point. 
The difference being, there is no one to one mapping here and those identified should 
generally be thought of as required parameters for your method to work. 
    
However, if the tuple bool value is True, if the parameter is not in kwargs it will
not produce a failure.  
"""    
@ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
def mykwfunc(**kwargs):
    print("Hello from kwargs standalone function")


print("Standalone Kwargs Standard - success")
mykwfunc(age=25, name="Fred Jones")

try:
    print("Standalone Kwargs Standard - failure on missing required param")
    mykwfunc(age=25)
except ParameterValidationException as ex:
    print("\tException caught", ex.__class__.__name__)
    print("\t",str(ex))
