#Foster Higginbotham's File.
#This project will demonstrate the abilitiy to use functions to calculate the gross earnings for an employee over several weeks.

#main
def main():

#need user input. some numbers will be floats while our week count will be an int for loop running purposes
    
    hourlyRate = float ( input("How much (in dollars) are you paid per hour?\n"))
    regWorkWeek = float ( input("How many hours should you work per week?\n"))
    overtimeRate = float ( input("What is the overtime rate for your job?\n"))
    numWeeksWorked = int ( input("How many weeks do you plan to be working?\n"))
    sumTotalPay = 0 

#loop for when it is more than 1 week
    
    for i in range (numWeeksWorked):

        hoursWorked = float ( input("How many hours did you work the next following week?\n"))
        overtime = overtimePay(hourlyRate, regWorkWeek, hoursWorked, overtimeRate)
        regular = regularPay(hourlyRate, regWorkWeek, hoursWorked)
        totalpay = overtime + regular
        sumTotalPay = totalpay + sumTotalPay
        
#print our outputs
        
        print ("Week", i+1, "regular pay =", regular,", overtime pay =", overtime, "total pay =", totalpay)
        print("Total Pay for", i+1, "weeks:", sumTotalPay)

#2 prior def's for both regular and overtime pay 
            
def overtimePay (payPerHour, regWorkWeek, hoursWorked, overtimePay):
    if (hoursWorked >= regWorkWeek):
        return (hoursWorked - regWorkWeek) * payPerHour * overtimePay
    else:
        return 0

def regularPay (payPerHour, regWorkWeek, hoursWorked):
    if (hoursWorked <= regWorkWeek):
        return payPerHour * hoursWorked
    else:
        return payPerHour * regWorkWeek

#close our main
main()


