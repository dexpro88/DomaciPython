osnovica = 40000

jan = 0.17
feb = 1.9
mar = 0.13
apr = 1.02
may = 0.78
jun = 0.67

january_to_june =  jan + feb + mar + apr + may + jun

print("Polugodisnji koeificijent iznosi: " +(str)(january_to_june))

july = 0.67
august = 0.35
sept = 1.18
oct = 0.20
nov = 0.66
dec = 1

total = january_to_june + july + august + sept + oct + nov + dec

bonus = total * osnovica/10

print("bonus = "+(str)(bonus))
