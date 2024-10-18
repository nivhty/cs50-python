vowels = {'a', 'e', 'i', 'o', 'u'}
temp = []
string = str(input("Input: "))

for c in string:
    if c.lower() not in vowels:
        temp.append(c)
output = ''.join(temp)
print(f"Output: {output}")

