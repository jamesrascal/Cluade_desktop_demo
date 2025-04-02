from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from app.models.submission import Submission

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
def admin_panel():
    if not current_user.is_admin:
        abort(403)
    submissions = Submission.query.order_by(Submission.date_submitted.desc()).all()
    return render_template('admin.html', title='Admin Panel', submissions=submissions)
