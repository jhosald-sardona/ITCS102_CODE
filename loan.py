#string formating

loan_amt = float(input("Enter the loan amount --->"))
years = int(input("Enter the number of years --->"))

month = years * 12
principal = loan_amt / month
reamining_balance = loan_amt

#for loop
print("|MONTH\t|\tPAYMENT\t\t|INTEREST\t|\tPRINCIPAL\t|\tBALANCE|\t|")
for count in range(1, month + 1):
    rem_bal = principal
    interest = rem_bal * 0.00256
    pay = interest + principal
    #print(count, principal) or 
    #print(count,roun(pay,2), round(interest, 2 ), round(principal,2), rounde(rem_bal,2))
    print(f"|{count}\t|\t {round(pay,2)}\t\t|\t {round(interest, 2 )}\t\t\t|\t {round(principal,2)}\t\t\t|\t {round(rem_bal,2)}\t|")

    print("total")