# Lucke Project
### _"Memory is the foundation of personal identity."_
_John Locke_

---
## Table of Contents
1. [Purpose of the Project](#1-purpose-of-the-project)
2. [User Stories](#2-user-stories)
3. [Features](#3-features)
4. [Future Features](#4-future-features)
5. [Typography and Color Scheme](#5-typography-and-color-scheme)
6. [Wireframes](#6-wireframes)
7. [Technology](#7-technology)
8. [Testing](#8-testing)
    1. [Code Validation](#81-code-validation)
    2. [Test Cases (User Story Based with Screenshots)](#82-test-cases-user-story-based-with-screenshots)
    3. [Fixed Bugs](#83-fixed-bugs)
    4. [Supported Screens and Browsers](#84-supported-screens-and-browsers)
9. [Deployment](#9-deployment)
    1. [Via Heroku](#91-via-heroku)
    2. [Via GitHub](#92-via-github)
10. [Credits](#10-credits)

## 1. Purpose of the Project
The Lucke project is a web application that allows users to sign up, sign in, and write diaries on their personal pages. Inspired by the philosopher John Locke, who emphasized the importance of memories, this project aims to provide a personal space for users to store and reflect on their thoughts and experiences.

## 2. User Stories
### User Registration and Authentication
- As a user, I want to sign up with my username and password so that I can create an account.
- As a user, I want to log in with my username and password so that I can access my account.


### Diary Management
- As a user, I want to write daily diary entries so that I can record my thoughts and experiences.
- As a user, I want to post my diary entries so that they are visible on my timeline.
- As a user, I want to view my previous diary entries so that I can reflect on my past experiences.
- As a user, I want to edit my diary entries so that I can update my thoughts and experiences.
- As a user, I want to delete my diary entries so that I can remove unwanted entries. 
- As a user, I want to Side Note on my own entries so that I can add additional thoughts.

## 3. Features
- User registration and authentication
- Personal diary page for each user
- Diary entry creation, posting, editing, and deletion
- Date modification for diary entries

## 4. Future Features
- Adding a comments section for users to interact with each other's entries
- Integrating an image generator to include pictures with diary entries
- Advanced search and filtering options for diary entries
- Mobile social app version of the platform

## 5. Typography and Color Scheme
- **Typography:** The project uses Bootstrap's default typography for consistency and readability.
- **Color Scheme:** A simple and clean color scheme is used, primarily leveraging Bootstrap's default color classes.


## 6. Wireframes
(To be created)

## 7. Technology
### Work Environments and Hosting
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [Lucid](https://lucid.app/) (ERD diagrams)
### Python Libraries
- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [decouple](https://pypi.org/project/python-decouple/) (store parameters in in .env files)
### Django Libraries
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [Whitenoise](https://whitenoise.evans.io/en/latest/) (used for serving static files)
### Database
- [ElephantSQL](https://www.elephantsql.com/) (used for serving static files)
### Frontend
- HTML
- CSS
- Bootstrap (4.5.2 Library)
- JavaScript
- Jquery (Librariy)


## 8. Testing

### 8.1 Code Validation
- HTML, CSS, and JavaScript code validated using W3C validators
- Python code checked with PEP8 guidelines

### 8.2 Test Cases (User Story Based with Screenshots)
- User registration
  ![User Registration](screenshots/user_registration.png)
- User login
  ![User Login](screenshots/user_login.png)
- Diary entry creation
  ![Diary Entry Creation](screenshots/diary_entry_creation.png)
- Edit Diary Entry
  ![Edit Diary Entry](screenshots/Edit_Diary_Entry.png)
- Delete Diary Entry
  ![Delete Diary Entry](screenshots/Delete_Diary_Entry.png)
- Add a SideNote
  ![Add a SideNote](screenshots/add_sidenote.png)  


### 8.3 Fixed Bugs
- **Circular Import Issue in `models.py`:**
  - **Issue:** There was a circular import issue caused by importing the `Diary` model at the beginning of the file which resulted in `ImportError: cannot import name 'Diary' from partially initialized module 'diary.models'`.
  - **Solution:** The solution was to refactor the imports and ensure that the `Diary` model was not causing a circular dependency, and modifing the import statements to only import necessary components at the right places.

- **NoReverseMatch Error for `request.user`:**
  - **Issue:** Encountered a `NoReverseMatch` error when trying to access `request.user` in the URL pattern.
  - **Solution:** The solution was to use the correct URL patterns and ensure that `request.user` is handled properly within the context of the view.

- **AJAX Handling for Sidenote Additions:**
  - **Issue:** The `is_ajax` method was deprecated in Django 4.0, causing the AJAX request handling to fail.
  - **Solution:** Updated the AJAX handling to use `request.headers.get('x-requested-with') == 'XMLHttpRequest'` instead of `request.is_ajax()`.


### 8.4 Supported Screens and Browsers
- Fully responsive design tested on various devices and screen sizes
- Compatible with major browsers: Chrome, Firefox, Safari, Edge

## 9. Deployment

###  Via Heroku
#### Installing libraries
- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip3 install dj_database_url pyscopg2``
- Install **Whitenoise** (prevent issues with Heroku not rendering custom stylesheet): ``pip3 install whitenoise``

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name app appropriately and choose relevant region, then click **Create App**

#### Environment Variables

- For local deployment, you will need to create a `.env` file in the root directory of the project and set the environment variables in this file.
- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.
- You need to define the following variables:
  - If using a Postgres database:
    - `DATABASE_URL` - the URL for your Postgres database.
    - `NAME` - the name of your database.
    - `USER` - the username for your database.
    - `PASSWORD` - the password for your database.
    - `HOST` - the host for your database.
    - `PORT` - the port for your database.
  - Django settings:
    - `SECRET_KEY` - the secret key for your Django project.
    - `DEBUG` - set to `True` for development, `False` for production.

#### Connecting Heroku to Database

- In Heroku dashboard, go to **Settings** tab
- Add new config vars **DATABASE_URL** (value is database URL), **SECRET_KEY** (value is secret key string)


#### Allow Heroku as host

- In ``settings.py`` add
    ````
    ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
    ````

## 10. Credits
- **Project Name Inspiration**: The English philosopher "_John Locke_". Check the [Article](https://plato.stanford.edu/entries/locke-personal-identity/) 
- **Libraries and Tools**: Django, Heroku, GitHub
- **AI Tools** [_ChatGPT_](https://openai.com/chatgpt)
- **Project Guidance and Support** [_Code Institute_](codeinstitute.net/)
- **Development**: "_Tariq Safieh 2024_" All Copyrights Reserved

---





