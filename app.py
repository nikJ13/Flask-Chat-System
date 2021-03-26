# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:53:54 2021

@author: anujjain
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager,logout_user,login_required,current_user, login_user
from flask_socketio import SocketIO, join_room
from flask_cors import CORS
from db import get_user,save_user
from pymongo.errors import DuplicateKeyError
from camera import takephoto
from face_compare import comparison

app = Flask(__name__)
app.secret_key = "my secret key" # every flask session should have a secret key defined
CORS(app)
socketio = SocketIO(app,cors_allowed_origins="*")
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@app.route('/')
def home():
    print(current_user.is_authenticated)
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print(current_user)
        return redirect(url_for('home')) # checks if user is already logged in
                                        # user does not need to log in again
    message = ''
    if request.method=='POST':
        username = request.form.get('username')
        password_input = request.form.get('password')
        arr = takephoto()
        user,image_stored = get_user(username)
        #print(image_stored)
        if comparison(arr,image_stored)[0]==None:
            message = 'Please try again!'
        else:
            if user and user.check_password(password_input) and comparison(arr,image_stored)[0]: # checks if the user exists
                print("the user is authenticated")           # and if the password plaintext matches with the password saved in the db
                login_user(user)
                return redirect(url_for('home'))
            else:
                message = 'Failed to login!' # if the auntentication fails
                                             # message to be displayed in the login page
    return render_template('login.html',message=message)

@app.route('/signup',methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        print(current_user)
        return redirect(url_for('home')) # checks if user is already logged in
                                        # user does not need to log in again
    message = ''
    if request.method=='POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password_input = request.form.get('password')
        img = request.form.get('imgdata')
        app.logger.info(img)
        try:
            save_user(username,email,password_input,img)
            return redirect(url_for('login'))
        except DuplicateKeyError:
            message = "User Already Exists"
    return render_template('signup.html',message=message)

@app.route("/logout")
@login_required # if the user is logged in, then only it can access this view
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/chat',methods=['GET','POST'])
@login_required  #chat shown only for logged in users
def chat():
    app.logger.info(request.args["room"])
    username = request.args['username']
    room = request.args['room']
    print(request.headers)
    if username and room:
        return render_template('chat.html',username=username,room=room)
    else:
        return redirect(url_for('home'))
    
@socketio.on("send_message")
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data["username"],
                                                                    data["room"],
                                                                    data["message"]))
    app.logger.info(data)
    if data["name"]=="secret":
        socketio.emit('receive_message', data, message = data['message'], room = data['room'])
    else:
        socketio.emit('message_r',data,message = data['message'], room = data['room'])

@socketio.on("take_photo")
def take_pic_for_auth(data):
    app.logger.info("I am going to take photo")
    arr1 = takephoto()
    user,img_stored = get_user(data["username"])
    if comparison(arr1,img_stored)[0]:
        socketio.emit("confirmed",data)
    else:
        socketio.emit("receive_message",data)
    
@socketio.on("join_room")
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data["username"],data["room"]))
    join_room(data["room"])
    socketio.emit("join_room_announcement",data)
    
@login_manager.user_loader
def load_user(username):               # checks if the username entered exists or not 
    print(username)
    print(get_user(username))       
    return get_user(username)[0]

if __name__=='__main__':
    socketio.run(app, debug=True)
