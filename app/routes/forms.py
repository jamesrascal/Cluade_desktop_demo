from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from app import db
from app.models.submission import Submission
from app.forms.submission import SubmissionForm

forms = Blueprint('forms', __name__)

@forms.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    form = SubmissionForm()
    if form.validate_on_submit():
        submission = Submission(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(submission)
        db.session.commit()
        flash('Your submission has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('submit.html', title='New Submission', form=form, legend='New Submission')
