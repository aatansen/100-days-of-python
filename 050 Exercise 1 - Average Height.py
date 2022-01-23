import math
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum=0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

#Write your code below this row 👇
    sum = sum+student_heights[n]
    average_height=sum/len(student_heights)
print(math.ceil(average_height))









#testing:
# x=[1,2,3,4]
# sum=0
# for y in x:
#     sum = sum+y
# print(sum)



