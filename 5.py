#Write a program to check if a number is prime or not
number=int(input("Enter a number: "))
is_prime=True
if(number>1):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            is_prime=False
            break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number.")