# ContainerSecurity
Log into your EC2 instance 
# To clone repository
git clone https://github.com/kmenon95/ContainerSecurity.git	
# To set your EC2
To get flask application need to have flask installed.
1. curl -O https://bootstrap.pypa.io/get-pip.py
2. sudo pip3 install flask
3. python3 app.py

you will get output like-
[ec2-user@ip-172-31-43-236 Projects]$ python3 app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.31.43.236:8080
Press CTRL+C to quit

Copy your public IP with the port you have mentioned and hit it in browser

http://<your_public_IP>:8080/


# Note- You have to open rule in your security group for the port mentioned in app.py you can assign any port number and open rule for it.
