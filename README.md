# Hymnal Django Project

## Project Description
Hymnal is a simple web application built with Django that serves as a digital hymnal. It allows users to browse a collection of hymns, view hymn details including lyrics and author information, and supports Progressive Web App (PWA) features for an enhanced user experience.

## Features
- Browse a list of hymns with a search filter.
- View detailed hymn information including lyrics, author, and optional audio.
- About page describing the project.
- PWA support for offline usage and installation on devices.
- Admin interface for managing hymns.

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Hymnal
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the hymnal.

## Usage
- Use the search bar on the home page to filter hymns by title.
- Click on a hymn title to view its details.
- Visit the About page for information about the project.
- Access the Django admin interface at `/admin/` to manage hymns.

## Technologies Used
- Django 5.0
- SQLite (default database)
- HTML, CSS, JavaScript for frontend
- Progressive Web App (PWA) support via django-pwa

## Project Structure
- `core/`: Main Django app containing models, views, templates, static files, and URL routing.
- `Hymnal/`: Project configuration including settings and URL routing.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django management script.

## PWA Support
This project includes Progressive Web App features such as a service worker and app manifest, allowing users to install the app on their devices and use it offline.

## License
This project is licensed under the MIT License.
