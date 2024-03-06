"""
This module defines a function to print 'Hello world of Python' to a provided output stream.
"""

def helloworld(out):
    """
    Prints 'Hello world of Python' to the provided output stream.
    
    Parameters:
        out (file-like object): The output stream to write the message to.
    """
    out.write("Hello world of Python\n")
