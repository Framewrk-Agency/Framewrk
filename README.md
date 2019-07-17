# Framewrk
Questions are the answer.

![Python](https://img.shields.io/badge/Python-3.7-blue.svg?longCache=true&style=flat-square&logo=python&logoColor=white&colorA=4c566a&colorB=5e81ac)
![Flask](https://img.shields.io/badge/Flask-1.0.2-blue.svg?longCache=true&style=flat-square&logo=flask&colorA=4c566a&colorB=5e81ac)
![Flask-WTF](https://img.shields.io/badge/FlaskWTF-0.14.2-blue.svg?longCache=true&style=flat-square&logo=flask&colorA=4c566a&colorB=5e81ac)
![Flask-Login](https://img.shields.io/badge/Flask--Login-0.4.1-blue.svg?longCache=true&style=flat-square&logo=flask&colorA=4c566a&colorB=5e81ac)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-0.12-blue.svg?longCache=true&style=flat-square&logo=flask&colorA=4c566a&colorB=5e81ac)
![Flask-SQLAlchemy](https://img.shields.io/badge/Flask--SQLAlchemy-2.3.2-red.svg?longCache=true&style=flat-square&logo=flask&logoColor=white&colorA=4c566a&colorB=5e81ac)
![Psycopg2-binary](https://img.shields.io/badge/Psycopg2--Binary-v2.7.7-red.svg?longCache=true&style=flat-square&logo=PostgreSQL&logoColor=white&colorA=4c566a&colorB=bf616a)
![Redis](https://img.shields.io/badge/Redis-v3.2.1-red.svg?longCache=true&style=flat-square&logo=Redis&logoColor=white&colorA=4c566a&colorB=bf616a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/Framewrk-Agency/Framewrk.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=GitHub)](https://github.com/Framewrk-Agency/Framewrk/issues)
[![GitHub Stars](https://img.shields.io/github/stars/Framewrk-Agency/Framewrk.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=GitHub)](https://github.com/Framewrk-Agency/Framewrk/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Framewrk-Agency/Framewrk.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=GitHub)](https://github.com/Framewrk-Agency/Framewrk/network)


## Project

* Our app follows Flask's "application factory" method. The 'core' of our app lives within the */framewrk* directory.
* */static* contains all source and production compressed frontend (JS, CSS, etc).
* */templates* contains all "pages" of our app, which are templates which dynamically build themselves at runtime.
* *config.py* holds all basic configuration information.
* Files like *Pipfile*, *Pipefile.lock*, and *requirements.txt* are all related to our Python environment.

### Backend

Framewrk is a web application build using Flask, a micro framework of Python. The choice to use this combination is highly intentional given the goals and aspirations of the product.

#### Core Technology

* The core of Framewrk will come down to executing significant & positive things with data. This makes **Python** an obvious choice.
* Framewrk is likely to grow quickly and adapt to needs faster. When we pair this with a quick-to-market mentality, we have a prime use case for **Flask**. Flask allows us to set up quick, scale effectively, and grants access to countless useful extensions.
* Selecting **MongoDB**, or specifically **MongoDB Atlas** paired with **MongoDB Stitch** offers a lot of advantages off the bat. NoSQL is obviously well suited for products where schemas are subject to change in our growth phase. Moreover, *Stitch* offers plenty of easy *“backend as a service”* features to assist in complex functionality such as user account creation out-of-the-box. As Framewrk matures, we may duplicate or transfer this data to traditional relational databases.
* A few of our Python libraries include:
  * **WTForms**: Handling user form validation and submission.
  * **Flask-FileUpload**: Used to upload files such as audio files by users.
  * **Boto**: Stores said files on an Amazon S3 bucket.
  * **Flask-Login**: Handling user sessions.

#### Architecture

* While initially set up as *Heroku* app, Framewrk is now hosted on *DigitalOcean*.
* We will be running a droplet serving our app as a WSGI app under NGINX.
* Our MongoDB instance is a cloud service existing separately.

### Frontend

The frontend of Framewrk is not based on any particular frontend framework. We use SCSS as a preprocessor, with perhaps a few choice elements extracted from sources here and there (for example, i below the logic for tooltips is a snippet from Bootstrap, but there was never an intention to import the entire Bootstrap library).

#### Techonlogy

* Styles are handled in the SCSS syntax of Sass, utilizing the pysass Python library.
* Styles are bundled upon building the app - we may want to discuss how these bundles are served
