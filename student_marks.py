# Dictionary containing student names as keys and their marks as values
students = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 67,
    "David": 49,
    "Eva": 91,
    "Frank": 50,
    "Grace": 38
}

print("Students with marks >= 50:\n")
for name, marks in students.items():
    if marks >= 50:
        print(f"Name: {name}, Marks: {marks}")
