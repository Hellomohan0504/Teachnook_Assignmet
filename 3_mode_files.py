# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r0NmUc8Cf3JaHhbEvGc_slCOHJauJLI_

**3 Different modes in Python**

**Read Mode**
"""

with open("content.txt",'r') as file:
  print(file.read())

"""**Write Mode**"""

with open("content.txt",'w') as file:
  file.write("Welcome \n")

"""**Append Mode**"""

with open("content.txt",'a') as file:
  file.write("To my page \n")

"""**r+**"""

with open("content.txt",'r+') as file:
  file.write("Python")

"""**w+**"""

with open("content.txt",'w+') as file:
  file.write("Python 3")

"""**a+**"""

with open("content.txt",'a+') as file:
  file.write("scripting")