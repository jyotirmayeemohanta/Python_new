# print("Enter the String:- ")
# str = input()

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# newstr = ""
# strlen = len(str)

# for i in range(strlen):
#     if str[i] not in vowels:
#         newstr = newstr + str[i]

# str = newstr
# print(str)


print("Enter the string")
str = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
i = 0
for c in str:
    if c in vowels:
        str = str[:i] + str[i+1:]
        i = i-1
    i = i+1
print(str)




