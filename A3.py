from bitstring import BitArray
from flask import *
app = Flask(__name__)
def booth(m,q,x,y):
	totalLength=x+y+1
	mA=BitArray(int=m,length=totalLength)
	print mA
	Add=mA<<(y+1)
	print Add
	mA1=BitArray(int=-m,length=totalLength)
	Sub=mA1<<(y+1)
	Q1=BitArray(int=q,length=y)
	Q1.prepend(BitArray(int=0,length=x))
	P=Q1 << (1)
	print "Add: ",Add.bin
	print "Sub : ",Sub.bin
 	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P=BitArray(int=P.int+Add.int,length=totalLength)
		elif P[-2:] == '0b10':
			P=BitArray(int=P.int+Sub.int,length=totalLength)
		P=BitArray(int=(P.int >>1),length=P.len)
	P = P[:-1]    #everything except the last q0 bit
	print "P : ",P.bin 
	return P.bin,P.int
@app.route('/')
def f():
	return render_template("index.html")
@app.route('/',methods=['POST'])
def g():
	text1 = int(request.form['text1'])
	text2 = int(request.form['text2'])
	n,m=booth(text1,text2,8,8)
        return render_template("index.html",product=n,product2=m)
if __name__ == '__main__':
	app.run('localhost',debug=True,port=5002)
index.html-----------------------------------------------
<!DOCTYPE html>
<html lang="en">
<body>
<h1>Enter data</h1>
<form action="." method="POST">
Enter 1st number:
<input type="text" name="text1">
Enter 2nd number:
<input type="text" name="text2">
<input type="submit" name="my-form" value="Send">
<p> Answer in Binary is: {{product}} and Answer in decimal is: {{product2}} </p>
</form>
</body>
</html>