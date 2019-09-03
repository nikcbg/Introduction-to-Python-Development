# Imports omitted

def create_app(test_config=None):
    # Earlier code omitted

    @app.route('/notes/<note_id>/edit', methods=('GET', 'POST', 'PATCH'))
    @require_login
    def note_update(note_id):
        note = Note.query.filter_by(user_id=g.user.id, id=note_id).first_or_404()
        if request.method in ['POST', 'PATCH']:
            title = request.form['title']
            body = request.body['title']
            error = None

            if not title:
                error = 'Title is required.'

            if not error:
                note.title = title
                note.body = body
                db.session.add(note)
                db.session.commit()
                flash(f"Successfully updated note: '{title}'", 'success')
                return redirect(url_for('note_index'))

            flash(error, 'error')

        return render_template('note_update.html', note=note)

    return app
    
    
    # Imports omitted

def create_app(test_config=None):
    # Earlier code omitted

    @app.route('/notes/<note_id>/delete', methods=('GET', 'DELETE'))
    @require_login
    def note_delete(note_id):
        note = Note.query.filter_by(user_id=g.user.id, id=note_id).first_or_404()
        db.session.delete(note)
        db.session.commit()
        flash(f"Successfully deleted note: '{note.title}'", 'success')
        return redirect(url_for('note_index'))

    return app
