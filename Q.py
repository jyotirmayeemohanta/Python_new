que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of www."]
opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
ans_list=[3,1,2,2]
sol_list=[1,1,2,2]  
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==ans_list[index]:
        return True
    else:
        return False
def que():
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        result=option(index)
        # if result == "no":
        #     index-=1
        if result==True:
            print("Congractualtion")
        else:
            print("you Losse !")
            break 
        index+=1
# question_list = ["1.How many continents are there?", "2.What is the capital of India?",	"3.NG mei kaun se course padhaya jaata hai?"]
# options_list = [["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
# solution_list = [3, 4, 1]
# lifeline = 0
# for i in range(len(question_list)):
# 	print(question_list[i]),len(question_list[i])
# 	print(1,options_list[i][0])
# 	print(2,options_list[i][1])
# 	print(3,options_list[i][2])
# 	print(4,options_list[i][3])
# 	user = int(input("Enter the correct option  "))
# 	if user == solution_list[i]:
# 		print("congrats! Aapka answer sahi hai")
# 		print()
# 	elif user == 5050:
# 		if lifeline == 0:
# 			lifeline+=1
# 			a = solution_list[i]-1
# 			print(question_list[i])
# 			print(1,options_list[i][a])
# 			print(2,options_list[i][i])
# 			user_input = int(input("Enter the correct option  "))
# 			if user_input == 1:
# 				print("Congratulation Aapka answer sahi hai")
# 				print()

# 		else:
# 			print("Aap lifelife use kr chuke hai")
# 			print()
# 	else:
# 		print("sadly! Aapka jawab galat hai")


que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of www."]
opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
ans_list=[3,1,2,2]
sol_list=[1,1,2,2]  
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==ans_list[index]:
        return True
    else:
        return False
def que():
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        result=option(index)
        # if result == "no":
        #     index-=1
        if result==True:
            print("Congractualtion")
        else:
            print("you Losse !")
            break 
        index+=1
que()
