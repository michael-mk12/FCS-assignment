
def main_menu():
  FaileSafe=True  
  while FaileSafe:
      print("------main menu------")
      user_info = input("Enter your choice: ")
      if user_info=="1":
        driver_menu()
      elif user_info=="2":
        print(2)
      elif user_info =="3":
         print("Goodbye")
         return False
      else:
          print("Invalid input, please try again.")
          print("1.To go to the driver's menu.")
          print("2.to go to the citie's menu.")
          print("3.to exit ")

def driver_menu():
  FaileSafe=True  
  print("Welcome to the drivers menu enter the following: ")
  print("1.To go to view all the  driver's.")
  print("2.to add a driver.")
  print("3.to go back to the main menu.")
  while FaileSafe:
      print("------Driver menu------")
      user_info = input("Enter your choice: ")
      if user_info=="1":
        view_driver()
      elif user_info=="2":
        add_driver()
      elif user_info =="3":
         return False
      else:
          print("Invalid input, please try again.")
          print("1.To go to view all the  driver's.")
          print("2.to add a driver.")
          print("3.to go back to the main menu.")
def view_driver():
   RyanGosling={
                0:{
                "ID":1,
                "name":"Max verstappen",
                "location":"akkar","destination":"",},
                1:{
                "ID":2,
                "name":"Lewis Hamilton",
                "location":"Saida","destination":"",},
                2:{
                "ID":3,
                "name":"Daniel Ricciardo",
                "location":"Jbeil","destination":"",
                  },
                }
   for i in range(len(RyanGosling)):
      print(str(RyanGosling[i])[1:-1])
   return RyanGosling
def add_driver():
    faileSafe = True
    RyanGosling = view_driver()
    while faileSafe:
            user_1 = input("Do you wish to add a driver y/n: ")
            if user_1.lower() == "y":
                  new_driver_info_2 = input("Enter the driver name: ")
                  new_driver_info_3 = input("Enter the driver location: ")
                  new_driver = {
                        "ID": len(RyanGosling)+1,
                        "name": new_driver_info_2,
                        "location": new_driver_info_3
                    }
                  RyanGosling[len(RyanGosling)] = new_driver
                  print(RyanGosling)
            elif user_1.lower() == "n":
                faileSafe = False
                print("Returning to the main menu")
                return False
            else:
                print("Invalid input, please try again.")
                print("y/n")      
def show_cities():
   RyanGosling =view_driver()

   
running = True
while running:
    print("Hello please enter the following: ")
    print("1.To go to the driver's menu.")
    print("2.to go to the citie's menu.")
    print("3.to exit ")
    running = main_menu()

