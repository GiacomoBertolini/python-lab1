string = input("insert a string: ")
if len(string) > 2:
    new_string = string[:2] + string[-2:]
else:
    new_string = ""
print("the new string is: ", new_string)
