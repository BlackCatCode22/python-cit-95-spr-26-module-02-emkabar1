# Payroll Program with Exception Handling (Worked Exercise 3.2)

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except ValueError:
    print("Error, please enter numeric input")
    quit()

if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr

print("Pay: ", xp)
