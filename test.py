# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enter Number 2:"))
# print("Addition of given numbers is: ",num1+num2)





# name = input("Enter Name: ")
# age = int(input("Enter Age: "))

# if (age > 17):
#     print('You are Eligibe')
# else:
#     print('You are not Eligibe')


# operator = input('Select Operator(+,-,*,/):')
# num1 = int(input('Enter Number:'))
# num2 = int(input('Enter Number:'))

# if operator == '+':
#     print("Addition is: ",num1+num2)
# if operator == '-':
#     print("Subtraction is: ",num1-num2)
# if operator == '*':
#     print("Multiplication is: ",num1*num2)
# if operator == '%': 
#     print("Multiplication is: ",num1*num2)
# else:
#     print("Wrong Input")


# list = ['Muzammil','Mudassir','Saad','Hassan']
# list.append('Haris')
# list.remove('Saad')
# # print(list)
# newlist = []
# for x in list:
#     if 's' in x:
#       newlist.append(x)

# print(newlist)  

# for x in list:
#     print(x)

# for i in range(0,len(list)):
#     print(list[i])

# i = 0;

# while i < len(list):
#     print(list[i])
#     i += 1

# num_list = [10,9,8,7,6,5,4,3,2,1,0]
# num_list.sort()
# num_list2=[]
# num_list2.copy()

# english = int(input("Enter English Marks:"))
# math = int(input("Enter Math Marks:"))
# urdu = int(input("Enter Urdu Marks:"))
# comp = int(input("Enter Computer Marks:"))
# isl = int(input("Enter Islamiyat Marks:"))

# total = english+math+urdu+comp+isl;

# print("Total Marks is:",total*100/500)

# 40




# Python3 Program for DFA that accepts string
# if it starts and ends with same character

# Function for the state Q1
def q1(s, i):

  # Condition to check end of string
  if (i == len(s)):
    print("Yes");
    return;
  
  # State transitions
  # 'a' takes to q1, and
  # 'b' takes to q2
  if (s[i] == 'a'):
    q1(s, i + 1);
  else:
    q2(s, i + 1);

# Function for the state Q2
def q2(s, i):
  
  # Condition to check end of string
  if (i == len(s)):
    print("No");
    return;
  
  # State transitions
  # 'a' takes to q1, and
  # 'b' takes to q2
  if (s[i] == 'a'):
    q1(s, i + 1);
  else:
    q2(s, i + 1);

# Function for the state Q3
def q3(s, i):
  
  # Condition to check end of string
  if (i == len(s)):
    print("Yes");
    return;
  
  # State transitions
  # 'a' takes to q4, and
  # 'b' takes to q3
  if (s[i] == 'a'):
    q4(s, i + 1);
  else:
    q3(s, i + 1);

# Function for the state Q4
def q4(s, i):
  
  # Condition to check end of string
  if (i == s.length()):
    print("No");
    return;
  
  # State transitions
  # 'a' takes to q4, and
  # 'b' takes to q3
  if (s[i] == 'a'):
    q4(s, i + 1);
  else:
    q3(s, i + 1);

# Function for the state Q0
def q0(s, i):

  # Condition to check end of string
  if (i == len(s)):
    print("No");
    return;
  
  # State transitions
  # 'a' takes to q1, and
  # 'b' takes to q3
  if (s[i] == 'a'):
    q1(s, i + 1);
  else:
    q3(s, i + 1);

# Driver Code
if __name__ == '__main__':
  s = "abbaabb";

  # Since q0 is the starting state
  # Send the string to q0
  q0(s, 0);
  
# This code is contributed by Rajput-Ji
