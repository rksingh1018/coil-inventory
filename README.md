# Coil Inventory Management System

A RESTful inventory management API built using Django and Django REST Framework.

## Features
- User authentication
- Coil inventory CRUD
- Sales orders with multiple items
- Inventory deduction on confirmed orders
- Low stock notifications
- Transaction-safe concurrency handling

## Tech Stack
- Django
- Django REST Framework
- SQLite (default)

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
