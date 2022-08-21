salary = float(input('Please enter your Salary in Figures : '))
tp = int(input('Enter your period of service in Figures : '))

if tp > 10 :
    new_sal = salary + ((10/100)*salary)
    print(new_sal)

elif tp >=6 and tp <= 10 :
    new_sal = salary + ((8/100)*salary)
    print(new_sal)

elif tp < 6 :
    new_sal = salary + ((5/100)*salary)
    print(new_sal)

else : 
    print('Invalid')