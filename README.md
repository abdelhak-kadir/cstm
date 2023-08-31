# Table of Contents
* Description
* Directories and Files
* Usage
* Contributors
* License
# CSTM (comptoire service transport et massagerie)
The project aims to modernize and optimize freight services by integrating suitable digital technologies. This will enhance the customer experience, streamline operations, and strengthen competitiveness in the transportation and freight industry.

# Project structure
 List the main directories and files in your project with their descriptions:
* **account/:** Contains the files related to project.
    - **migrations/:** Stores database migration files.
    - **templates/account/:** Contains templates for account-related views.
    - **__init __.py:** Initialization file for the account app.
    - **admin.py:** Configuration for the admin interface related to accounts.
    - **apps.py:** App configuration for the account app.
    - **forms.py:** Contains forms for user input.
    - **models.py:** Defines the database models for user accounts.
    - **tests.py:** Unit tests for the account app.
    - **urls.py:** Defines URLs and routing for the account app.
* **photos/2023/:** Contains photo-related files for the year 2023.
* **static/:** Contains static files such as stylesheets, scripts, and images.
* **trans/:** Contains files related to trans.
    - **.env:** Environment configuration file.
    - **__init__ .py:** Initialization file for the trans app.
    - **asgi.py:** ASGI configuration for the trans app.
    - **settings.py:** Project settings for the trans app.
    - **urls.py:** URL routing for the trans app.
    - **wsgi.py:** WSGI configuration for the trans app.
* **.gitignore:** Specifies files and directories to be ignored by Git.
* **db.sqlite3:** SQLite database file.
* **manage.py:** Django management script.
* **requirement.txt:** Lists the project's dependencies.
* **README.md:** This file, providing an overview of the project and its structure.

# Running the project
To run the project, follow these steps:
* upgrade pip install :
   > `pip install upgrade`
* install `python 3.11`
* Clone the Repository:
   > `git clone <repository_url>`

   > `cd <project_directory>`
* Set Up Virtual Environment :
   > `python3 -m venv venv`

   > `source venv/bin/activate`
* Install Dependencies:
   >` pip install -r requirement.txt`
* Apply Migrations: 
  > `python manage.py makemigrations`

  > `python manage.py migrate`




