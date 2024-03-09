# accounts
# hiding 6 digits out of 10 showing 4


account_no = int(input("Please enter an 10 digit account number: "))
print(f"XXXXXX{account_no % 10000}")