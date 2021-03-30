#
#(c) Microsoft. All rights reserved.
#
"""This file tests ParameterValidator on standalone Python methods."""
import sys
import os
import typing 

attempts=1
found=False
cur_path = os.getcwd()

while not found:
    if os.path.exists(os.path.join(cur_path, 'src')):
        sys.path.append(os.path.join(cur_path, 'src'))
        found = True
    cur_path = os.path.split(cur_path)[0]
    if attempts >= 3:
        break
    attempts += 1

from paramvalidator import ParameterValidator, ParameterValidationException
from paramvalidator.exceptions import (
    ParameterNoneValidationException,
    ParameterTypeValidationException,
    ParameterKwargValidationException,
    ParameterCountValidationException,
    ParameterRangeValidationException
)


def test_predefine_params_args():
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


    # Splatting - OK
    single_args = [3, "hey", None]
    print("Standalone Args Splatting - success")
    myfunc(*single_args)


    # Splatting - Too many arguments
    single_args.append("One too many")
    try:
        print("Standalone Args Splatting - success")
        myfunc(*single_args)
    except ParameterValidationException as ex:
        assert(isinstance(ex, ParameterCountValidationException))
        print("\t",str(ex))

    # Standard call but make first parameter None where it's not allowed
    try:
        print("Standalone Args Standard - failure on invalid type for parameter")
        myfunc("1", "hey", None)
    except ParameterValidationException as ex:
        assert(isinstance(ex, ParameterTypeValidationException))
        print("\t",str(ex))

    # Standard call but make first parameter None where it's out of range
    try:
        print("Standalone Args Standard - failure on range of parameter")
        myfunc(1, "hey", None)
    except ParameterValidationException as ex:
        assert(isinstance(ex, ParameterRangeValidationException))
        print("\t",str(ex))

    try:
        print("Standalone Args Standard - failure on range of parameter")
        myfunc(None, "hey", None)
    except ParameterValidationException as ex:
        assert(isinstance(ex, ParameterNoneValidationException))
        print("\t",str(ex))

def test_predfined_params_kwargs():
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
        assert(isinstance(ex, ParameterKwargValidationException))
        print("\t",str(ex))

    try:
        print("Standalone Kwargs Standard - failure on missing required param 2")
        mykwfunc()
    except ParameterValidationException as ex:
        print("\t",type(ex), str(ex))
        assert(
            isinstance(ex, ParameterKwargValidationException)
            or
            isinstance(ex, ParameterCountValidationException)
            )

def test_params_mixed():

    @ParameterValidator((int, False), name=(str,False))
    def mymixedfunc(num, **kwargs):
        print("Hello from standalone function")

    print("Standalone Mixed - ok")
    mymixedfunc(3, name="Name")

    try:
        print("Standalone Mixed - failure on missing required param")
        mymixedfunc(3)
    except ParameterValidationException as ex:
        assert(isinstance(ex, ParameterKwargValidationException))
        print("\t",str(ex))

