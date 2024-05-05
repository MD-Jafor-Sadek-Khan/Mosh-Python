"""logical_operators """

high_income: bool = True
good_credit: bool = False
student: bool = False

if (high_income or good_credit) and not student:
    print("Eligeble")
else:
    print("Not Eligeble")
