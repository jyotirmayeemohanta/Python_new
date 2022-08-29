# a={"nidhi":[20,25,30],"abhisek":[45,100,80],"shanti":[40,60,90],"avinash":[30,50,70]}
# count=0
# for key in a:
#     count=count+1
# def sum_function(a):
#     b=[]
#     for i in a:
#         for j in range(len(a[i])):
#             if not b:
#                 b=[0]*len(a[i])
#             b[j]+=a[i][j]/count
#     print(b)
   
# sum_function({"nidhi":[20,25,30],"abhisek":[45,100,80],"shanti":[40,60,90],"avinash":[30,50,70]})

a={"nidhi":[20,40,30],"abhishek":[95,100,80],"jyoti":[80,70,90]}
def sum_sub(a,i):
	sum=0
	num=val[i]
	for value in a.values():
		if num>=value[i]:
			num=value[i]
	return num
for val in a.values():
	l=len(val)
	for index in range(l):
		print(sum_sub(a,index))
	break
sum_sub(i,{"nidhi":[20,40,30],"abhishek":[95,100,80],"jyoti":[80,70,90]})