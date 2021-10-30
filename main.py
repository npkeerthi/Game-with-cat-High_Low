from flask import Flask
import random

n=random.randint(0,9)

app=Flask(__name__)

@app.route('/')
def home():
    return '<img style="margin-left:210px" width=250px src="https://media0.giphy.com/media/FrEnONcaBGJ0c/giphy.gif?cid=ecf05e47h1pff32wt70y9v789djh3no9adnytp0l6ily27y0&rid=giphy.gif&ct=g">' \
           '<h1 style=" position:relative; left:480px; bottom:100px; color:#FFB319" >Elloo!..Will you play with me?</h1> ' \
           '<h1 style=" text-align:center; margin-top:-68px; ">  Guess The Number I Have Chosen Between 0 and 9 </h1>' \
           '<img style="margin-left:420px" src="https://media4.giphy.com/media/JdFEeta1hLNnO/200w.webp?cid=ecf05e47gsp82mx0xne1td0c27hciy7l8vb028yucwkykshn&rid=200w.webp&ct=g">'

@app.route('/<int:num>')
def nums(num):
    if n > num:
        return '<h1 style="text-align:center;color:#FFA0A0"> Too Low ... Try Again <br> where are you... </h1>' \
               '<img style="margin-left:390px" width=330px src="https://media3.giphy.com/media/Vzkgcis3OCRUSVMleW/giphy.gif?cid=ecf05e47agprvkjgqt76hosh2fcgrjvxt4ozzopsfbb4a925&rid=giphy.gif&ct=g">'
    elif n < num:
        return '<h1 style="text-align:center;color:#B91646"> Too High !!   Try Again.... <br>Im searching for you.</h1>' \
               '<img style="margin-left:390px" width=280px src="https://media0.giphy.com/media/ck0U1b3jHLgKWFd84X/giphy.webp?cid=ecf05e4765tn4zprqrucip3ibfchoc5h0lilj5xie6i8luqn&rid=giphy.webp&ct=g">'
    else:
        return '<h1 style="text-align:center;color:#FFA6D5"> 😸 Yaay...<br>You Found Me...!!!</h1>' \
               '<img style="margin-left:380px" width=350px src="https://media2.giphy.com/media/LqVHd24x3QoWA/giphy.gif?cid=ecf05e477jf049zad5fz1zvuylsyt8zuds2rqvtsp7dd3kko&rid=giphy.gif&ct=g">'


if __name__=="__main__":
    print(n,"is the number in my 🧠 ")
    app.run(debug=True)








