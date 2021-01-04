from flask import Flask

import random

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def alive() -> str:

    return "alive"


# @app.route('/login', methods=["POST"])
# def login():


@app.route(
    "/predict/<string:month>/<int:customer_visiting_website>/<string:seller_available>",
    methods=["GET"],
)
def user(month: str, customer_visiting_website: int, seller_available: str) -> int:

    random_num = random.randint(2000, 5000)
    random_num = str(random_num)
    return random_num


if __name__ == "__main__":
    app.run(port=5000, debug=False)
