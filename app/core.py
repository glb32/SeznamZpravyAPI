from flask import Flask, url_for, jsonify
import query
import json

app = Flask(__name__)
Q = query.Query()

@app.route('/topstory')
def topstory():
    return(Q.QueryTopStory())

@app.route('/search/<query>/<count>')
def search(query,count=3):
    return(Q.Search(query,int(count)))


if __name__ == '__main__' :
    app.run()
