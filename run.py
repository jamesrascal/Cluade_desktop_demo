from app import create_app, db, bcrypt
from app.models.user import User
from app.models.submission import Submission
from flask import current_app

app = create_app()

# Create an application context
with app.app_context():
    # Create database tables
    db.create_all()
    
    # Create an admin user if no users exist
    if User.query.count() == 0:
        admin = User(
            username="admin",
            email="admin@example.com",
            password=bcrypt.generate_password_hash("admin123").decode('utf-8'),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")

if __name__ == '__main__':
    app.run(debug=True)