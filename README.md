## Prerequisites

Make sure you have the following installed on your machine:

- Python (3.x recommended)
- pipenv (Python package and virtual environment manager)
- Git

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/taqiyaehsan/AcaiLibraryApp.git
   cd LibraryApp
   ```
2. **Create a Virtual Environment:**

   ```bash 
   pipenv install --dev
   ```

3. **Activate the Virtual Environment:**

     ```bash
     pipenv shell
     ```

4. **Install Dependencies:**

   ```bash
   pipenv install requirements.txt
   ```

5. **Apply Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set a username, email, and password for the superuser.

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The application should be accessible at http://localhost:8000/

8. **Access the Admin Interface:**

   - Navigate to http://localhost:8000/admin/ and log in with the superuser credentials created earlier.


## User Registration

To register a new user, follow these steps:

1. **Run the Development Server:**

``` bash
python manage.py runserver
```

2. Open your web browser and navigate to http://localhost:8000/register/ 

3. Fill out the registration form with the required information.

4. Click the "Register" button to create a new user.


## User Login

To log in as a registered user:

1. Navigate to http://localhost:8000/login/

2. Enter your username and password.

3. Click the "Login" button to access your account.
   

## Additional Features

- Visit the Library List page at http://localhost:8000/library/library/ to see a list of books and their availability.
- View user list on http://localhost:8000/library/users/
- Use the admin interface to manage users, books, and other application data.
- GET a JSON list of books from http://localhost:8000/library/api/books/ with optional limit parameter http://localhost:8000/api/books/?limit=5 
- Checkout a book from http://localhost:8000/library/api/checkout/ by entering book ID as {"book_id": 1} (replace the number according to desired book to be checked out)

## Contributing

Feel free to contribute to the development of this application. Create a new branch, make your changes, and submit a pull request.

```
