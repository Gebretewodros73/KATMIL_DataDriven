#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration settings
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checklist.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your_secret_key_here'  # Remember to change this to a secure value in production

# db = SQLAlchemy(app)

# class Checklist(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # checklist_type = db.Column(db.String(50))
    # confirmed = db.Column(db.Integer)
    # not_confirmed = db.Column(db.Integer)
    # not_applicable = db.Column(db.Integer)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/concrete_checklist')
def concrete_checklist():
    return render_template('concrete_checklist.html', title='Concrete Checklist')

@app.route('/electrical_checklist')
def electrical_checklist():
    return render_template('electrical_checklist.html', title='Electrical Checklist')

@app.route('/formwork_checklist')
def formwork_checklist():
    return render_template('formwork_checklist.html', title='Formwork Checklist')

@app.route('/nightwork_checklist')
def nightwork_checklist():
    return render_template('nightwork_checklist.html', title='Nightwork Checklist')

@app.route('/reinforcement_checklist')
def reinforcement_checklist():
    return render_template('reinforcement_checklist.html', title='Reinforcement Checklist')

@app.route('/dailydiary_checklist')  # Corrected the decorator
def dailydiary_checklist():
    return render_template('dailydiary_checklist.html', title='Daily Diary Checklist')

@app.route('/about')
def about():
    return render_template('about.html', title='About The Company')

@app.route('/showcase')
def showcase():
    return render_template('showcase.html', title='Showcase')

@app.route('/formats')
def formats():
    return render_template('formats.html', title='Forms')

#@app.route('/submit', methods=['POST'])  # Corrected the methods string
#def submit():
    checklist_type = request.form.get('checklist_type')
    confirmed = request.form.getlist('confirmed')
    not_confirmed = request.form.getlist('not_confirmed')
    not_applicable = request.form.getlist('not_applicable')
    
    confirmed_count = len(confirmed)
    not_confirmed_count = len(not_confirmed)
    not_applicable_count = len(not_applicable)
    
    checklist = Checklist(
        checklist_type=checklist_type,
        confirmed=confirmed_count,
        not_confirmed=not_confirmed_count,
        not_applicable=not_applicable_count
    )
    db.session.add(checklist)
    db.session.commit()
    
    return render_template('result.html', confirmed=confirmed_count, not_confirmed=not_confirmed_count, not_applicable=not_applicable_count)

# Ensure to add other routes as needed for your application.

if __name__ == '__main__':
    with app.app_context():
        app.run()