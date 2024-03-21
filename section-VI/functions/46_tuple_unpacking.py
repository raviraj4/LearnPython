workhours = [("Abby",100),("Billy", 4000), ("Cassie",8200)]
# define a function to determine employee of the month!
#  WE WANT TO RETURN NAME AND HOURSWORKED OF THE EMPLOYEE!
# =>

def employee_check(workhours):
    current_max = 0 
    star_employee = ""
    
    for employee,hours in workhours:
        if hours > current_max:
            current_max = hours
            star_employee = employee
        else:
            pass
        
    # print(star_employee, current_max)
    # IF WE PRINT WE GET => Cassie 8200    
    return (star_employee, current_max)

result = employee_check(workhours)

print(result)
# >>> ('Cassie', 8200)

#   TA DA! WE PERFORMED TUPLE UNPACKING WITH FUNCTION CALLS