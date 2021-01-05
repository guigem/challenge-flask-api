#Saying that we will be using python in your methods
FROM python:3.7

#Creating a folder "app" to store all the files in the container
RUN mkdir /app

#Copying all the files to the container
COPY . app/

#Starting in "app"
WORKDIR /app

#Installing all the libraries from "requirements.txt"
RUN pip install -r requirements.txt

#The action is to run "api.py"
CMD ["python", "api.py"]
