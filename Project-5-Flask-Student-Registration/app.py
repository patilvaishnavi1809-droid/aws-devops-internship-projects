"""
Flask-Based Student Registration Web Application
--------------------------------------------------
Allows users to register students via a web form, stores the data in MySQL,
and provides a page to view all registered students.
"""
import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# MySQL configuration (pulled from environment variables)
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST", "localhost")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER", "root")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD", "")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB", "student_registration")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_REGEX = re.compile(r"^[0-9]{10}$")


def validate_form(name, email, phone, course, address):
    """Server-side validation mirroring the client-side checks."""
    errors = []
    if not name or len(name.strip()) < 2:
        errors.append("Name must be at least 2 characters long.")
    if not email or not EMAIL_REGEX.match(email):
        errors.append("Please enter a valid email address.")
    if not phone or not PHONE_REGEX.match(phone):
        errors.append("Phone number must be exactly 10 digits.")
    if not course or len(course.strip()) < 2:
        errors.append("Course is required.")
    if not address or len(address.strip()) < 5:
        errors.append("Address must be at least 5 characters long.")
    return errors


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        course = request.form.get("course", "").strip()
        address = request.form.get("address", "").strip()

        errors = validate_form(name, email, phone, course, address)
        if errors:
            for e in errors:
                flash(e, "error")
            return render_template("index.html", form=request.form)

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO students (name, email, phone, course, address) "
                "VALUES (%s, %s, %s, %s, %s)",
                (name, email, phone, course, address),
            )
            mysql.connection.commit()
            cur.close()
            flash("Student registered successfully!", "success")
            return redirect(url_for("register"))
        except Exception as e:
            flash(f"Database error: {e}", "error")
            return render_template("index.html", form=request.form)

    return render_template("index.html", form={})


@app.route("/students")
def students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students ORDER BY created_at DESC")
    rows = cur.fetchall()
    cur.close()
    return render_template("students.html", students=rows)


@app.route("/students/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cur.close()
    flash("Student record deleted.", "success")
    return redirect(url_for("students"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
