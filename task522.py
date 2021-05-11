#!/usr/bin/env python3

var1 = input('Vvedite IP dlya analiza:')
var2 = var1.split('/')
var3 = var2[0].split('.')
var4 = "1" * int(var2[1]) + "0" * (32 - int(var2[1]))
var5 = '{:08b}'.format(int(var3[0])), '{:08b}'.format(int(var3[1])), '{:08b}'.format(int(var3[2])), '{:08b}'.format(int(var3[3]))
var6 = ''.join(var5)
var8 = var6[0:int(var2[1])] + "0" * (32 - int(var2[1]))
var9 = '{}.{}.{}.{}'.format(int(var8[0:8], 2), int(var8[8:16], 2), int(var8[16:24], 2), int(var8[24:32], 2))
var10 = var9.split('.')

print('\n' + 'Subnet:')
#print(f"{var6[0:var7]}")
print(f"{var10[0]:<10}", f"{var10[1]:<10}", f"{var10[2]:<10}", f"{var10[3]:<10}")
print(f"{var8[0:8]:<10}", f"{var8[8:16]:<10}", f"{var8[16:24]:<10}", f"{var8[24:32]:<10}", '\n')
print('Mask:')
print('/' + var2[1])
print(f"{int(var4[0:8], 2):<10}", f"{int(var4[8:16], 2):<10}", f"{int(var4[16:24], 2):<10}", f"{int(var4[24:32], 2):<10}")
print(f"{var4[0:8]:<10}", f"{var4[8:16]:<10}", f"{var4[16:24]:<10}", f"{var4[24:32]:<10}")

