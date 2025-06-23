hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("per hour:"))
if h<=40:
    regular = float(h * rate)
    print(regular)
else:
    regular = 40 * rate
    overtime = float(h-40) * 1.5 * rate
    total = regular + overtime 
    print(total)

    #(45-40)*1.5*10.5+40*10.5
    #40*10.5=420
    #(45-40)*rate per hour*1.5+40*rate per hour