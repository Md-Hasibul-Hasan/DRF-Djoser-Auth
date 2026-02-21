# 🔐 DRF Djoser Authentication System

![Django](https://img.shields.io/badge/Django-4.x-green)
![DRF](https://img.shields.io/badge/DRF-REST_Framework-red)
![Djoser](https://img.shields.io/badge/Auth-Djoser-yellowgreen)
![JWT](https://img.shields.io/badge/JWT-Enabled-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

A complete authentication backend built with **Django REST Framework + Djoser + JWT (SimpleJWT)**.

This system provides secure user authentication including registration, email verification, login, token management, password reset, and protected profile endpoints.

---

# 📬 API Documentation (Postman)

Full API documentation available here:

🔗 **Postman Documentation:**  
https://documenter.getpostman.com/view/48875561/2sBXVkBVJf

You can use the Postman collection to test all endpoints including:
- Registration
- Login
- JWT Token
- Profile
- Email Verification
- Password Reset

---

# 🚀 Features

- ✅ User Registration
- ✅ Email Verification
- ✅ Secure Login
- ✅ JWT Access & Refresh Tokens
- ✅ Token Refresh & Verify
- ✅ Protected Profile Endpoint
- ✅ Change Password
- ✅ Password Reset via Email
- ✅ Djoser Integration
- ✅ Scalable API Architecture

---

# 📡 API Endpoints

## 🔑 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/user/register/` | Register new user |
| POST | `/api/user/login/` | Login user |
| POST | `/api/user/token/` | Obtain JWT tokens |
| POST | `/api/user/token/refresh/` | Refresh access token |
| POST | `/api/user/token/verify/` | Verify token |

---

## 📧 Email Verification

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/user/verify-email/<uid>/<token>/` | Verify email address |

---

## 👤 User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/user/profile/` | Get user profile (Protected) |
| POST | `/api/user/change-password/` | Change password |
| POST | `/api/user/send-reset-password-email/` | Send reset password email |
| POST | `/api/user/reset-password/<uid>/<token>/` | Reset password |

---

## 🗂 Full Route Summary

```
admin/
api/user/token/
api/user/token/refresh/
api/user/token/verify/
api/user/register/
api/user/verify-email/<uid>/<token>/
api/user/login/
api/user/profile/
api/user/change-password/
api/user/send-reset-password-email/
api/user/reset-password/<uid>/<token>/
```

---

# 🔄 Authentication Flow

### 1️⃣ Register
POST → `/api/user/register/`

### 2️⃣ Verify Email
Click link:
```
/api/user/verify-email/<uid>/<token>/
```

### 3️⃣ Login
POST → `/api/user/login/`

Response:
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### 4️⃣ Access Protected Routes
Add header:
```
Authorization: Bearer <access_token>
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | Django |
| API | Django REST Framework |
| Authentication | Djoser + SimpleJWT |
| Database | SQLite |
| Email | Django Email Backend |

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/DRF_Djoser_Auth.git
cd DRF_Djoser_Auth
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If not available:

```bash
pip install django djangorestframework djoser djangorestframework-simplejwt
```

---

## 4️⃣ Configure Settings

Add to `INSTALLED_APPS`:

```python
'rest_framework',
'rest_framework.authtoken',
'djoser',
```

JWT Configuration:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

DJOSER Configuration:

```python
DJOSER = {
    'USERNAME_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SEND_ACTIVATION_EMAIL': True,
    'PASSWORD_RESET_CONFIRM_URL': 'reset-password/{uid}/{token}',
    'ACTIVATION_URL': 'verify-email/{uid}/{token}',
}
```

---

## 5️⃣ Run Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- JWT Authentication Implementation
- Email Verification Workflow
- Password Reset Flow
- Secure Protected APIs
- RESTful API Architecture
- Production-Ready Backend Setup

---

# 👨‍💻 Author

**Md-Hasibul-Hasan**  
Backend Developer (Django & DRF)

---

# 📜 License

This project is developed for educational and portfolio purposes.
