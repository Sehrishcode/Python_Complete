# secret_number = 9
# guess_count= 0
# guess_limit = 3
# while guess_count < guess_limit:
#    guess = int(input("Guess: "))
#    guess_count +=1
#    if guess == secret_number:
#     print("You win!")
#     break
# else:
#    print("Sorry! You failed.")
print("............. Car Game.............")
command = ""
started = True
while True:
  command = input(" > ").lower()
  if command == "start":
    if started == True:
      print("Car is already started.")
    else:
        started = True
        print("Car Started...")
    
  elif command == "stop":
    if not started:
      print("car is already stopped.")
    else:
      started = False
      print(" Car Stopped.")
  elif command == "help":
    print("""
Start - to start the car.
Stop - to stop the car.
quit - to quit.
    """)
  elif command == "quit":
    print(" Game End.")
  else:
    print("Sorry i don't understand that!")

    

    