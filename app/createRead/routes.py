from flask import redirect, render_template, request, session, url_for
from app.createRead import bp
from app.models.createRead import User
from app.extensions import db

@bp.route('/')
def index():
    return render_template('createRead/index.html')

@bp.route('insert/')
def insert():
    return render_template('createRead/insert.html')

@bp.route('insert/test/' , methods=('GET' , 'POST'))
def test():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        userFname = User.query.filter_by(fname=fname).first()
        userLname = User.query.filter_by(lname=lname).first()

        if userFname or userLname:
            return "<h1>User already exist</h1>"

        new_user = User(fname = fname , lname = lname)
        db.session.add(new_user)
        db.session.commit()
        session.clear()
        return render_template('createRead/test.html')

    return redirect(url_for('createRead.insert'))

@bp.route('data/getall/')
def fetch():
    names = User.query.all()
    return render_template('createRead/fetch.html' , names = names)

