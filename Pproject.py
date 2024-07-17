RyanGosling={
            0:{
            "ID":1,
            "name":"Max verstappen",
            "location":"beirut","destination":"jounieh",},
            1:{
            "ID":2,
            "name":"Lewis Hamilton",
            "location":"sidon","destination":"tyre",},
            2:{
            "ID":3,
            "name":"Daniel Ricciardo",
            "location":"tripoli","destination":"hermel",
              },
            }
cities1=[]
cities2=[]
for i in range(len(RyanGosling)):
      cities1.append(RyanGosling[i]["location"])
      cities2.append(RyanGosling[i]["destination"])
start={1:{"x":33.8,"y":35.4},
         2:{"x":33.5,"y":35.3},
         3:{"x":33.9,"y":36.8},
         }
end={0:{"x":33.9,"y":35.6},
       1:{"x":33.2,"y":35.2},
       2:{"x":34.3,"y":36.2},
       }
def main_menu():
  FaileSafe=True  
  while FaileSafe:
      print("------main menu------")
      user_info = input("Enter your choice: ")
      if user_info=="1":
        driver_menu()
      elif user_info=="2":
        city_menu()
      elif user_info =="3":
         print("Goodbye")
         return False
      else:
          print("Invalid input, please try again.")
          print("1.To go to the driver's menu.")
          print("2.to go to the citie's menu.")
          print("3.to exit ")

def city_menu():
    FaileSafe=True  
    print("Welcome to the city's menu enter the following: ")
    print("1.To go to view all the  cities.")
    print("2.to add a city.")
    print("3.to check which driver can get to a city.")
    print("4.to go back to main menu.")
    while FaileSafe:
      print("------City menu------")
      user_info = input("Enter your choice: ")
      if user_info=="1":
       show_city()
      elif user_info=="2":
        add_city()
      elif user_info =="3":
         print()
      elif user_info =="4":
          return False
      else:
          print("Invalid input, please try again.")
          print("1.To go to view all the  cities.")
          print("2.to add a city.")
          print("3.to go back to the main menu.")
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
  global RyanGosling
  for i in range(len(RyanGosling)):
      print(RyanGosling[i])
  return RyanGosling
def add_driver():
    global RyanGosling,cities1,cities2
    faileSafe = True
    while faileSafe:
            user_1 = input("Do you wish to add a driver y/n: ")
            if user_1.lower() == "y":
             
              new_driver_info_2 = input("Enter the driver name: ")
              new_driver_info_3 = input("Enter the driver location: ")
              new_driver_info_4 = input("Enter the driver destination: ")
              new_driver= {
                    "ID": len(RyanGosling)+1,
                    "name": new_driver_info_2,
                    "location": new_driver_info_3,
                    "destination":new_driver_info_4,
              }
              RyanGosling[len(RyanGosling)] = new_driver
              print(RyanGosling)
              cities1.append(new_driver_info_3) 
              cities2.append(new_driver_info_4)
              check_diliver()
            elif user_1.lower() == "n":
                faileSafe = False
            else:
                print("Invalid input, please try again.")
                print("y/n")
def show_city():
   global cities1, cities2
   print("All cities are:  ",cities1, cities2)
   return cities1, cities2

def add_city():
   global cities2, cities1
   failSafe = True
   while failSafe:
    user1=input("Do you wish to add a city y/n")
    if user1.lower() == "y":
        new_city=input("Enter the city name: ")
        if new_city == cities1 or new_city == cities2 :
            print("City already exists")
            add_city()
        cities1.append(new_city)
        check_diliver()
    elif user1.lower() == "n":
        failSafe = False
        print("Returning to the main menu")
        main_menu()
        return False 
    else:
        print("Invalid input, please try again.")
        print("y/n")
def check_diliver():
  global start,end
  max_x=36
  max_y=36
  min_x=33.1
  min_y=33.1
  print("add the location of the starting location ")
  stx=float(input("Enter the altitude of the city (max is 36 min is 33.1)"))
  sty=float(input("Enter the latitude of the city (max is 36 min is 33.1)"))
  print("add the location of the ending location")
  stx1=float(input("Enter the altitude of the destination of the city (max is 36.6 min is 33.1)"))
  sty1=float(input("Enter the latitude of the destination city (max is 36 min is 33.1)"))
  sum1=stx-stx1
  sum2= sty-sty
  if sum1 <= 0.3 or sum2<=0.3:
    if stx > max_x or sty < min_x or sty > max_y or sty<min_y:
      print("Invalid altitude, please enter the altitude within the range (max is 34.6)")
      check_diliver()
    else:
      for i in start:
        if stx == start[i]["x"] or sty == start[i]["y"]:
            print("this location alreadt exists")
            check_diliver()
      newcity={"x":stx,"y":sty}
      start[len(start)]=newcity
      if stx1 > max_x or stx1 < min_x or sty1 > max_y or sty1 < min_y:
        print("Invalid altitude, please enter the altitude within the range (max is 34.6)")
        check_diliver()
      else:
        for i in end:
          if stx1 == end[i]["x"] or sty1 == end[i]["y"]:
              print("this location alreadt exists")
              check_diliver()
        newcity1={"x":stx1,"y":sty1}
        end[len(end)]=newcity1
      print("The new cities and their coordinates are: ")
      show_city()
  elif sum1< 0.3 or sum2<0.3:
     print("its to far away to diliver it can't reach")
     check_diliver()
  else:
     print("Error accured going to main menu")
     main_menu()
# def driver_to_location():
#     global start, end
#     print("add the location of the starting location ")
#     stx=int(input("Enter the altitude of the city (max is 34.6 min is 33.1)"))
#     sty=int(input("Enter the latitude of the city (max is 36 min is 35.1)"))
#     print("add the location of the ending location")
#     for i in range(len(start)):
#       if stx in start[i]["x"] and sty in start[i]["y"]:
#         print(f"The driver with ID {i+1} can get to the city from {start[i]['x']},{start[i]["y"]}")
# failsafe = True
# while failsafe:
#     print("Hello please enter the following: ")
#     print("1.To go to the driver's menu.")
#     print("2.to go to the citie's menu.")
#     print("3.to exit ")
#     failsafe = main_menu()
  # for i in range(1,4):
  #   if start[i]["x"]<=max_x and start[i]["x"]>=min_x and start[i]["y"]<=max_y and start[i]["y"]>=min_y and end[i]["x"]<=max_x and end[i]["x"]>=min_x and end[i]["y"]<=max_y and end[i]["y"]>=min_y:
  #     print(f"The driver with ID {i} can get to the city from {start[i]['x']},{start[i]['y']} to {end[i]['x']},{end[i]['y']}")
  #   else:
  #     print(f"The driver with ID {i} can not get to the city from {start[i]['x']},{start[i]['y']} to {end[i]['x']},{end[i]['y']}")
main_menu()