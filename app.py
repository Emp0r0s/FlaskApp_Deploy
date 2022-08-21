#import-modules
from flask import Flask
from datetime import datetime
import os

app= Flask(__name__)

#/
@app.route("/")
def home():
    return "Hello World!!!"

#/time
@app.route("/time")
def time():
    now = datetime.now().time()
    current_time = now.strftime("%H:%M:%S")
    return "Current Time = " + str(current_time)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)