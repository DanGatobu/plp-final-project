# plp-final-project
This repository contains the source code for a web application that allows farmers to sell their livestock online. The application includes a Learning Management System (LMS) to help farmers learn how to use the platform to sell their livestock more effectively. The web application is written using the Python Django framework.
To Use the wecsite, please visit [Farmy](livestockmarket.vercel.app).

Table of Contents
Getting Started
Installation
Usage

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You will need the following software installed on your system before you can run this application:

Python (version 3.6 or higher)
pip (version 19 or higher)
virtualenv (optional)
Installation
To install the application, follow these steps:

Clone the repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/username/plp-final-project.git
Navigate to the root directory of the project and create a virtual environment (optional):

bash
Copy code
virtualenv env
source env/bin/activate
Install the necessary dependencies using pip:

Copy code
pip install -r requirements.txt
Create a local database for the application:

Copy code
python manage.py migrate
Usage
To start the application, run the following command from the root directory of the project:

Copy code
python manage.py runserver
This will start the server and the application will be available at http://localhost:8000.
