Vision Book Store

Project Overview
Vision Book Store is a full stack web application built using Python and Django.
The application simulates a real online bookstore where users can browse books, add items to a shopping cart, place orders, and review their previous purchases.
Administrators can manage books, categories, and orders using Django’s built-in admin panel.

This project was developed as a capstone project with a strong focus on backend development, REST APIs, authentication, and deployment.

Project Demo


Project Features

User Features
User authentication (login and logout)
Browse all available books
View best-selling books
Add books to cart
Checkout and place orders
View previous orders
View personal profile information

Admin Features
Secure admin panel
Add, edit, and delete books
Manage book categories
Update book prices
View all user orders

Technologies Used

Python
Django
Django REST Framework
SQLite
HTML
Django Templates
Bootstrap
Gunicorn
Git and GitHub
Render

Project Structure

Vision_Book_Store
manage.py
requirements.txt
templates
staticfiles
vision_book_store
accounts
books
cart
orders

API and Backend Architecture

The backend is structured using multiple Django apps to ensure clean separation of concerns.
REST APIs were built using Django REST Framework to handle books, cart operations, and orders.
Authentication and authorization are handled using Django’s built-in authentication system.
The frontend is rendered using Django templates connected directly to backend logic.

How to Run the Project Locally

Clone the repository
Navigate to the project directory
Create and activate a virtual environment
Install dependencies from requirements.txt
Run database migrations
Create a superuser
Start the Django development server

Deployment

The project was deployed as a production web service using Render.
Gunicorn is used as the production server.
Environment variables were configured to ensure compatibility with the deployment platform.
Static files were collected and served correctly.

Deployment Challenges

One of the biggest challenges in this project was deployment.
Before this project, I had no hands-on experience deploying a Django application.

During deployment, I faced several real-world issues such as incorrect project structure, missing modules, wrong Django version in requirements, static file configuration warnings, Python version compatibility problems, and module import errors.

By debugging these issues, reading logs, and fixing configuration problems, I learned how production environments differ from local development and how to properly deploy a Django project.

What I Learned

How to build a complete Django project from scratch
How to structure backend applications professionally
How authentication and authorization work in Django
How REST APIs integrate with frontend templates
How to prepare a Django project for production
How to deploy a backend application to a cloud platform
How to debug real deployment and environment issues

Conclusion

Vision Book Store represents a complete backend-focused web application with real functionality and real deployment experience.
This project significantly improved my understanding of Django, backend development, and production deployment workflows, and it gave me the confidence to build and deploy future full stack applications.