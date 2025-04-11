from flask import Flask, request, escape #escape safely encodes user inputs to prevent injection, but not best for URLs
from flask import jsonify
from urllib.parse import quote #this is an alternative to escape as it is designed for parameters
import requests #import python requests library

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello World Part 5")


@app.route('/health', methods=["GET", "POST"])
def health():
    if request.method =="GET":
        return jsonify(status="OK", method="GET"), 200
    
    if request.method =="POST":
        return jsonify(status="OK", method="POST"), 200

@app.route('/values')
def values():
    course = request.args["course"]
    rating = request.args.get("rating")

    return {"message": f"{course} with rating {rating}"}
#to run: http://localhost:5000/values?course=Ste&rating=100

@app.route('/lookup')
def get_author():
    # use the requests library to look up an external API OpenLibrary for auther and return the resonse in variable res
    res = requests.get("https://openlibrary.org/search/authors.json?q=Michael%20Crichton")
    if res.status_code == 200:
        return {"message": res.json()} #json needs to be lower case
    elif res.status_code ==404:
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server Error!"}, 500

@app.route('/book/<isbn>')
def get_book(isbn):
    # use the requests library to look up an external API OpenLibrary foruser inputted ISBN
    safe_isbn = quote(isbn) #uses urllib.parse to prevent injection
    book = requests.get(f"https://openlibrary.org/isbn/{safe_isbn}.json") #json needs to be lower case
    if book.status_code == 200:
        return {"message": book.json()} #json needs to be lower case
    elif book.status_code ==404:
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server Error!"}, 500

#eg ISBM 1449355730