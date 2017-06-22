# miNyl - helping you listen to GOOD music

Is your vinyl record collection getting the best of you? miNyl is a web app for music lovers that helps you manage your analog collection in this "21st Century Digital World" (you got that reference, right?). Search for songs in your collection and keep track of all those records you gotta have. miNyl, helping you listen to GOOD music.

#### Checkout [miNyl](http://www.williamocaldwell.com/minylclient/)!

## This is the miNyl Django RESTful API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django and REST framework:
```
pip install django
pip install djangorestframework
```

### Installing

Clone repo:
```
git clone https://github.com/wocaldwell/minyl-backend
```
Setting up the database:
```
./damnit_django.sh 
```
### Special Note
One of the views in this API is being used to serve environment variables to another app residing on the same VPS. Therefore, there are some superfluous (to this project) ENVs that need to be included in your environment in order for the code to run properly.
```
nano ~/.zshrc
```
(or `/.bashrc`, or `/.bash_profile`)and add the following lines ot the bottom of the file.
```
export FIREBASEURL=""
export GOOGLEKEY=""
export WEATHERKEY=""
export WEATHERREF=""
```
then press `control + x` to exit, `y` to confirm the changes and then `return` to write to the file. Now you should be all set to fire up the server.

### Start Server Locally
Run project in the CLI:
```
python manage.py runserver
```
The API should now be ready for consumption by the [miNyl AngularJS client](https://github.com/wocaldwell/minyl-frontend).

### Running the tests
No testing suites included in this project.

### Deployment
No additional resources required.
### Built With

* [Python](http://www.dropwizard.io/1.0.2/docs/) - Main Language
* [Django](http://www.dropwizard.io/1.0.2/docs/) - The framework used
* [pip](https://maven.apache.org/) - Dependency Management


### Authors

* **William Caldwell** - [wocaldwell](https://github.com/wocaldwell)


### Acknowledgments
"Thank you all and GOOD NIGHT!" - Every Musician Ever