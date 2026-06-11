from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    username = ' '
    if request.method == 'POST':
        username = request.form.get('username')  
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')

        if password == confirm:
          if (username == password):
            message = "Username and password should be different"
          else:
            message = "Account created"
            return render_template('welcome.html', message=message)
        else:
            message = "Passwords should match"

    return render_template('index.html', message=message, username = username)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
