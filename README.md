 CLM Django Project

This is the **CLM Django project**, a web application built with **Django** and Python.  
This README guides you on how to set up the project locally, install dependencies, and run it.

---

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.10+  
- pip (Python package manager)  
- virtualenv (optional but recommended)  
- PostgreSQL or another database (depending on your `settings.py`)  

---

## 1. Clone the Repository

```bash
git clone https://github.com/isurupsk/CLM-.git
cd CLM-
2. Create a Virtual Environment
It is recommended to use a virtual environment to isolate dependencies:

bash
Copy code
# Create virtual environment
python3 -m venv env

# Activate it (Linux/macOS)
source env/bin/activate

# Activate it (Windows)
env\Scripts\activate
3. Install Dependencies
Install all Python dependencies from requirements.txt:

bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
4. Configure Environment Variables
The project uses environment variables for sensitive keys (AWS, DB, etc).
Create a .env file in the root project directory:

ini
Copy code
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
SECRET_KEY=your_django_secret_key
Make sure .env is added to .gitignore to prevent exposing secrets.

5. Database Setup
Make sure your database is running (PostgreSQL, MySQL, or SQLite).

bash
Copy code
# Apply migrations to create database tables
python manage.py makemigrations
python manage.py migrate
6. Create Superuser (Admin)
To access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set username, email, and password.

7. Run the Project
Start the Django development server:

bash
Copy code
python manage.py runserver
Open your browser and go to:
http://127.0.0.1:8000

8. Optional Commands
Run tests:

bash
Copy code
pytest
Collect static files (if using static files):

bash
Copy code
python manage.py collectstatic
