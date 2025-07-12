## Django Todo App 📝
A simple and user-friendly Todo application built with Django, demonstrating essential CRUD functionality and clean UI.

## Features
- Create new tasks
- Update (edit) existing tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Filter tasks by status or date (if implemented)
- Clean UI, optionally using Bootstrap and Django’s message framework

## Project Structure
'''django-todo/
├── manage.py
├── db.sqlite3           # Default SQLite database (can use Postgres, MySQL, etc.)
├── requirements.txt
├── todo/                # Django app
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Task model
│   ├── views.py         # CRUD views
│   ├── forms.py         # (optional) ModelForm for tasks
│   ├── urls.py          # App-specific URLs
│   ├── templates/
│   │   └── todo/
│   │       ├── base.html
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       └── task_confirm_delete.html
│   └── static/          # CSS, JS, images
└── project/             # Your Django project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py'''

Requirements
Python 3.x
Django ≥3.x
SQLite (default) — you can update DATABASES in settings.py to use another database

Installation
Clone your repo
git clone https://github.com/codewithadityaj/django-todo.git
cd django-todo


Create a virtual environment and activate it

python -m venv env
# On macOS/Linux:
source env/bin/activate
# On Windows:
.\env\Scripts\activate
Install dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Make and apply migrations

nginx
Copy
Edit
python manage.py makemigrations
python manage.py migrate
(Optional) Create a superuser

nginx
Copy
Edit
python manage.py createsuperuser
Run the development server

nginx
Copy
Edit
python manage.py runserver
Visit this URL in your browser:
http://127.0.0.1:8000/todo/

Usage
Add a task via the “Create Task” page

Check/uncheck tasks to mark them complete/incomplete

Edit or delete tasks using the action buttons

Optionally filter tasks by status or date (if implemented)

Optionally login to access admin interface or user-specific data

Recommended Enhancements
Add user authentication to enable per-user task lists

Use Django’s message framework for notifications

Style the app using Bootstrap/Tailwind for better UI

Extend the Task model to include fields like due date, priority, tags

Convert to class-based views (ListView, CreateView, etc.) for cleaner code

Add pagination or search functionality

Security & Deployment Tips
Enable DEBUG = False in settings.py for production

Use a strong SECRET_KEY and store it securely

Serve static files via WhiteNoise or a dedicated static server

Use HTTPS and secure database credentials

Consider deploying with Gunicorn + Nginx on a VPS or cloud platform

License
This project is open-source and available under the MIT License. See the LICENSE file for details.

Author
Aditya Ashok Jadhav
GitHub
