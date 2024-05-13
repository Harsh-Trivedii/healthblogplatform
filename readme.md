# Health Blog Platform

## Setup Instructions

### Prerequisites
- Python 
- Django 

### Installation Steps


1. **Install Django:**
   - Install Django using pip:
     ```
     pip install django
     ```

2. **Run Migrations:**
   - Apply database migrations to set up the database schema:
     ```
     python manage.py migrate
     ```

3. **Start the Development Server:**
   - Launch the Django development server:
     ```
     python manage.py runserver
     ```

4. **Access the Application:**
   - Open a web browser and go to `http://127.0.0.1:8000/` to access the Health Blog Platform.

5. **Create Superuser (Optional):**
   - If you want to access the Django admin interface, create a superuser account:
     ```
     python manage.py createsuperuser
     ```
     Follow the prompts to create a superuser account.
