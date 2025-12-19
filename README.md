# NewsPaper CRM

## Overview

**NewsPaper** is a Django‑based news publishing platform that allows users to create, manage, and read news articles. It provides a solid foundation for learning Django concepts such as authentication, models, views, templates, and routing.

The project is intentionally kept simple and clean so it can be easily extended with features like categories, comments, search, or APIs.

The goal of this project was to strengthen my Django skills.

---

## Features

* User authentication (sign up, login, logout)
* Article creation and management
* Templated views using Django’s template engine
* Modular Django app structure
* Easy to customize and extend
* Adding comment under each article (New)

---

## Installation

### Prerequisites

* Python **3.8+**
* pip

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/sobhan661/NewsPaper.git
cd NewsPaper
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Apply database migrations**

```bash
python manage.py migrate
```

6. **Create a superuser (admin access)**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. **Open in your browser**

```
http://127.0.0.1:8000/
```

---

## License

This project is licensed under the **MIT License**.