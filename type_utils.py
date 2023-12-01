def is_type_or_raise(value, name, expected_type):
    """
    Check if a value is of the expected type and raise an exception if not.

    This function validates whether the provided value adheres to the specified type requirement. 
    If the value is None, it raises an InvalidValueError. 
    If the value's type does not match the expected type, an InvalidTypeError is raised.

    Parameters:
    - value: The value to be checked.
    - name (str): A descriptive name or identifier for the value being checked.
    - expected_type (type): The expected type that the value should conform to.

    Raises:
    - InvalidValueError: If the provided value is None.
    - InvalidTypeError: If the type of the provided value does not match the expected type.

    Returns:
    - None: If the value passes the type check.

    Example:
    >>> is_type_or_raise(42, "example_value", int)
    None

    Note:
    The function utilizes custom exception classes, InvalidValueError and InvalidTypeError, to provide
    more specific information about the encountered issue.

    """
    if value is None:
        raise ValueError(f"{name} cannot be None.")
    
    if not isinstance(value, expected_type):
        raise TypeError(f"{name} must be of type {expected_type.__name__}.")
    
    return None


