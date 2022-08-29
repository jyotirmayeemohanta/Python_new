# a=3
# b=5
# c=a+b
# d=a-b
# e=a*b
# print(c)
# print(d)
# print(e)


# def is_leap(year):
#     if year%4==0:
#         print("year leap year")
#     elif year%100==0 or year%400==0:
#         print("year leap year")
#     else:
#         print("false")
    
# year = int(input("enter any year"))


def is_leap(year):
    leap=False
    if year%4==0:
        print("year leap year")
    elif year%100==0:
        print("NOT a leap year")
    elif year%400==0:
        print("leap year")
year=int(input("enter any year"))
print(is_leap(year))