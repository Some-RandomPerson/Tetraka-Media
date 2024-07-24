from flask import Flask, render_template, redirect, request, url_for
import os
import webbrowser
import time
from cryptography.fernet import Fernet
import sys

app = Flask(__name__)


#home page uwu

@app.route("/", methods=["GET", "POST"])
def home():
    time.sleep(0.4)
    return render_template('home.html')


#keyboard stuff

@app.route("/keyboards", methods=["GET", "POST"])
def keyboards():
    time.sleep(0.4)
    return render_template('keyboards/keyboard-catagory.html')

@app.route("/keyboards/logitech-g915-tkl-review", methods=["GET", "POST"])
def logitech_g915():
    time.sleep(0.4)
    return render_template('keyboards/logitech-g915-rev.html')

@app.route("/keyboards/logitech-g213-review", methods=["GET", "POST"])
def logitech_g213():
    time.sleep(0.4)
    return render_template('keyboards/logitech-g213-rev.html')


#mice stuff

@app.route("/mice", methods=["GET", "POST"])
def mice():
    time.sleep(0.4)
    return render_template('mice/mice-catagory.html')

@app.route("/mice/logitech-g203-rev")
def logitech_g203():
    time.sleep(0.4)
    return render_template('mice/logitech-g203-rev.html')


#monitor stuff

@app.route("/monitors", methods=["GET", "POST"])
def monitors():
    time.sleep(0.4)
    return render_template('monitors/monitor-catagory.html')

@app.route("/monitors/msi-g27cq4-e2", methods=["GET", "POST"])
def msi_g27cq4_e2():
    time.sleep(0.4)
    return render_template('monitors/msi-g27cq4-e2-rev.html')


#social links  

@app.route("/facebook", methods=["GET"])
def facebook():
    time.sleep(0.4)
    return redirect('https://www.facebook.com')

@app.route("/instagram", methods=["GET"])
def instagram():
    time.sleep(0.4)
    return redirect('https://www.instagram.com')

@app.route("/twitter", methods=["GET"]) #im not calling it X, thats a dumb name
def twitter():
    time.sleep(0.4)
    return redirect('https://www.twitter.com')


#encryption of data

key = Fernet.generate_key()
cipher_suite = Fernet(key)


#Form Redirection

@app.route("/redirect", methods=["GET", "POST"])
def redi():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        email = request.form.get("email")
        data = {
            last_name,
            first_name,
            email
        }
        text = str(data)
        # open a file in write mode
        with open('name-list.csv', 'a') as file:
            # write variables using string formatting
            encrypted_text = cipher_suite.encrypt(text.encode())
            file.write(f"{str(encrypted_text)}\n")
            file.close()
        with open('name-list-dec.csv', 'a') as file:
            file.write(str(data))
            file.close()
    else:
        sys.exit()
    print(data)
    time.sleep(0.4)
    return render_template('redirect.html', code=307), {"Refresh": "3; url=/"}
 
#admin

@app.route("/cutomer-data-restricted", methods=["GET", "POST"])
def customer():
    time.sleep(0.4)
    return render_template('customer-data.html')

@app.route("/admin-page", methods=["GET", "POST"])
def admin():
    time.sleep(0.4)
    return render_template('admin-page.html')

 
#application

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
