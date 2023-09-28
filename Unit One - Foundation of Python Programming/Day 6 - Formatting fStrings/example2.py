number = 42
print(f"{number:<5}")   
#output: 42___          # _ indicates space

number = 42
print(f"{number:>5}")  
#output: ___42

value = 3.1415
print(f"{value:^8}")
#output: _3.1415_

long_text = "This is a long string"
print(f"{long_text:.15}")
#output: This is a long_

name = "Alice"
age = 28
print(f"Name: {name:<10} Age: {age}")
#output: Name: _____Alice Age: 28