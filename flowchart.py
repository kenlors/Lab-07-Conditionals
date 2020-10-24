move = input("Does it move? (yes/no) ")
if move == "yes":
  should = input("Should it? (yes/no) ")
  if should == "yes":
    print("No problem")
  elif should == "no":
    print("Then use duct tape!!!")
  else:
    print("Answer my question! You didn't type yes or no.")
elif move == "no":
  print("Then use duct tape!!!")
else:
  print("Answer my question! You didn't type yes or no.")
