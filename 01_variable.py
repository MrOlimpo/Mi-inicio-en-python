# variable
my_string_variable = "my string variable"

print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenacion of variables in a print
print(my_string_variable,my_int_variable,my_bool_variable)
print("This is the value of:", my_bool_variable)

# some Functions of the sistem 
print(len(my_string_variable))

# variables in a only line
name, surname, nickname, age = "Alfredo", "Medina", "Pepe", 18
print("My firs name is:",name,". and my lastname is:",surname,". im",age,"old...", "And my nickname is:", nickname)

#opction inputs 
""""
name = input("What is your name: ")
age = input("How old are you: ")
print(name,age)
"""
# we changed its type
name = 25
age = "Jose"
print(name,age)

# We force the type?
address: str = "my address"
address = 32

print(address)