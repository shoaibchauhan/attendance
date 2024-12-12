Clone the repository:
git clone https://github.com/shoaibchauhan/attendance.git

Configure the database (PostgreSQL is used):
Update the DATABASES settings in the settings.py file to point to your PostgreSQL database.

Run migrations:
python manage.py makemigrations
python manage.py migrate

Start the FastAPI application:

uvicorn main:app --reload
Test the API endpoints using Swagger UI by navigating to /docs in your browser:


Due to time constraints, I have created a simple README instead of a more detailed one.
