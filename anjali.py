f=float(input("Enter the temperature in fahrenheit :"))
c=(f-32)*5/9
print("{} fahrenheit = {} Celsius ".format(f,c))
c=float(input("Enter the temperaturein celsius :"))
f=9*c/5+32
print("{1} celsius = {0} fahrenheit".format(f,c))
print(c,"celsius = ",f,"fahrenheit")