def checker(str1):
    file_data=""
    with open('input.txt','rt') as f:
        for line in f:
            file_data = file_data + line
    a = file_data.split('.')
    print 'Original File: ', a
    b = str1.split('.')
    print 'Input Text ', b
    for i in range(len(a)-1):
    	a[i]=str(a[i]).strip()
	for i in range(len(b)-1):
    	b[i]=str(b[i]).strip()
	count = 0
    for i in a:
    	print('\n')
    	print(i)
    	print('Compared With: ')
        for j in range(0,len(b)-1):
        	print(b[j])
        	if i==b[j]:
		        count=count+1
	print "Total count matched = ",count
    print "Original length: ", len(a)-1
    percentage = (float(count)/(len(b)-1))*100.0      #check if a          
    return percentage
server.py------------------
from plag import *
from flask import Flask , request, render_template
app = Flask(__name__)
@app.route('/')
def fun():
    return render_template('index.html',msg=None)
@app.route('/eval',methods=['POST','GET'])
def check():
    a = checker(request.form['string'])
    return render_template('index.html',msg=a)
if __name__=="__main__":
    app.run()
index.html--------------------
<html>
<head>
<title>Plagiarism Detection</title>
</head>
<body>
<h1>
Plagiarism Detection Program
</h1>
 <form method="POST" action="/eval">
  Enter Text: <input type="string" name="string"><br>
  <input type="submit" value="Submit">
</form> 
<h3>The percentage of plagiarism is: {{ msg }}<h3>
</body>
</html>

