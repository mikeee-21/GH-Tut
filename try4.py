# This code is from branch 1.
for i in range(5):
    print(f"{i+1}.) From Branch 1.")
    
print("No error!")

# from branch 2
for i in range(5):
    print(f"{i+1}.) From Branch 2.")

print("No error! from b2.")
print("From main, now merger conflict solve!")

print("From Branch 1")
print("From Branch 1")

print("From Branch 2")
print("From Branch 2")