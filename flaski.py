from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


#def create_app():
    #db.init_app(app)
    #with app.app_context():
        #db.create_all()

    #return app
'''
#Initialize the db
db = SQLAlchemy(app)
db.init_app(app)
'''
'''
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
'''
#Create a function to return string
    #def __repr__(self):
        #return '<Name %r>' % self.id

subscribers = []
'''
db.create_all()
db.session.commit()
'''
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

@app.route('/formularios')
def formularios():
    title_dropdown_5 = 'Formularios/forms'
    return render_template("formularios.html", title= title_dropdown_5)



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

global answers
answers = []

@app.route('/form_dos', methods = ["POST", "GET"])
def form_dos():

    one = request.form.get("one")
    two = request.form.get("two")
    three = request.form.get("three")
    four = request.form.get("four")

    if not one or not two or not three or not four:
        error_statement = "All form fields are required"
        return render_template('fail.html', error_statement = error_statement,
                               one = one, two = two, three = three, four = four)


    if one == "uno" and two == "dos" and three == "tres" and four == "cuatro":
        return render_template('perfect_score.html')
    else:
        answers.append(f"'one' is {one}'two is' {two}'three is' {three} 'four is {four}")
        return render_template('form_dos.html', answers=answers)

@app.route('/perfect_score', methods = ["POST", "GET"])
def perfect_score():
    title_perfect = "You got a perfect score!"
    return render_template('perfect_score.html', title = title_perfect, answers=answers)

    one = request.form.get("one")
    two = request.form.get("two")
    three = request.form.get("three")
    four = request.form.get("four")

    answers.append(f"'one' is {one}'two is' {two}'three is' {three} 'four is' {four}")
    return answers

@app.route('/music')
def music():
    title_four = 'Escuche gratis.'
    return render_template('music.html', title=title_four)

@app.route('/problemas_de_verbos')
def problemas_de_verbos():
    title_vbs = 'Listen to the recordings and write the English or Spanish translation on the line.'
    return render_template('problemas_de_verbos.html', title=title_vbs)

global verb_answers
verb_answers = []

@app.route('/form_tres', methods = ["POST", "GET"])
def form_tres():

    vb_one = request.form.get("vb_one")
    if vb_one == "yo hablo":
        return render_template('perfect_score_dos.html')
    else:
        return render_template('form_tres.html', answers=verb_answers)


@app.route('/perfect_score_dos', methods = ["POST", "GET"])
def perfect_score_dos():
    title_perfect = "You got a perfect score!"
    return render_template('perfect_score_dos.html', title = title_perfect, answers=verb_answers)


if __name__ == "__main__":
    app.run(debug=True)
