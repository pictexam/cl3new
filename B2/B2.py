from flask import Flask , request, render_template

app = Flask(__name__) #Flask constructor takes the name of current module (__name__) as argument.

@app.route('/') #The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
def fun():
    return render_template('h.html',msg="") #render the template without any message
    
@app.route('/',methods=['POST']) #this url calls the checker function for evaluating plagarism
def check():
    a = checker(request.form['string'])
    return render_template('h.html',msg=a) #render the template with the plagarism percentage

def checker(str1):
    file_data=""
    with open('data.txt','rt') as f:
        file_data = f.read()
    
    # remove unwanted characters from both strings
    unwanted_chars = ":?.-!_/\,;"
    for char in unwanted_chars:
        file_data = file_data.replace(char,"") #remove the inwanted characters from the data and the knowledge
        str1 = str1.replace(char,"")

    a = file_data.split()
    print a
    b = str1.split()
    print b

    copy_count = 0

    for i in b:
        if i in a:
            copy_count = copy_count + 1
                
    print "copy_count = ", copy_count
    percentage = str(float(copy_count)/len(a)*100.0) + "%"                
    return percentage

if __name__=="__main__":
    app.run()
