#!/usr/bin/env python3

var1 = input('Vvedite set\' dlya analiza:')
var2 = var1.split('/')
var3 = var2[0].split('.')
var4 = str("1" * int(var2[1]) + "0" * (32 - int(var2[1])))

print('\n' + 'Network:')
print(f"{var3[0]:<10}", f"{var3[1]:<10}", f"{var3[2]:<10}", f"{var3[3]:<10}")
print(f"{bin(int(var3[0])):<10}", f"{bin(int(var3[1])):<10}", f"{bin(int(var3[2])):<10}", f"{bin(int(var3[3])):<10}", '\n')
print('Mask:')
print('/' + var2[1])
print(f"{int((var4[0:8]), 2):<10}", f"{int((var4[8:16]), 2):<10}", f"{int((var4[16:24]), 2):<10}", f"{int((var4[24:32]), 2):<10}")
print(f"{var4[0:8]:<10}", f"{var4[8:16]:<10}", f"{var4[16:24]:<10}", f"{var4[24:32]:<10}" + '\n')


