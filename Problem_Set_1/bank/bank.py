greet = input("Greeting: ")
greet = greet.lower().strip()
if greet.startswith("hello"):
    money=0
elif greet.startswith("h"):
    money=20
else:
    money=100
print(f"${money}")
