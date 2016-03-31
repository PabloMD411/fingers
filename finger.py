import sys
i=2
a=int(sys.argv[1])
while a%i:i+=1
print 1 if a==i else 0
