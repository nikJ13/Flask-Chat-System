# Flask-Chat-System
This chat system implements facial authentication for the user to log into the system. Also secret messages can be sent between the users who use this application. This message can be read only through facial authentication. This project is primarily developed to display the backend security functionality.

Technology used:
- Python (Flask, face_recognition,socket.io,pymongo,opencv)
- Javascript (Frontend, socket.io)
- HTML
- MongoDB

##Future Scope
-Improve the UI
-Make the application more scalable

##Screenshots of Output
![image](https://user-images.githubusercontent.com/51831161/156635225-834770e6-3ddd-4472-99e4-dcf3b2c901a8.png)

Signup Page


![image](https://user-images.githubusercontent.com/51831161/156635352-19e16be0-d10d-48d2-9b25-0375b352dc15.png)

Storing user credentials and face data in encrypted format on MongoDB


![image](https://user-images.githubusercontent.com/51831161/156635448-de3fa011-227b-474b-bbc8-9f796a2d23ab.png)

Login Using Facial Authentication


![image](https://user-images.githubusercontent.com/51831161/156635651-fa1c1aa9-4765-4c19-b5d9-ad927eb123d6.png)

Create chat room


![image](https://user-images.githubusercontent.com/51831161/156635736-46ff0c65-07c5-44ce-bbc4-392d185ad245.png)

Users can chat


![image](https://user-images.githubusercontent.com/51831161/156636099-eff62b45-7820-459f-bfe0-1784444247f8.png)

The normal messages are encrypted in the backend to avoid Man-in-the-Middle attacks


![image](https://user-images.githubusercontent.com/51831161/156636486-ca6cd46e-ecf8-47c1-a0f6-b37e0ac819cb.png)

Secret messages can be sent on the chat to avoid shoulder spoofing. They can be accessed through facial authentication only.

