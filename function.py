ages = [10,20,30]
incomes = [100,200,300,400]

def calculate_average(list):
    sum = 0;
    for i in list:
        sum = sum + i;

    return sum/len(list)

print ("The average of your 'ages' list is: ",calculate_average(ages))
print ("The average of your 'incomes' list is: ",calculate_average(incomes))

