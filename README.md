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

#### 1. Clone the Repository

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
