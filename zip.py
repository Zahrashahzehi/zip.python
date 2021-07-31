# zip 
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7,8]
print(list(zip(numbers_1 , numbers_2)))
print("=========================================")
print(dict(zip(numbers_1 , numbers_2)))
print("=================================================")
my_list = [(1,5) , (2,6) , (3,7) , (4,8)]
print(list(zip(*my_list)))
print("======================================")
students = ["zahra ", "sara ", "mina"]
midterm = [80,67,89]
final = [34 , 87 , 97]
final_gread = zip(students , map(lambda pair : max(pair) , zip(midterm , final)))
print(dict(final_gread))