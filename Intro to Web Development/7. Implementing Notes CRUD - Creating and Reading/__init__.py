import os
import functools

from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

def create_app(test_config=None):
    # Ommit initial setup

    db.init_app(app)
    migrate = Migrate(app, db)

    def require_login(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if not g.user:
                return redirect(url_for('log_in'))
            return view(**kwargs)
        return wrapped_view

    @app.before_request
    def load_user():
        user_id = session.get('user_id')
        if user_id:
            g.user = User.query.get(user_id)
        else:
            g.user = None

    # Remaining code omitted
    
    # Imports omitted

def create_app(test_config=None):
    # Initial setup omitted

    from .models import db, User, Note

    db.init_app(app)
    migrate = Migrate(app, db)

    # Earlier views omitted

    @app.route('/notes')
    @require_login
    def note_index():
        return 'Note Index'

    @app.route('/notes/new', methods=('GET', 'POST'))
    @require_login
    def note_create():
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            error = None

            if not title:
                error = 'Title is required.'

            if not error:
                note = Note(author=g.user, title=title, body=body)
                db.session.add(note)
                db.session.commit()
                flash(f"Successfully created note: '{title}'", 'success')
                return redirect(url_for('note_index'))

            flash(error, 'error')

        return render_template('note_create.html')

    return app
    
    
from flask_sqlalchemy import SQLAlchemy
from mistune import markdown

# db and User omitted

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def body_html(self):
        return markdown(self.body)    
