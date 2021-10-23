# MOOVE ASSESSMENT API (a django web API to manipulate applicant data)

<hr/>

![https://ibb.co/c83RpL4](https://i.ibb.co/PWjJbQq/default-rest.png)

<hr/>

# Full Name: Peter Aderibigbe Oluwaseun

<hr/>

## Introduction

This is a finished solution to the test as stated in the mail i received. This API exposes **five (5) endpoints** which
includes:

- Getting lists of all applicants
- Retrieve a single applicant record
- Create new applicant
- Update existing applicant
- Delete existing applicant

## Features

The feature included in this completed test include:

- Django admin page
- Swagger UI and Redoc UI documentation pages
- Prepopulated data

## Installation

Installing this project locally to your developemnt machine is preety simple and straightforward

### Prerequisites

Ensure you have **git**, **python interpreter**, **pip**, and **activated VIRTUAL ENVIRONMENT** fully setup on your
machine

#### Steps

1. Activate your virtual environment
2. Clone this repository

```
git clone https://github.com/adepeter/moove-dj-assessment
```

4. Change into this cloned directory

```
cd moove-dj-assessment
```

5. Install are required dependencies or packages (important: Ensure your virtual environment is activated)

```
pip install -r requirements.txt
```

6. Run makemigrations

```
python manage.py makemigrations
python manage.py migrate
```

7. Load prepopulated data into the database

````
python manage.py loaddata db.json
````

8. Run development server

````
python manage.py runserver
````

### Documentation URL Previews

Once confirmed that development server is active and running, fire up your browser and input the address below:

* **Swagger UI doc URL:** _[127.0.0.1:8080/docs/swagger/](https://127.0.0.1:8000/docs/swagger/)_
* **Redoc UI doc URL:** _[127.0.0.1:8080/docs/redoc/](https://127.0.0.1:8000/docs/redoc/)_

### Authenticating API and Admin page

This API uses three method of authentication to authenticate restrict session which involves data modification to the
backend. To allow acces, easiest and basic authentication is to login the admin by using the url below and supplying the
stated credentials.

* **Django Admin URL:** _[127.0.0.1:8080/admin](https://127.0.0.1:8000/admin)_
* **Token:** _2eeb62f783d65d11c752cb28fd6c63dd3e258053_
* **Username:** *test*
* **Password:** *test*

### Django Test Pass

Passing tests - 100%

### Screenshots

![https://ibb.co/F6zGCTN](https://i.ibb.co/D4Q3T2s/moove-admin-menu.png)
![https://ibb.co/60pNBZ2](https://i.ibb.co/k2rM1yp/redoc-ui.png)
![https://ibb.co/DbCHGcN](https://i.ibb.co/598gYpd/swagger-ui.png)
