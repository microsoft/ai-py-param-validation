#
#(c) Microsoft. All rights reserved.
#
"""
This file tests out using ParameterValidator on class methods. Note that you CAN
use it on the __init__ function as well assuming you have parameters other than self.
"""
import sys
import typing
sys.path.append("./src")
from src.paramvalidator import ParameterValidator, ParameterValidationException


class TestClass:
    def __init__(self):
        pass

    """
    In this case our method pre-defines all of it's parameters, i.e. 

    int, string, list

    The int and string are required, but the list is not.

    ParameterValidator inputs line up directly against the defined parameters 
    in the method signature. 
    """    
    @ParameterValidator((int, False), (str, False), (list, True))
    def myfunc(self, num: int, str: str, list: typing.List[object]):
        print("Hello from class method")

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
    def mykwfunc(self, **kwargs):
        print("Hello from kwargs class function")


def test_class():
    td = TestClass()
    print("Class Args Standard - success")
    td.myfunc(1, "str", [])

    try:
        print("Class Args Standard - inappropriate None")
        td.myfunc(None, "hey", None)
    except ParameterValidationException as ex:
        print("\tException caught", ex.__class__.__name__)
        print("\t",str(ex))

    print("Class Kwargs Standard - success")
    td.mykwfunc(age=25, name="Fred Jones", uncheckedvalue="this will not be checked")

    try:
        print("Class Args Standard - invalid data type")
        td.mykwfunc(age=25, name="hey", addresses="main st")
    except ParameterValidationException as ex:
        print("\tException caught", ex.__class__.__name__)
        print("\t",str(ex))
