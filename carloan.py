print("Welcome to the RBA Car Loan Calculator.\n\n")

while True:

    totalAmount = input("Please enter the total amount.")
    try:
        totalAmount = int(totalAmount)
        break
    
    except ValueError:
        print("Please enter a number.")

# Part2 : Store the downPayment

while True:

    downPayment = input("Please enter the down payment.")
    try:
        downPayment = int(downPayment)
        break
    
    except ValueError:
        print("Please enter a number.")
    


# Part3 : Store the interestRate

while True:

    interestRate = input("Please enter the interest rate.")
    try:
        interestRate = float(interestRate)
        break
    
    except ValueError:
        print("Please enter a number.")
      
    
# Part4 : Store the loanPeriod

while True:

    loanPeriod = input("Please enter the loan period.")
    try:
        loanPeriod = float(loanPeriod)
        break
    
    except ValueError:
        print("Please enter a number.")
        
