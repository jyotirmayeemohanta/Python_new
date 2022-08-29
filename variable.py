# name=input("What is your name ?")
# length=len(name)
# print(length)

# print(len("Jyoti"))

# print("hello"[3])

# print("123" + "789")

# list=[4,8,1,3,9]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]
#         j+=1
#     i+=1
# print(list)

# print(5*5)
# print(5**2)
# print(5**3)

# print(list("pqrs"))



# m=""
# a=int(input("enter "))
# t=a
# while a>0:
#     k=a%10
#     a//=10                                                          
#     m=m+str(k)
# if int(m)==t:
#     print("it is a polindram")
# else:
#     print("isnt polindram")


# n = int(input("Enter the number "))  
# for i in range(1,11):  
#     c = n*i  
#     print(n,"*",i,"=",c) 

# list = ['Jyoti','Alok','Trishakha','lisa']  
# for i in range(len(list)):  
#     print("Hello",list[i])  

print("Enter the String: ")
str = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newtext = ""
textlen = len(str)

for i in range(textlen):
    if str[i] not in vowels:
        newtext = newtext + str[i]

print("\nString after removing Vowels: ")
text = newtext
print(text)

# print("Enter the string")
# str = input()

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# i = 0
# for c in str:
#     if c in vowels:
#         str = str[:i] + str[i+1:]
#         i = i-1
#     i = i+1
# print(str)

