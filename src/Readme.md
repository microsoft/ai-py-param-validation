# Parameter Validation
When developing software, one of the lowest hanging fruit items you can choose to manage is validation of parameters being passed to your methods.

This is true whether the method is free standing (outside a class) or contained within a class.

This repo has a decorator class that can be used in both cases.

## Usage
To use this functionality, you need to use the validation_decorator.ParameterValidator to decorate your methods.

Regardless of method type there are multiple options, with examples:

1. A function that has all predefined arguments
```python
    """
    Have to define an entry for each incoming parameter, in this case 2 ints
    that cannot be None
    """
    @ParameterValidator((int, False), (int, False))
    def myfunc(param1, param2)
```
2. A function that has only kwargs
```python
    """
    Define only the arguments you expect. In this case one int (count) and 
    one string (name) where neither can be None. 

    If passed True (can be None) no error is thrown if the field is not in kwargs.
    """
    @ParameterValidator(count=(int, False), name=(str, False))
    def myfunc(**kwwargs)
```
3. A function with mixed predefined args and kwargs
```python
    """
    A mix of above, for all predefined arguments you MUST have an entry, but 
    for kwargs define only what you want to verify.
    """
    @ParameterValidator((int, False), name=(str, False))
    def myfunc(count, **kwwargs)
```

### Validation Tuples
In all cases there is a validation tuple defined as 

||||
|--|--|--|
|t[0]|Required|Type of parameter to expect.|
|t[1]|Required|Boolean True or False indicates whether the value can be None (True) or must have a valid value (False)|
|t[2]|Optional|If present it contains a tuple with an acceptable range in (low,high) format. This will only be validated on int/float argument types.|


### 1 - Function has well defined arguments
If you have well defined arguments such as below, this is straight forward

```python
"""
This function takes two parameters, both of which are expected to be integers.

NOTE: No range provided, for range tests see test_standalone.py

There MUST be the same number of definitions passed to ParameterValidator as the number of parameters passed to the method itself.
"""
@ParameterValidator((int, False), (int, False))
def add(num: int, num: int):
    print("Hello from standalone function")

# And you can validate int/floats with a range such as 
@ParameterValidator((int, False,(3,5)), (int, False,(500,1000))
def add(num: int, num: int):
    print("Hello from standalone function")
    
```

### 2 - Function takes a variable number of parameters in kwargs (dict)
```python
"""
This function takes only the kwargs parameter.

However, internally the function will expect two parameters pass (contrived, yes) for left and right.

The input to ParameterValidation is a kwargs input where the name of the parameter is the name expected to be found in kwargs, the value is a tuple identical to that used above.

In this instance, only the incoming values in kwargs are validated against the input to the ParameterValidator class. There can be more parameters, but those will not be tested.

In reality, the check should be on inputs that you EXPECT to be there.
If you allow None (type,True) and the parameter is not in kwargs, no error will be raised.
"""
@ParameterValidator(left=(int, False), right=(int, False))
def add(**kwargs):
    print("Hello from standalone function")
```

## Example 1 - Standalone Function with defined arguments

Standalone method with arguments
```python
@ParameterValidator((int, False), (str, False), (list, True))
def myfunc(num, str, list):
    print("Hello from standalone function")
```
Test it using splatting and with set parameters
```python
# Splatting
single_args = [1, "hey", None]
print("Standalone Args Splatting -")
myfunc(*single_args)

# Standard call
print("Standalone Args Standard -")
myfunc(1, "hey", None)
```

# Example 2 - Standalone function using kwargs
Function
```python
# Test standalone method with kwargs
@ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
def mykwfunc(**kwargs):
    print("Hello from kwargs standalone function")
```
And test this
```python
print("Standalone Kwargs Standard -")
mykwfunc(age=25, name="Fred Jones")
```

# Example 3 - Class with both types of functions
Class definition:
```python
class TestDecorator:
    def __init__(self):
        pass

    @ParameterValidator((int, False), (str, False), (list, True))
    def myfunc(self, num: int, str: str, list: typing.List[object]):
        print("Hello from class method")

    @ParameterValidator(age=(int, False), name=(str, False), addresses=(list, True))
    def mykwfunc(self, **kwargs):
        print("Hello from kwargs class function")
```
And finally, test the class
```python
td = TestDecorator()
print("Class Args Standard -")
td.myfunc(1, "str", [])
print("Class Kwargs Standard -")
td.mykwfunc(age=25, name="Fred Jones")
```