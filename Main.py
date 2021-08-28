# by Kalashnikov.Vincent
# Algorithm test
from package_method import *
from package_excel_data import *

# Add obj
method = method_lib()
exexcel = excel_exchange()

# Keyboard input
arr = input("input")#input the age
age = [int(n) for n in arr.split()]#use space to seperate each nums
are = input("input")#input the math's grade
math = [int(a)for a in are.split()]#use space to seperate each nums

for i in range(len(age)):
    method.add_new_e(age[i],math[i])

method.times_age()

print("request_unique_age_list() test:" , method.request_unique_age_list())
print("request_score_age_list() test:" , method.request_score_age_list())
print("request_times_age_list() test: " , method.request_times_age_list())

method.bubbles_sort_age()

exexcel.show_table(method.request_bubbles_unique_age_list(), 
            method.request_score_age_list(), 
            method.request_bubbles_times_age_list())