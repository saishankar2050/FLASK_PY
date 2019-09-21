from flask import Flask,redirect,url_for,render_template,request,flash
from flask_mail import Mail,Message
from random import randint
from db import Base,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager,current_user,login_user,logout_user,login_required

app=Flask(__name__)
app.secret_key='ss'

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

@login_manager.user_loader
def load_user(user_id):
	return session.query(User).get(int(user_id))





























app.secret_key='ss'
engine=create_engine('sqlite:///register.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()

@app.route('/show')
def showdata():
	user1=session.query(User).all()
	return render_template('show.html',reg=user1)

@app.route('/register',methods=['POST','GET'])
def registerData():
	if request.method == 'POST':
		newData=User(name=request.form['name'],id=request.form['id'],email=request.form['email'],password=request.form['password'])
		session.add(newData)
		session.commit()
		flash("new data is added")
		return redirect(url_for('log'))
	else:
		return render_template('register.html')

@app.route('/edit/<int:user_id>',methods=['POST','GET'])
def editData(user_id):
	editeddata=session.query(User).filter_by(id=user_id).one()
	if request.method == 'POST':
		editeddata.id=request.form['id']
		editeddata.name=request.form['name']
		editeddata.email=request.form['email']
		session.add(newData)
		session.commit()
		flash("Data is updated")
		return redirect(url_for('showdata'))


	else:
		return render_template('edit.html',register=editeddata,id=user_id)
@app.route('/delete/<int:user_id>',methods=['POST','GET'])
def deleteData(user_id):
	deletedata=session.query(User).filter_by(id=user_id).one()
	session.delete(deletedata)
	session.commit()
	flash("data is deleted")
	return redirect(url_for('showdata'))
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/show2')
def showda():
	user1=session.query(User).all()
	return render_template('show.html',reg=user1)


'''@app.route('/register1',methods=['POST','GET'])
def registerData():
	if request.method=='POST':
		regdata=User(id=request.form['id'],name=request.form['name'],email=request.form['email'],password=request.form['password'])
		session.add(regdata)
		session.commit()
		return redirect(url_for('login.html'))
	else:
		return render_template('register.html')'''

@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
    	return redirect(url_for('index'))
    try:
        if request.method=='POST':
            user=session.query(User).filter_by(email=request.form['email'],password=request.form['password']).first()
            if user:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Login Failed')
                return render_template('login.html')
        else:
            return render_template('login.html',tittle='login')
    except Exception as e:
        flash("Login Failed")
    else:
    	return render_template('login.html',tittle='login')

	




	
	
    
	

		
		
		



	
	


# '''mail otp
# app=Flask(__name__)


# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']=465
# app.config['MAIL_USERNAME']='saishankar2050@gmail.com'
# app.config['MAIL_PASSWORD']='9951040873'
# app.config['MAIL_USE_TLS']=False
# app.config['MAIL_USE_SSL']=True

# mail=Mail(app)
# otp=randint(000000,999999)
# app.secret_key='ss'

# @app.route('/email')
# def email():
# 	return render_template('email.html')


# @app.route('/email_verify',methods=['POST','GET'])
# def verify():
# 	email=request.form['mail']
# 	msg=Message('OTP for Verification',sender='saishankar2050@gmail.com',recipients=[email])
# 	msg.body=str(otp)
# 	mail.send(msg)
# 	return render_template('verify.html')

# @app.route('/validation',methods=['POST','GET'])
# def validation():
# 	user_otp=request.form['otpvalue']
# 	if otp == int(user_otp):
# 		return "OTP Verification Done!!!"
# 	else:
# 		return "Invalid OTP" 



    	
    
    	


	
	
    
    	


# @app.route('/shankar/')

# def index():
#       return "<h1> hello world !!!!!</h1>"
# @app.route('/shankar/<name>') 
# def index1(name):
# 	 return "welcome %s"%name

# @app.route('/check/<n>')
# def check(n):
# 	if(n=="string"):
# 		return redirect(url_for('index1',name="shankar"))
# 	else:
# 		return redirect(('index'))
# @app.route('/login/<int:v>')
# def login1(v):
#        return render_template('login.html',username=v)
# #file uploading
# @app.route('/upload')
# def upload():
#      return render_template('upload.html')

# @app.route('/success',methods=['POST','GET'])
# def success():
#        if request.method== 'POST':
#        	  f=request.files['image']
#        	  f.save(f.filename)
#        	  return render_template('success.html',name=f.filename)
#        else:
#        	  return " pleased check code:" '''

if __name__=='__main__':
    app.run(debug=True)