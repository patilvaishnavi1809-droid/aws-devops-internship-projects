# Project 5: Flask-Based Student Registration Web Application

## 📌 Objective
A Flask web app that lets users register students via a form, stores the data
in **MySQL**, and displays all registered students in a table — with edit
(delete implemented) capability.

## 🛠 Tech Stack
`Python (Flask)` · `MySQL` · `HTML/CSS` · `Git & GitHub` · `(Optional) EC2 deployment`

## 📎 Reference Repository
Base repo used as a starting point: https://github.com/swati-zampal/stud-reg-flask-app.git

---

## 🚀 Step-by-Step Guide

### Step 1: Set Up the Database
```bash
mysql -u root -p < schema.sql
```
This creates the `student_registration` database and a `students` table with
`name`, `email`, `phone`, `course`, `address` columns.

**✅ Deliverable:** Screenshot of `SHOW TABLES;` / `DESCRIBE students;` output.
📸 `screenshots/step1-database-schema.png`

---

### Step 2: Configure Environment Variables
```bash
cp .env.example .env
# then edit .env with your MySQL host / user / password
```

**✅ Deliverable:** N/A (no secrets in screenshots) — confirm `.env` is in `.gitignore`.

---

### Step 3: Install Dependencies & Run Locally
```bash
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```
Visit `http://localhost:5000` in your browser.

**✅ Deliverable:** Screenshot of the registration form running in the browser.
📸 `screenshots/step3-form-running.png`

---

### Step 4: Register a Student (Form Handling + Validation)
Fill out the form with a name, email, 10-digit phone number, course, and address.
- **Client-side**: HTML5 `required`/`pattern` attributes + a small JS check on phone.
- **Server-side**: `validate_form()` in `app.py` re-validates everything before
  writing to MySQL (never trust client-side validation alone).

**✅ Deliverable:** Screenshot of a successful "Student registered successfully!" message.
📸 `screenshots/step4-successful-registration.png`

---

### Step 5: View Registered Students
Navigate to `http://localhost:5000/students` to see all records in a table,
sorted by most recently registered, with a **Delete** action per row.

**✅ Deliverable:** Screenshot of the students table with at least 2–3 entries.
📸 `screenshots/step5-students-table.png`

---

### Step 6 (Optional): Deploy to EC2
1. Launch an EC2 instance, install Python + MySQL client.
2. Clone this repo, repeat Steps 1–3 on the instance.
3. Run behind `gunicorn` + `nginx` (recommended) or `flask run --host=0.0.0.0`
   for a quick demo.
4. Open the relevant security group port (80 or 5000).

**✅ Deliverable (if completed):** Public URL + screenshot of the app running on EC2.
📸 `screenshots/step6-ec2-deployment.png`

---

## 📂 Repository Structure
```
Project-5-Flask-Student-Registration/
├── README.md
├── app.py
├── requirements.txt
├── schema.sql
├── .env.example
├── templates/
│   ├── index.html
│   └── students.html
├── static/
│   └── style.css
└── screenshots/
```

## ✅ Deliverables Checklist
- [ ] Complete Flask project hosted on GitHub
- [ ] GitHub repo link in documentation
- [ ] README with overview, setup instructions, screenshots, component explanation (this file)
- [ ] (Optional) Deployment URL if hosted publicly
