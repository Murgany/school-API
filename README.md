
#School Management System

#Overview

This simple School Management System API is a Django-based web application designed to streamline administrative tasks. The system provides functionalities for managing student information, class details, attendance records, and user authentication.

#API URL: 

https://simpleschoolsystem.pythonanywhere.com/

#Admin user interface URL:

https://simple-school-system.netlify.app/

#Test credentials | both URLs:

Username: Symon
Password: admin

#Features

    Student Information Management
        Store and manage comprehensive student information including name, age, gender, class, section, admission date, guardian details, and emergency contact.
        View, add, update, and delete student records.

    Class Information Management
        Maintain class information such as class name and short form.
        View, add, update, and delete class records.

    Attendance Management
        Record and manage student attendance.
        Mark students as present or absent on specific dates.
        View attendance records for individual students.

    User Authentication and Authorization
        User registration and login functionality.
        Token-based authentication for secure API access.
        Different levels of access control based on user roles (e.g., admin, teacher, student).

#Components

    Models
        StudentClassInfo: Represents information about different classes.
        StudentInfo: Stores details of individual students.
        Attendance: Tracks student attendance records.

    Serializers
        Serialize model data for API interaction.

    Views
        Implement CRUD operations for managing student information, class details, and attendance records.
        User registration and login views.

    Admin Interface - Built with ReactJS
        Custom admin interface for managing student and attendance records.

#Technologies Used

    Django: Backend web framework for building the application.
    Django REST Framework: Used for building RESTful APIs.
    Knox: Token-based authentication library for Django REST Framework.
    SQLite: Default database engine for storing application data.

#Getting Started

    Clone the repository to your local machine.
    Install Python and Django if not already installed.
    Install the required dependencies using pip install -r requirements.txt.
    Run database migrations using python manage.py migrate.
    Start the development server with python manage.py runserver.

#Contributors

    [Rawy Murgany]
    [rawymo@outlook.com]

#License

This project is licensed under the MIT License.
