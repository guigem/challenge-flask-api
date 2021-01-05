# challenge-flask-api

#### BeCode challenge: January 2021

#### Contributors: Guillaume Gémis

## Aim of this project

The aim of this challenge is to create an functional API using [Flask](https://flask.palletsprojects.com/en/1.1.x/ "Title") and deploy it on the platform [Heroku](https://www.heroku.com/ "Title"). 
The API has three different routes that can be exploited: 

- */status:* this GET route returns the world **Alive** when the access with the API is correct and functional.

- */predict/month/customer_visiting_website/seller_available:* this GET route takes 3 parameters: a given month, the number of customers who visit the website during that specific month and the name of the seller available. This function returns a **random number** from 2000 to 5000. 

- */login:* this POST route returns a sentence that highlights the username and the length of the password of the user. Due to the lack of a form that could get these two information, we decided to mock them using [Postman](https://www.postman.com/ "Title"). 

Once those routes were built, our API was stored in a [Docker container](https://www.docker.com/ "Title") and deployed on [Heroku](https://www.heroku.com/ "Title").

## Result

The result of this work can be checked by clicking on this [link](https://challenge-flask-api-guigem.herokuapp.com/status "Title"). 

## Repository content

- [api.py](./api.py "Title"): main file written in Python that creates the API an its three routes.

- [requirement.txt](./requirement.txt "Title"): list of libraries needed for the container and the deployment (see below for the list).

- [Dockerfile](./Dockerfile "Title"): instructions to build and run the container.

- [Procfile](./Procfile "Title"): code to indicate to Heroku what to display

## Installation 

In order to run and launch this project, [Flask](https://flask.palletsprojects.com/en/1.1.x/ "Title") must be installed: 
```
$ pip install Flask 
```
It is then just required to run [api.py](./api.py "Title") and the api should be active localy ([on port 5000](127.0.0.1:5000/status "Title").
As a reminder the deployed version can be found [here](https://challenge-flask-api-guigem.herokuapp.com/status "Title").




