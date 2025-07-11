# 📝 Task Management System - Django

A simple Task Management web application built using Django.  
This app helps users to create, update, delete, and manage their daily tasks effectively.

---

## 🚀 Features

- User authentication (Login, Register, Logout)
- Task CRUD operations
- Prioritized task tracking
- Admin panel for data control

---

## 🖥️ Running the Project Locally (Mac M1 Compatible)

### ✅ Prerequisites

- Python 3.10+
- Git
- Virtualenv (optional but recommended)
- (Optional) Homebrew for macOS:  
  [https://brew.sh](https://brew.sh)

---

### 🔧 Setup Instructions


```bash
#Clone the Repository

git clone https://github.com/Moniruzzaman-Shawon/Task-Management-Django.git
cd Task-Management-Django

#Create and Activate Virtual Environment
python3 -m venv venv

source venv/bin/activate  # For macOS/Linux

# Install Required Packages
pip install -r requirements.txt
 #or 
pip install django

#Apply Migrations
python manage.py migrate
python manage.py runserver


#Run the Development Server
python manage.py runserver
```


📁 Folder Structure
```
Task-Management-Django/
│
├── taskapp/           # Main Django App
├── templates/         # HTML Templates
├── static/            # Static files
├── db.sqlite3         # SQLite DB (default)
├── manage.py
└── requirements.txt   # Project dependencies


```


📦 Optional: PostgreSQL Support
```
brew install postgresql
brew services start postgresql
```

## settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```

## ✍️ Author

**Moniruzzaman Shawon**  
🔗 [LinkedIn](https://www.linkedin.com/in/moniruzzamanshawon/)  
📫 Email: m.zaman.djp@gmail.com

---

Copyright (c) 2025 Moniruzzaman Shawon

