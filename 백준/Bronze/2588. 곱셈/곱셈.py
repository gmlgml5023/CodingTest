num1 = input()
num2 = input()
num3 = int(num1)*int(num2[2])
num4 = int(num1)*int(num2[1])
num5 = int(num1)*int(num2[0])
num6 = int(str(num5)+'00') + int(str(num4)+'0') + num3
print(num3, num4, num5, num6, end='\n')