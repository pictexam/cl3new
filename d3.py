import hashlib
import random
def check_prime(a):
	if(a<2):
		return False
	elif(a==2):
		return True
	else:
		count = 0
		for x in range(3,a):
			if(a%x==0):
				count+=1
		if(count>0):
			return False
	return True
def Check_p_q(p,q):
	if(not check_prime(p)):
		print("P is not prime")
		return False
	if( not check_prime((q))):
		print("q is not Prime")
		return False
	if((p-1)%q!=0):
		print('p is NOT prime modulus of Q')
		return False
	return True			
print("Enter P ")
p = int(input())
print("Enter Q")
q = int(input())
print("Enter message")
msg = raw_input()
if(Check_p_q(p,q)):
	print("PRIME WORKS")
h = random.randint(1,p-1)
g = pow(h,((p-1)/q))%p
print("Enter X")
x = int(input())
k = random.randint(1,q)
y = (pow(g,x)%p)
r = (pow(g,k)%p)%q
m = hashlib.sha1()
m.update(msg)
print(m.hexdigest())
H = int(str(m.hexdigest()),16)
print("H : ",H)
temp = float(1)/k
temp = temp%q
s = temp*(H + (r*x))
print("R : ",r)
print("S : ",s)
w = (1/s)%q
u1 = (H*w)%q
u2 = (r*w)%q
v = ((pow(g,u1)*pow(y,u2))%p)%q
if(v==r):
	print("VERIFIED")
else:
	print("BMJ")






