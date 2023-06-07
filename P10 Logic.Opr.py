has_good_income = False
has_good_credit = False

if has_good_income and has_good_credit:
    print("Eligible for loan")
elif has_good_income or has_good_credit:
    print("Eligible for loan but for six months only.")
else:
    print("Not eligible for loan")
has_good_income = False
has_criminal_record = False
print(".............Another Example...............")
if has_good_income and not has_criminal_record:
    print("Eligible for loan")
elif has_good_income or not has_criminal_record:
    print("Eligible for loan but for six months only.")
else:
    print("Not eligible for loan")
    


