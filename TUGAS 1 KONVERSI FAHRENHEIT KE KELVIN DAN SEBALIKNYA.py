Fa = int(input("silahkan isi temperature fahrenheit : "))
Kb = int(input("silahkan isi temperature kelvin     : "))
Ka = int(((Fa - 32) * 5/9) + 273.15)
Fb = int(((Kb - 273.15) * 9/5) +32)
print (Fa,"Fahrenheit", "di konversi ke Satuan Kelvin adalah",Ka, "Kelvin")
print (Kb,"Kelvin", "di konversi ke Satuan Fahrenheit adalah",Fb, "Fahrenheit")