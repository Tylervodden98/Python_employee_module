import csv
import datetime as dt
import os
import employee_functions as emp

# Ask user for how many employees they want
number_employee = emp.num_employee()

# Use List comprehension to make a list of employee dictionaries
employee_comp = [emp.employee() for num_person in range(0, number_employee)]
