from flask import Flask
import query


app = Flask(__name__)
Q = query.Query(0)

@app.route('/topstory')
def topstory():
    return(Q.QueryTopStoryHeadline())

@app.route('/search/<query>/<count>')
def search(query,count=3):
    return(Q.Search(query,int(count)))

#IMPORTANT: ALWAYS CALL TOPSTORY BEFORE MAKING A CALL TO GETDOCUMENTTEXT()
@app.route('/topstory/more')
def more():
    return(Q.GetDocumentText())

if __name__ == '__main__' :
    app.run()
