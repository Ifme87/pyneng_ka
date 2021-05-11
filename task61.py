#!/usr/bin/env python3

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

var1 = str(mac[0]).replace(':', '.')
var2 = str(mac[1]).replace(':', '.')
var3 = str(mac[2]).replace(':', '.')
var4 = str(mac[3]).replace(':', '.')
result = [var1, var2, var3, var4]

print(result)
