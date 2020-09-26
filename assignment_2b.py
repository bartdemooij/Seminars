"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    The first argument string_1 will be turned into a lowercased version of the string, while string_2 will be turned into a uppercased version of the string. 
    This function returns a dictionary of string_1 as lower case, string_2 as upper case and a combination of the two.
    
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
