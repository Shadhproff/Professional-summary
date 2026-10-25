# PYTB-1026: Django Multimedia Website Application

A full-stack web application built using Python and Django that allows users to upload, manage, and showcase multimedia items dynamically backed by a local SQLite database.

---

## 📌 Project Overview
This project was built as part of the PYTB-1026 Section Assignment. It demonstrates backend development concepts using Python and Django, implementing the **Model-View-Template (MVT)** architectural pattern, database persistence via SQLite, and custom local timezone configurations.

---

## 🚀 Key Features
* **Dynamic Content Management:** Add, view, and manage titles, descriptions, and media files directly through the built-in Django Admin dashboard.
* **MVT Architecture:** Clean separation of concerns using Models (`models.py`), Views (`views.py`), and HTML Templates.
* **Database Persistence:** Automatically utilizes a lightweight **SQLite** (`db.sqlite3`) database for reliable record handling.
* **Local Time Localization:** Configured with custom timezone settings (`Africa/Lagos`) to accurately record upload timestamps.

---

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite
* **Frontend:** HTML5, CSS3, Django Templates
* **Version Control:** Git & GitHub

---

## ⚙️ How to Run Locally

Follow these steps to set up and run the project on your local machine:

### 1. Clone the repository
```bash
git clone [https://github.com/Shadhproff/Professional-summary.git](https://github.com/Shadhproff/Professional-summary.git)
cd Professional-summary


2. Create and activate a virtual environment   
On Windows:   
Bash
python -m venv venv
venv\Scripts\activate
On macOS/Linux:   
Bash
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
Bash
pip install django
4. Run database migrations
Bash
python manage.py migrate
5. Start the development server
Bash
python manage.py runserver
6. View in browser
Open your web browser and navigate to:http://127.0.0.1:8000/
👨‍💻 Author Olafenwa Muhammed-shadhily
GitHub: @Shadhproff