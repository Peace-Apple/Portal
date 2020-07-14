from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'astonreba@gmail.com'
app.config['MAIL_PASSWORD'] = 'oqegkrodmxvajxah'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

items = [
    {
        "name": "Apples",
        "unit_price": 100,
        "date_created": datetime.utcnow()
    },
    {
        "name": "Mangoes",
        "unit_price": 100,
        "date_created": datetime.utcnow()
    }
]

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST', 'GET'])
def add_item():
    if request.method == 'POST':
        new_item = {
            "name": request.form['name'],
            "unit_price":request.form['price'],
            "date_created": datetime.utcnow()
        }
        items.append(new_item)

        msg = Message('A new shop item has been added', sender='astonreba@gmail.com', recipients=['martinkatamba@akorion.com'])
        msg.body = str(new_item)
        mail.send(msg)

        return redirect('/')
    else:
        return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
