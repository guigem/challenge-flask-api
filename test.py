from flask import Flask, request

import random

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def alive() -> str:
    '''
    This GET route checks the status of the API

    Returns
    -------
    str
        Return the string "alive".

    '''
    
    return "alive"



@app.route(
    "/predict/<string:month>/<int:customer_visiting_website>/<string:seller_available>",
    methods=["GET"],
)
def user(month: str, customer_visiting_website: int, seller_available: str) -> int:
    '''
    This GET route takes 3 parameters and returns a random number between 2000 and 5000.
    
    Parameters
    ----------
    month : str
        Current month.
    customer_visiting_website : int
        Number of customers visiting the website for a given month.
    seller_available : str
        Name of the seller.

    Returns
    -------
    int
        Random number between 2000 and 5000.

    '''

    random_num = random.randint(2000, 5000)
    random_num = str(random_num)
    return random_num


@app.route("/login", methods=["POST"])
def login() -> str:
    
    '''
    This POST route makes sure that username and password are correct. 
    The request is sent using postman.

    Returns
    -------
    str
        Returns a string with the correct information .

    '''
    
    #Dictionnary with the json request for username and password
    body = {
            'user' : request.json["username"],
            'password' : request.json["password"] }


    return f"Login success for user {body['user']} with password of length: {len(body['password'])}!!"


if __name__ == "__main__":
    app.run(port=5000, debug=False)
