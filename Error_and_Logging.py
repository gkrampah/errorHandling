#!/usr/bin/env python
# coding: utf-8

# ## Exceptions versus Syntax Errors
# * Syntax errors occur when the parser detects an incorrect statement
# * exception error occurs whenever syntactically correct Python code results in an error.
# * We can use raise to throw an exception if a condition occurs. The statement can be complemented with a custom exception. The program comes to a halt and displays our exception to screen, offering clues about what went wrong.

# In[21]:


x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


# ## The AssertionError Exception
# 
# Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. We assert that a certain condition is met. If this condition turns out to be True, then that is excellent! The program can continue. If the condition turns out to be False, you can have the program throw an AssertionError exception. The program comes to a halt and displays our exception to screen, offering clues about what went wrong.

# In[24]:


x = 10
assert (x<5), "x is indeed greater than 10"


# ## The try and except Block: Handling Exceptions
# if we dont want the program to terminate when an exception is encountered. Without a try-except block, the last line wouldn’t be reached as the program would crash.

# In[7]:


try: 
    1 / 0
except ZeroDivisionError: 
    print('Divided by zero')

print('Should reach here')


# In[31]:


import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
    
linux_interaction()


# In[28]:


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')


# In[32]:


try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')


# In[29]:


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)


# In[15]:


def process_positive_integer(number):
    if number <= 0:
        raise ValueError("Input must be a positive integer.")
    return number * 2



try:
    result = process_positive_integer(-5)
except ValueError as e:
    print(f"An error occurred: {e}")


# ## The else Clause
# In Python, using the else statement, you can instruct a program to execute a certain block of code only in the absence of exceptions.

# In[33]:


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')


# In[34]:


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)


# In[11]:


filename = "example.txt"

try:
    with open(filename, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"File not found: {filename}")
    # Handle the missing file here
except IOError:
    print(f"An I/O error occurred while reading {filename}")
    # Handle the I/O error here
else:
    # Process the data from the file
    print(f"Successfully read data from {filename}")


# ## Cleaning Up After Using finally
# Imagine that you always had to implement some sort of action to clean up after executing your code. Python enables you to do so using the finally clause.
# 
# 

# In[8]:


try:
    x = 1
except:
    print('Failed to set x')
else:
    print('No exception occured')
finally:
    print('We always do this')


# In[35]:


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')


# In[17]:


def divide(a, b):
    try:
        c = a/b
    except ZeroDivisionError as e:
        print(f'error occured as:{e}')
        c = a/4.
        print(c)
        return c
    else:
        print(c)
        return c
    finally:
        print('\033[92m function executed\033[00m')

result = divide(10., 0)
#result = divide(10, 5)


# In[19]:


def divide(x,y):
    
    try:
        value = 50
        x.append(value)
    
    except AttributeError as atr_err:
        print(atr_err)
        
    else:
        try:
            result = [i / y for i in x]
            print( result )
        except ZeroDivisionError:
            print("Please change 'y' argument to non-zero value")

    finally:
        print("\033[92m Code by DataCamp\033[00m")
        
        
x = [40,65,70,87]
divide(x,3)


# In[21]:


def file_editor(path,text):
    try:
        data = open(path)

        try:
            data.write(text)

        except:
            print("Unable to write the data. Please add an append: 'a' or write: 'w' parameter to the open() function.")

        finally:
            data.close()

    except:
        print(f"{path} file is not found!!")
        
        
path = "data_base.txt"
text = "DataCamp Workspace: Share your data analysis in a cloud-based environment--no installation required."

file_editor(path,text)


# # Raising custom exceptions
# 

# In[22]:


value = 2_000
if value > 1_000:   
    # raise the ValueError
    raise ValueError("Please add a value lower than 1,000")
else:
    print("Congratulations! You are the winner!!")


# In[23]:


value = 2_000
try:
    if value > 1_000:
          
        # raise the ValueError
        raise ValueError("Please add a value lower than 1,000")
    else:
        print("Congratulations! You are the winner!!")
              
# if false then raise the value error
except ValueError as e:
        print(e)


# In[16]:


class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Negative numbers are not allowed: {self.value}"

def process_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number * 2

try:
    result = process_positive_number(-5)
except NegativeNumberError as e:
    print(f"An error occurred: {e}")


# # Using Python’s logging module
# 

# In[1]:


import logging

# Configure the logging settings
logging.basicConfig(filename="file.log", level=logging.DEBUG, filemode='w', format="%(asctime)s - %(name)s -%(levelname)s - %(message)s"
                   , datefmt='%d-%b-%y %H:%M:%S')

# Log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


# In[2]:


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.exception("Attempted division by zero")
    else:
        return result

#divide(10, 2)
divide(10, 0)


# In[4]:


def divide(a, b):
    try:
        result = a / b
    except Exception as e:
          logging.error("Exception occurred", exc_info=True)
    else:
        return result

#divide(10, 2)
divide(10, 0)


# In[20]:


filename = "example.txt"

try:
    with open(filename, "r") as file:
        data = file.read()
except FileNotFoundError as e:
    print(f"File not found: {filename}")
    # Handle the missing file here
except PermissionError as e:
    print(f"Permission denied for file: {filename}")
    # Handle the permission error here
except IOError as e:
    print(f"An I/O error occurred while reading {filename}: {e}")
    # Handle the I/O error here
else:
    # Process the file data
    print(data)


# ## Logging Examples

# In[ ]:




