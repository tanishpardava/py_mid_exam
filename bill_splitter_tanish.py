print("======================================================================================")


print("Welcome to the Bill Splitter App!")


print("======================================================================================")


#User Inputs 

total_bill_am = float(input("Enter Total Bill amount: "))

number_of_people = int(input("Enter number of people: "))

tip_percentage = int(input("Enter tip percentage (0/5/10/15/20):"))



#Validation using control structure


if number_of_people <= 0:
    print("This is Not valid, Enter Again No. of people.")

if total_bill_am or tip_percentage < 0:
    print("Negative value not valid.")


#Calculations


tip_amount = (tip_percentage / 100 ) * total_bill_am

final_bill = total_bill_am + tip_amount

per_person = final_bill / no_people

#Display all value properly

print(f"Tip Amount: Rs.{tip_amount}")
print(f"Total Bill (with Tip): {final_bill} ")
print(f"Each person should pay: Rs.{per_person}")


#Using while loop to continue or exit based on user input (y/n)
print()

yes_no = input("Would you like to calculate another bill? (y/n): ")

while yes_no == "y":

   
   #User Inputs for value
   
    total_bill_am = float(input("Enter Total Bill amount: "))
   
    number_of_people = int(input("Enter number of people: "))
   
    tip_percentage = int(input("Enter tip percentage (0/5/10/15/20):"))


   
   
   
   #Validation control structure
   
   
    if number_of_people <= 0:
       print("This is Not valid, Enter Again No. of people.")
   
    if total_bill_am or tip_percentage < 0:
       print("Negative value not valid.")
   
   
   #Calculations
   
   
    tip_amount = (tip_percentage / 100 ) * total_bill_am
   
    final_bill = total_bill_am + tip_amount
   
    per_person = final_bill / number_of_people
   
   #Display all value properly
   
    print(f"\nTip Amount: Rs.{tip_amount}\n")
  
    print(f"\nTotal Bill (with Tip): {final_bill} \n")
  
    print(f"\nEach person should pay: Rs.{per_person}\n")

   
   
   #Using while loop to continue or exit based on user input (y/n)
   
    yes_no = input("Would you like to calculate another bill? (y/n): ")