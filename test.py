inp = input()
i=0
c = ''
while inp[i]!=' ':
	c+=inp[i]
	i+=1
a = int(c)
b = int(inp[i::])
print(a+b)