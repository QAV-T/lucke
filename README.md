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
![new-user](/Readme/welcome_page.png)
![new-user](/Readme/new_user.png)
- As a user, I want to log in with my username and password so that I can access my account.
![new-user](/Readme/new_user-login.png)
![new-user](/Readme/new_user-profile-two.png)
- As a user, I want to read more about the project idea and potential, so that I understand more the concept and the motive.
![new-user](/Readme/about.png)


### Diary Management
- As a user, I want to write daily diary entries so that I can record my thoughts and experiences.
![new-user](/Readme/new_user-first-diary.png)
- As a user, I want to post my diary entries so that they are visible on my timeline.
![new-user](/Readme/new_user-profile.png)
- As a user, I want to view my previous diary entries so that I can reflect on my past experiences.
![new-user](/Readme/new_user-diary.png)
- As a user, I want to edit my diary entries so that I can update my thoughts and experiences.
![new-user](/Readme/new_user-first-edit.png)
![new-user](/Readme/new_user-after-first-edit.png)
- As a user, I want to delete my diary entries so that I can remove unwanted entries. 
![new-user](/Readme/new_user-delete.png)
- As a user, I want to Side Note on my own entries so that I can add additional thoughts and reflect on diaries.
![new-user](/Readme/new_user-first-sidenote.png)
![new-user](/Readme/new_user-after-first-edit.png)

## 3. Features
- User registration and authentication
- Personal diary page for each user
- Diary entry creation, posting, editing, and deletion
- Date modification for diary entries
- User abelity to write unlimited sidenotes for each diary.

## 4. Future Features
- Integrating an image generator to include pictures with diary entries
- Advanced search and filtering options for diary entries
- Mobile social app version of the platform
- Adding a comments section for users to interact with each other's entries

## 5. Typography and Color Scheme
- **Typography:** Using Bootstrap's default typography for consistency and readability. The application leverages Bootstrap's well-designed typography system to ensure that all text elements are clear, legible, and visually appealing. This includes headings, paragraphs, and other text elements that are styled for optimal readability across different devices and screen sizes.
- **Color Scheme:** The application uses a warm combination of colors to create a warm and cozy feeling of a safe place to write down the diaries. The color palette is carefully chosen to evoke feelings of comfort and security, encouraging users to freely express their thoughts and emotions. This includes soft, warm tones for the background and accents that provide a harmonious and inviting interface.
- **UI:** The user interface combines warm colors to create a cozy atmosphere, making it feel like a safe place to write down diaries. The design includes simple blocks to navigate and a timeline to give users an overview of their diaries. The navigation blocks ensure that users can easily access different sections of the application, while the timeline provides a visual representation of their diary entries, helping them keep track of their writing journey in a structured and intuitive way.

### 6. Entity Relationship Diagram
### Database Model

The database model diagram was designed using [Lucidchart](https://lucid.app/lucidchart/94e7f6d5-55c3-4ce2-ba36-828086a6c315/edit?invitationId=inv_29bacae7-7749-4820-912d-b49fb0e8ffc6&page=0_0#).

![ERD](/Readme/ERD,%20Diary%20.jpeg)
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
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Used to control forms)
- [Whitenoise](https://whitenoise.evans.io/en/latest/) (Used for serving static files)
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
#### HTML, CSS, code validated using W3C validators
#### HTML:
**Home page**

No errors or warnings to show.

**Login page**

No errors or warnings to show.

**Login\logout page**

No errors or warnings to show.

**Sign up page**

No errors or warnings to show.

**Create diary page**

No errors or warnings to show.

**Delete diary page**

No errors or warnings to show.

**Diary edit page**

No errors or warnings to show.

**Profile page**

No errors or warnings to show.

**Side note list page**

No errors or warnings to show.

**Base page**

No errors or warnings to show.

**About page**

No errors or warnings to show.

#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

No error found.

![css](/Readme/css-validation.png)

#### Python [CI Python Linter](https://pep8ci.herokuapp.com/) code checked with PEP8 guidelines
All Python files been checked **admin.py**, **forms.py**, **models.py**, **urls.py**, **views.py**, **settings.py** and **lucke/urls.py**

- I found errors related to trailling whitespaces, blank lines and newlines at the end of the file. All the errors been fixed accordingly.

![python validation](/Readme/admin-py.png)
![python validation](/Readme/lucke-views-py.png)
![python validation](/Readme/models-py.png)

### 8.2 Test Cases (User Story Based with Screenshots)
- User registration
 ![new-user](/Readme/new_user.png)
- User registration username error
![username error](/Readme/user_matching-error.png)
- User registration password error
![password error](/Readme/password_matching-error.png)
- User login
![user login](/Readme/new_user-login.png)
- Login error
![user login error](/Readme/new_user-login-error.png)
- New user profile
![new user profile](/Readme/new_user-first-page.png)
- Diary entry creation
  ![Diary Entry Creation](/Readme/new_user-profile.png)
- Edit Diary Entry
  ![Edit Diary Entry](/Readme/new_user-first-edit.png)
- Delete Diary Entry
  ![Delete Diary Entry](/Readme/new_user-delete.png)
- Add a SideNote
  ![Add a SideNote](/Readme/new_user-diary.png)  


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





