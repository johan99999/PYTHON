inputan = int(input("delivery : " ))
inputan2 = int(input("pick-up : "))
######################################
a = 1400

if inputan >= 2500 :
    a = 1500
elif inputan >= 3000 :
    a = 1750

#####################################
total = ((inputan + inputan2) * a)
format = f"Rp. {total:,}"
#####################################
print(format)
