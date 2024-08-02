"""A company decided to give bonuses to employee according to following criteria
 #Time period of service
 more than"""
salary = int(input("Salary: "))
years = int(input("Years of service: "))
if years >= 10:
    bonus = salary * 10/100
    print(bonus)
elif years >= 6 <= 10:
    bonus2 =  salary * 8/100
    print(bonus2)
else:
    bonus3 = salary * 5/100
    print(bonus3)

