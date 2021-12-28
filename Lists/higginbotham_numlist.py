# Foster Higginbotham's File.
# In this assignment, I will demonstrate the ability to write and apply python code that will allow the user to add numbers to a list, 
# remove numbers from a list and print the numbers in a list.

# create an empty list
newList =[]

# while loop so that we can keep looping our program until user selects to quit
while(True):
    print("What selection would you like to make?")
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Print the list")
    print("4. Quit")
    selection = int(input())
    
    # if - else statements for different selections from the user (1-4)
    # choice 1, adding elements to our list 
    if selection == 1:
        number = int(input("What number do you want to add?\n"))
        #add to our list
        newList.append(number)
        print("Your number has been added.")
        
    # choice 2, removal of number from our list
    elif selection == 2:
        number = int(input("What number do you want to remove?\n"))
        try:
            # removal of our number with .remove
            newList.remove(number)
            print("Your number has been removed.") 
            # if number isnt on the list, print this message
        except ValueError:
            print("Sorry, that number is not on the list.")
            
    # choice 3, print our list         
    elif selection == 3:
        print("Your list is {}".format(newList))
        
    # choice 4, the condition in which our loop breaks
    else:
        print("Thank you for using the list generator!")
        break
            
 
