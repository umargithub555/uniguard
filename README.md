# uniguard

Steps to run this project:
1. Download and install python using this link -> https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe
2. Clone this repository in-to your local system.
3. Make an environment env using "python -m venv env".
4. Install the requirement.txt using "pip install -r requirement.txt".
5. Make a .env file in the root directory having these " DATABASE_URL="postgresql://postgres:pgsql@localhost/uniguard"
JWT_SECRET_KEY=eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTc0MDE1MzM3MCwiaWF0IjoxNzQwMTUzMzcwfQ.k5w_dCs2X-5kskO53fhJlQte5rqrswtasme0QPotcjk "
6. Run the backend using "uvicorn app.main:app --reload".
