# Daily Jotter - A Flask Web Application 📝

Welcome to Daily Jotter! This is a simple, clean, and functional web application built with Python and Flask that allows users to write, save, and view their daily diary entries. This project was built to demonstrate a fundamental understanding of full-stack web development, from backend logic and database management to frontend presentation.
## ✨ Features

*   **Create Entries:** A clean and simple form to write and save new diary entries with a title and content.
*   **Automatic Timestamps:** Every entry is automatically timestamped with the exact date and time it was created.
*   **View All Entries:** A dedicated page that dynamically displays all past entries in a clean, card-based layout, sorted with the newest entry first.
*   **Persistent Storage:** Entries are permanently saved in a robust SQLite database.
*   **User-Friendly Flow:** Clear navigation, including a success confirmation page after an entry is saved and links to move between the entry form and the viewing page.
*   **Delete Entries (Coming Soon/Optional):** The application can be extended with a feature to delete entries.

---

## 🛠️ Technology Stack & Tools

This project utilizes a range of modern web technologies:

*   **Backend:**
    *   **Python:** The core programming language.
    *   **Flask:** A lightweight and flexible web framework for routing and handling requests.
    *   **SQLAlchemy & Flask-SQLAlchemy:** For Object-Relational Mapping (ORM), allowing for easy interaction with the database using Python objects instead of raw SQL.
    *   **SQLite:** A self-contained, serverless database, perfect for small to medium-sized applications.

*   **Frontend:**
    *   **HTML5:** For the structure and content of the web pages.
    *   **CSS3:** For styling the application to be clean and user-friendly.
    *   **Jinja2:** A powerful templating engine used with Flask to dynamically generate HTML and display data from the backend.

*   **Development Environment:**
    *   **Virtual Environment (`venv`):** To manage project dependencies in an isolated environment.
    *   **Git & GitHub:** For version control and code hosting.

---

## 🚀 Getting Started & Local Setup

To run this project on your local machine, please follow these steps:

### Prerequisites
*   Python 3.x installed on your system.
*   `pip` (Python package installer).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    *   **On Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    The `requirements.txt` file contains all the necessary libraries.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    This is a one-time command to create the `data.db` file and the necessary tables.
    
    *   Start the Python interactive shell:
        ```bash
        python
        ```
    *   Run the following commands inside the shell:
        ```python
        from app import app, db
        with app.app_context():
            db.create_all()
        exit()
        ```
    This will create a `data.db` file inside an `instance` folder.

5.  **Run the application:**
    ```bash
    python app.py
    ```

6.  Open your web browser and navigate to `http://127.0.0.1:5000` to see the application in action!

---