has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
     print("Eligible for loan")

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
     print("Eligible for loan")

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
     print("Eligible for loan")

has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
     print("Eligible for loan")

has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
     print("Eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
     print("Eligible for loan")



#AND Both the condition must be true
#OR : alteat one condition must be true
#NOT: