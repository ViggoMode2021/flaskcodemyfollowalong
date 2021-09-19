from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

#Initialize the db
db = SQLAlchemy(app)
db.init_app(app)


#Create db model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last = db.Column(db.String(50))
    email = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, first_name, last, email, date_created):
        self.first_name = first_name
        self.last = last
        self.email = email
        self.date_created = date_created

#Create a function to return string
    #def __repr__(self):
        #return '<Name %r>' % self.id

subscribers = []

db.create_all()
db.session.commit()

@app.route('/')
def index():
    title = "Ryan Viglione's website"
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = "Links to Ryan's other websites"
    return render_template("about.html", title= title)

@app.route('/subscribe')
def subscribe():
    title_two = 'Puedes subscribirte ahora'
    return render_template('subscribe.html', title=title_two)

@app.route('/practice_Spanish')
def practice_Spanish():
    title_four = 'Practice Spanish here'
    return render_template('practice_Spanish.html', title=title_four)

#Dropdowns
@app.route('/adjetivos')
def adjetivos():
    title_dropdown_1 = 'Adjetivos/adjectives'
    return render_template("adjetivos.html", title= title_dropdown_1)

@app.route('/sustantivos')
def sustantivos():
    title_dropdown_2 = 'Sustantivos/nouns'
    return render_template("sustantivos.html", title= title_dropdown_2)

@app.route('/Cultura')
def Cultura():
    title_dropdown_3 = 'Cultura/culture'
    return render_template("Cultura.html", title= title_dropdown_3)

@app.route('/verbos')
def verbos():
    title_dropdown_5 = 'Verbos/verbs'
    return render_template("verbos.html", title= title_dropdown_5)



@app.route('/form', methods = ["POST"])
def form():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    '''
    if request.method == "POST":
        friend_name = request.form['first_name', 'last_name', 'email']
        new_friend = Friends(name=friend_name)

        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect ('/subscribe')

        except:
            return "Error"

    else:
        friends = Friends.query.order_by(Friends.date_created)
        return render_template("subscribe.html")

    message = "You have been subscribed to my email newsletter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("ryansviglione@gmail.com", "")
    server.sendmail("ryansviglione@gmail.com", email, message)
    '''
    if not first_name or not last_name or not email:
        error_statement = "All form fields are required"
        return render_template('fail.html', error_statement = error_statement,
                               first_name = first_name, last_name = last_name, email = email)

    subscribers.append(f"{first_name} {last_name} {email}")
    title_three = 'Muchas gracias.'
    return render_template('form.html', title=title_three, subscribers=subscribers)

@app.route('/music')
def music():
    title_four = 'Escuche gratis.'
    return render_template('music.html', title=title_four)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

#####################################RESERVES###############################################

#first_name = first_name, last_name= last_name, email = email
    '''
 <img src="static/images/SoundCloud.png" width="300">
        <a href="https://www.qries.com/">
    '''
