# Creating dictionary

student = {
    "name": "Praneetha",
    "age": 20,
    "course": "CSE"
}

# Access values
print("Name:", student["name"])

# Add new key-value pair
student["college"] = "VTU"

print("Updated Dictionary:")
print(student)

# Check key exists
if "age" in student:
    print("Age key exists")

# Remove key
del student["course"]

print("After Deletion:")
print(student)