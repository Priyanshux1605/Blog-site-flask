from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Unique id for diary entries
    title = db.Column(db.String(100), nullable=False) #Title
    data = db.Column(db.Text, nullable=False) #Content
    date_posted = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"DiaryEntry('{self.title}', '{self.date_posted}')"

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/add", methods=["GET","POST"])
def add_entry():

    title_from_form = request.form['title']
    data_from_form = request.form['data']

    new_entry = DiaryEntry(title=title_from_form, data=data_from_form)

    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('success'))


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/entries")
def show_entries():

    all_entries = DiaryEntry.query.order_by(DiaryEntry.date_posted.desc()).all()

    return render_template("entries.html", entries_list=all_entries)


if __name__ == "__main__":
    app.run(debug=True)