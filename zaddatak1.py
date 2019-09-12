 

firstNumber = int('10111110',2)
secondNumber = int('01101011',2)
rez = firstNumber&secondNumber
 
print((bin)(firstNumber)+" & "+(bin)(secondNumber)+ " = " +(bin)(rez))
print("\nDecimalno\n")
print((str)(firstNumber)+" & "+(str)(secondNumber)+ " = " +(str)(rez))


firstNumber = int('00100110',2)
secondNumber = int('10101001',2)
rez = firstNumber|secondNumber
 
print("\n"+(bin)(firstNumber)+" | "+(bin)(secondNumber)+ " = " +(bin)(rez))
print("\nDecimalno\n")
print((str)(firstNumber)+" | "+(str)(secondNumber)+ " = " +(str)(rez))


firstNumber = int('1000',2)
secondNumber = int('0101',2)
rez = firstNumber^secondNumber    
 
print("\n"+(bin)(firstNumber)+" ^ "+(bin)(secondNumber)+ " = " +(bin)(rez))
print("\nDecimalno\n")
print((str)(firstNumber)+" ^ "+(str)(secondNumber)+ " = " +(str)(rez))


firstNumber = int('11001011',2)
rez = ~firstNumber  
 
print("\n~"+(bin)(firstNumber) + " = " +(bin)(rez))
print("\nDecimalno\n")
print("~"+(str)(firstNumber) + " = " +(str)(rez))


firstNumber = int('10101000',2)
rez = firstNumber<<2  
 
print( "\n"+(bin)(firstNumber) +" <<2 = " +(bin)(rez))
print("\nDecimalno\n")
print( (str)(firstNumber) + " <<2 = " +(str)(rez))

firstNumber = int(' 01010010',2)
rez = firstNumber>>2  
 
print( "\n"+(bin)(firstNumber) +" >>2 = " +(bin)(rez))
print("\nDecimalno\n")
print( (str)(firstNumber) + " >>2 = " +(str)(rez))