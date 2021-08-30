# creating a dictionary
student = {}

# populating the dictionary with key value pairs
student = {"Name": "John",
           "Age": 25,
           "Courses": ["Maths", "Physics"]
           }

# printing data from dictionary
print(student)            # prints all key, value pairs
print(student["name"])    # prints only value of named key

# accessing key value pair using get method
print(student.get("name"))

# adding new key value pair to a  dictionary
student["phone"] = "01738 447385"

# searching a dictionary for a key named "phone", returns not found if no result
print(student.get("phone", "not found"))

# changing information in a dictionary
student["Name"] = "Jane"

# using update function to update more than one piece of information, dictionary as argument
student.update({"Name": "Steve", "Age": 27, "Courses": "Geology", "Phone": "2342145435"})

# deleting a dictionary key value pair
del student["age"]

# looping through keys and values of dictionary
print(len(student))      # displays number of keys
print(student.keys())    # displays all the keys
print(student.values())  # displays all the values
print(student.items())   # displays all key and value pairs

for key, value in student.items():  # prints all key value pairs from loop
    print(key, value)


