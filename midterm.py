def Admin_Menu():
  print("1. Display statics")
  print("2. Add an Employee")
  print("3. Display all Employees")
  print("4. Change Employees Salary")
  print("5. Remove Employee")
  print("6. Raise Employees Salary")
  print("7. Exit")  
def User_Menu():
  print("1. Check my salary") 
  print("2. Exit")
def D_Satatics():
  counf=0
  counm=0 
  for line in emp_list :
    
    if line[3] == "female":
     counf+=1

    else : counm+=1
  print(counm,counf)           
def Add_Employe():
  new_id=input("enter the id please :  ")  
  new_name=input("enter the id please :  ")  
  time=input("enter the time please :  ") 
  gender=input("the gender :  ") 
  salary=input("enter "+ new_name +"`s salary" ) 
  new=[new_id, new_name, time, gender, salary]
  with open("employe.txt.txt", 'a') as f:
    content = ",".join(new)  #youtube:)
    f.write(content + "\n")
def Login_Form():
  maxI = 0 
  print("Hello Wellcome to FCS Midterm")
  while  maxI < 5 :
    U_admin=input("Username :   ")
    P_admin=input("Password :  ")
    if U_admin =="admin" and P_admin == "admin123123" :
       Admin_Menu() 
    elif U_admin in emp_list and P_admin== "":
      User_Menu()
    else :
      print("incorrect username or password")
      maxI += 1 
  if maxI  >= 4 :
   print("You've reached the maximum number of attempts.") 

