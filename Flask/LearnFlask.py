from flask import Flask , render_template , redirect , request
import os

web = Flask(__name__)

picfolder = os.path.join('static/images/')
web.config['PIC_FOLDER'] = picfolder

@web.route('/')
@web.route('/register')
def home():
    pic = os.path.join(web.config['PIC_FOLDER'] , 'Hashira.jpg')
    return render_template('register.html' , pic = pic)

@web.route('/confirm' , methods=['POST' , 'GET'])
def register():
    if request.method == "POST":
        n= request.form.get('Name')
        c = request.form.get('City')
        p = request.form.get('PhnNum')
        return render_template('confirm.html' , name = n , City = c ,PhnNum = p)        

if __name__ == '__main__':
    web.run(debug=True)
    
