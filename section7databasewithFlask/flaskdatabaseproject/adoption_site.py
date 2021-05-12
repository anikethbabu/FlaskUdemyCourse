# adoption_site.py
import os
from forms import AddForm, DelForm, OwnerForm
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"

####
# Database Section
####

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

######
# Models
######


class Puppy(db.Model):

    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.Column(db.Text)

    def __init__(self, name, owner=None):
        self.name = name
        self.owner

    def __repr__(self):
        if self.owner is None:
            return f"Puppy {self.name} does not have an owner assigned yet"
        return f"Puppy {self.name} owner is {self.owner}"


# Form view functions
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("list_pup"))
    return render_template("add.html", form=form)


@app.route("/list", methods=["GET", "POST"])
def list_pup():

    puppies = Puppy.query.all()

    return render_template("list.html", puppies=puppies)


@app.route("/delete", methods=["GET", "POST"])
def delete_pup():
    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data

        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for("list_pup"))
    return render_template("delete.html", form=form)


@app.route("/owner", methods=["GET", "POST"])
def add_owner():
    form = OwnerForm()
    if form.validate_on_submit():

        name = form.name.data
        id = form.id.data

        pup = Puppy.query.get(id)
        pup.owner = name
        db.session.commit()
        flash(f"You have chosen {name} as {pup.name}'s owner.")
        return redirect(url_for("list_pup"))

    return render_template("owner.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
