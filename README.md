# GateMate – Smart Gate Pass Management System

## Overview

GateMate is a Flask-based Smart Gate Pass Management System designed for colleges and institutions.
It provides a secure and automated gate pass workflow with:

* Student Login & Registration
* Parent OTP Verification
* Coordinator Approval
* HOD Approval
* QR-Based Gate Pass
* QR Verification at Gate
* SMS Notifications using Twilio
* AI-Based Request Analysis

---

# Features

## Student Module

* Register/Login
* Submit gate pass request
* Parent OTP verification
* Track request status
* View QR Gate Pass after approval

---

## Coordinator Module

* View pending requests
* Approve or reject requests
* Forward approved requests to HOD

---

## HOD Module

* View forwarded requests
* Final approve/reject requests
* Generate QR-based gate pass
* Send SMS notification to parents

---

## Security Features

* Password hashing using bcrypt
* OTP verification
* QR expiration handling
* One-time QR usage
* Session-based authentication

---

# Tech Stack

## Backend

* Python
* Flask

## Database

* MySQL

## Frontend

* HTML
* CSS
* Bootstrap
* Jinja2 Templates

## APIs & Libraries

* Twilio API
* bcrypt
* qrcode
* Flask-WTF

---

# Project Structure

```text
GateMate/
│
├── app.py
├── ai_engine.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── student.html
│   ├── coordinator_dashboard.html
│   ├── hod.html
│   ├── qr_page.html
│   ├── qr_result.html
│   ├── about.html
│   ├── contact.html
│   └── help.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

# Installation

## 1. Clone Project

```bash
git clone <repository_url>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

# Database Setup

## Create Database

```sql
CREATE DATABASE gatemate1;
USE gatemate1;
```

---

## Create Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'student',
    branch VARCHAR(50),
    year VARCHAR(20),
    parents_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Create Gate Pass Requests Table

```sql
CREATE TABLE gate_pass_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    student_name VARCHAR(100) NOT NULL,
    reason TEXT NOT NULL,
    out_date DATE NOT NULL,
    out_time TIME NOT NULL,
    status VARCHAR(30) DEFAULT 'Pending',
    status_coordinator VARCHAR(30) DEFAULT 'Pending',
    coordinator_id INT,
    sentiment VARCHAR(50),
    ai_status VARCHAR(50),
    score FLOAT,
    qr_token VARCHAR(255),
    qr_expires_at DATETIME,
    qr_used BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (student_id) REFERENCES users(id),
    FOREIGN KEY (coordinator_id) REFERENCES users(id)
);
```

---

# Twilio Setup

Open `app.py` and update:

```python
TWILIO_ACCOUNT_SID = "YOUR_SID"
TWILIO_AUTH_TOKEN = "YOUR_TOKEN"
TWILIO_FROM_NUMBER = "YOUR_TWILIO_NUMBER"
```

---

# Run Project

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Create HOD & Coordinator Accounts

## Step 1

Register normally from website.

---

## Step 2

Update roles from MySQL:

### HOD

```sql
UPDATE users
SET role='hod'
WHERE email='hod@gmail.com';
```

### Coordinator

```sql
UPDATE users
SET role='coordinator'
WHERE email='coordinator@gmail.com';
```

---

# Default Workflow

```text
Student
   ↓
Parent OTP Verification
   ↓
Coordinator Approval
   ↓
HOD Approval
   ↓
QR Generation
   ↓
Gate Verification
```

---

# AI Features

The system uses AI logic from `ai_engine.py` to:

* Analyze student request sentiment
* Predict request status
* Generate approval score

---

# Future Improvements

* Face Recognition Integration
* Live Gate Entry Logs
* Mobile App
* Email Notifications
* Dashboard Analytics
* Multi-HOD Support

---

# Author

Sachin Jain

---

# License

This project is developed for educational purposes.
