kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371


miles = kilometers * conv_fac

print('%0.1f kilometers is equal to %0.1f miles' %(kilometers,miles))