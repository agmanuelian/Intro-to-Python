def fizzbuzz_generator(var):
    for num  in range ( 1 , var+1):
        if num%3 == 0  and num%5 == 0 :  
	        print("Fizz Buzz")
        elif num % 3 == 0:  
	        print("Fizz")
        elif num % 5 == 0:  
	        print("Buzz")
        else:
            print(str(num))

fizzbuzz_generator(10)