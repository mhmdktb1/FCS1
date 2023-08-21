from datetime import datetime
emp_list=[]

def Admin_Menu():
  while True :
    print("1. Display statics")
    print("2. Add an Employee")
    print("3. Display all Employees")
    print("4. Change Employees Salary")
    print("5. Remove Employee")
    print("6. Raise Employees Salary")
    print("7. Exit")
    print("")
    option = int(input("choose number please  "))
    if option > 7 or option <1 :
      print("enter number from 1 to 7")
    elif option ==1:
      D_Satatics()
    elif option ==2 :
      A_Employe()
    elif option == 3 :
      D_Employee()
    elif option == 4:
      S_Change()
    elif option == 5:
      E_Remove()
    elif option ==6:
      S_Raise()
    else :
      F_saving()
      break
def User_Menu():

  while True :
    print("1. Check my salary") 
    print("")
    print("2. Exit")
    option = int(input("choose number please  "))
    if option > 2 or option <1 :
      print("enter 1 or 2")
    elif option == 1:
      print(" i didnot get it:(")
     
    else : 
      print("exiting")
      break
def Login_Form():
  maxI = 0 
  print("Hello Wellcome to FCS Midterm")
  while  maxI < 5 :
    U_admin=input("Username :   ")
    P_admin=input("Password :   ")
    if U_admin =="admin" and P_admin == "admin123123" :
       Admin_Menu()
       break
    elif U_admin in emp_list and P_admin== "":
      User_Menu()
      break
    else :
      print("incorrect username or password")
      maxI += 1 
  if maxI  >= 4 :
   print("You've reached the maximum number of attempts.") 
def D_Satatics():
  counf=0
  counm=0 
  for line in emp_list :
    
    if line[3] == "female":
     counf+=1

    else : counm+=1
  print(counm,counf)           
def A_Employe():
  new_id=input("enter the id please :  ")  
  new_name=input("enter the name please :  ")  
  time=datetime.now().strftime("%Y-%m-%d")#zero.web,school
  gender=input("the gender :  ") 
  salary=input("enter "+ new_name +"`s salary" ) 
  new=[new_id, new_name, time, gender, salary]
  emp_list.append(new)
  with open("employe.txt.txt", 'a') as f:
    content = ",".join(new)  #youtube:)
    f.write(content + "\n")
def F_reading():# used youtube to learn it
  with open("employe.txt.txt","r") as file :
   for line in file :
        line_strip=line.strip()
        line_split=line_strip.split()
        emp_list.append(line_split)
def F_saving():# i used internet to learn it
   with open("employe.txt.txt","w") as file :
    for E in emp_list:
      content=",".join(E)
      file.write(content + "\n")
def D_Employee():
  emp_list.reverse()
  for employee in emp_list:
    print(employee) 
def S_Change():
  id=input("enter the id :    ")
  salary=input("enter the new salray :   ")
  for i in emp_list :
    if i[0] == id:
      i[-1] = salary 
      print("salary updated") 
      
      break
    else :
      print("not found") 
def E_Remove():
  id=input("Enter the id :   ")
  for i in emp_list:
    if i[0]==id :
      emp_list.remove(i)
def S_Raise():
  id=input("enter the id :    ")
  Percentage = float(input("Enter the raise percentage: "))
  for i in emp_list :
     if i[0]==id:
        salary= float(i[-1])
        new_salary =salary*Percentage
        i[-1]= str(new_salary)
        print("salary raised") 
        saving()
        break
     else :
        print("not found")         
F_reading()
Login_Form()
