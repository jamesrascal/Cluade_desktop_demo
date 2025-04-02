```
This app is a demo app generated using Calude Code CLI as a demo for a video
```

# Flask Form Application

A simple Flask web application with user authentication, form submission, and admin panel.

## Features

- User registration and login
- Protected form submission (only for authenticated users)
- Admin panel to view all submitted forms
- Bootstrap styling for responsive design

## Setup Instructions

1. Clone the repository

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python run.py
```

5. Access the application at `http://127.0.0.1:5000`

## Default Admin User

Username: admin  
Email: admin@example.com  
Password: admin123

## Project Structure

```
app/
  ├── static/
  │   └── main.css
  ├── templates/
  │   ├── admin.html
  │   ├── home.html
  │   ├── layout.html
  │   ├── login.html
  │   ├── register.html
  │   └── submit.html
  ├── forms/
  │   ├── auth.py
  │   └── submission.py
  ├── models/
  │   ├── user.py
  │   └── submission.py
  ├── routes/
  │   ├── admin.py
  │   ├── auth.py
  │   ├── forms.py
  │   └── main.py
  └── __init__.py
run.py
requirements.txt
README.md
```