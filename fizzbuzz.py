
try:
    usr_input = input("Enter a number > ")
    for n in range(1,int(usr_input)):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
except:
    print("Please only enter an integer.")