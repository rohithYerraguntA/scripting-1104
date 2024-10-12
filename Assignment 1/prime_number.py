# function to check if a number is prime
def prime_number(i):
    if i < 2:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

# function to find a prime number prior to entered number    
def finding_previous_prime(i):
    for j in range(i-1, 1, -1):
        if prime_number(j):
            return j
    return None

# function to find a prime number next to the entered number
def finding_next_prime(i):
    j = i + 1
    while True:
        if prime_number(j):
            return j
        j += 1

# function that finds factors of entered number including number itself        
def all_factors(i):
    factors = []
    for j in range(1, i+1):
        if i % j == 0:
            factors.append(j)
    return factors

# this is the main function that handles user input
def main():
    
    # takes input until the input is a valid positive whole number
    while True:
        number = input("enter a positive whole number: ")
        if number.isdigit() and int(number) > 0:
            number = int(number)
            break
        else:
            print("Please enter a valid positive whole number")
            
    previous_prime = finding_previous_prime(number)
    if previous_prime:
        print(f"The prime before {number} is {previous_prime}")
    else:
        print(f"There is no prime number before {number}")
    
    if prime_number(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
        factors = all_factors(number)
        print(f"factors of {number} are: {factors}")
             
    next_prime = finding_next_prime(number)
    print(f"The next prime number after {number} is {next_prime}")
    
    
if __name__ == "__main__":
        main()
