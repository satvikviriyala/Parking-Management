# Parking-Management
# Architecture of the Vehicle Parking App

This document outlines the architecture for the "Vehicle Parking App - V1" project, including the file and folder structure, the responsibilities of each component, how application state is managed, and the interconnectedness of the services.

### File and Folder Structure

A well-organized structure is key for a maintainable Flask application. Here is a recommended structure:

```
VehicleParkingApp/
├── app.py
├── config.py
├── requirements.txt
├── instance/
│   └── database.sqlite3
├── project/
│   ├── __init__.py
│   ├── models.py
│   ├── controllers.py  (or routes.py)
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       ├── admin_dashboard.html
│       └── user_dashboard.html
└── README.md
```

### What Each Part Does

*   **`VehicleParkingApp/`**: The root folder of your project that you will zip for submission.
*   **`app.py`**: The main entry point of your application. This script initializes the Flask application and runs it.
*   **`config.py`**: Contains configuration settings for your application, such as the database URI and any secret keys.
*   **`requirements.txt`**: A list of all Python libraries and dependencies required to run the project (e.g., Flask, Flask-SQLAlchemy).
*   **`instance/`**: A folder that holds instance-specific data that shouldn't be version controlled, like your SQLite database file.
    *   **`database.sqlite3`**: The SQLite database file.
*   **`project/`**: The main package for your application.
    *   **`__init__.py`**: Initializes the `project` package, creates the Flask app object, and sets up extensions.
    *   **`models.py`**: Defines the database schema through classes (models) for `User`, `ParkingLot`, `ParkingSpot`, and `Reservation`.
    *   **`controllers.py` (or `routes.py`)**: Contains the application's routes and view functions that handle requests and render templates.
    *   **`static/`**: Holds static files like CSS, JavaScript, and images that are served directly to the browser.
    *   **`templates/`**: Contains the Jinja2 HTML templates for the application's frontend.

### Where State Lives and How Services Connect

*   **State Management:** The primary state of the application (data about users, parking lots, spots, and reservations) is stored persistently in the **SQLite database (`database.sqlite3`)**. Session state, which keeps track of whether a user is logged in, is managed by Flask's session mechanism, which uses signed cookies on the client-side.

*   **Service Connection Flow:**
    1.  A user interacts with the application through their web browser.
    2.  The browser sends an HTTP request to the Flask application.
    3.  The request is routed to the appropriate view function in `controllers.py` based on the URL.
    4.  The controller function interacts with the database via the models defined in `models.py` to retrieve or store data.
    5.  The controller then renders a Jinja2 template from the `templates/` directory, passing in the necessary data.
    6.  The rendered HTML is sent back to the user's browser as an HTTP response.
    7.  Static files like CSS and JavaScript are requested by the browser and served from the `static/` directory.
