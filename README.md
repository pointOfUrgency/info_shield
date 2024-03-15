This back-end side one of my project. I have created API that provides next opportunities: get all existing content, get all existing content by ID, create new content (for admins), get ID of current user, 
register new users and log in and log out.

How to run it locally I will tell below:

Create virtual environment 

Import there all dependencies from requirements.txt

Organize DB stuff (I used postgres)

Use command in concole:

uvicorn main:app --reload

add /docs to url to test all endpoints
