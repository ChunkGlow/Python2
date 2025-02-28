medical_cause = input("Please enter your medical cause Y or N")

attendance = int(input("Enter your attendance"))

if medical_cause == 'Y':
	print("Yes youa re allowed")
else:
	if attendance > 75:
		print("Allowed")
	else:
		print("Not allowed")