
# Social Media API

A RESTful Social Media API built using Python, Django, and Django REST Framework.

## Features

- User Registration
- Token Authentication
- Create, List, Update and Delete Posts
- User Post Wall
- Create and List Comments
- Like and Unlike Posts
- Follow and Unfollow Users
- Followers and Following Lists
- View and Update User Profile
- Post Ownership Authorization

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Token Authentication

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Muhammed-anzil/social-media-api-.git
cd social-media-api-
```

### 2. Create a virtual environment

```bash
python -m venv apienv
```

Activate on Windows:

```powershell
.\apienv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/register/` | Register user |
| POST | `/login/` | Obtain authentication token |
| POST | `/postcreate/` | Create post |
| GET | `/post/` | List posts |
| GET, PUT, PATCH, DELETE | `/post/<id>/` | Retrieve, update or delete post |
| POST | `/comment/<id>/` | Create comment |
| GET | `/listcomment/<id>/` | List comments |
| GET, POST | `/like/<id>/` | List or create likes |
| DELETE | `/unlike/<id>/` | Unlike a post |
| POST | `/follow/` | Follow a user |
| GET | `/listfollow/` | List following |
| GET | `/followers/` | List followers |
| GET, PATCH, PUT | `/profile/` | View or update profile |
| GET | `/myposts/` | View your posts |

## Authentication

Use the token obtained from `/login/` to access protected endpoints.

In Postman, select **Authorization → Bearer Token** only if your API expects Bearer authentication; otherwise use the token format configured by your Django REST Framework TokenAuthentication setup.

## Author

Developed as a Django REST Framework learning project.
