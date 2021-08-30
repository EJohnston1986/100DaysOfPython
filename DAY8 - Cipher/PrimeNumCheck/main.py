# prime number checker
def prime_num_chk(number):
    i = number - 1
    if number % 1 == 0:
        while i > 0:
            if number % i == 0:
                print(f"The number {number} is not prime")
            i -= 1


numberChk = int((input("Enter a whole number and find out if it is prime")))
prime_num_chk(numberChk)
