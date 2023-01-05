import os
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='<PATH_TO YOUR_ContainerSecurityfolder>/Projects/templates')

@app.route('/')
def home():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
os.environ['FLASK_DEBUG'] = '1'    
#%env FLASK_DEBUG=1
#python3 app.py --> need to run to start application
