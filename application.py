from flask import Flask, redirect, jsonify, request, abort
from zgameDAO import gameDAO
app = Flask(__name__, static_url_path='', static_folder='.')


#@app.route('/')
#def index():
    #return (404)

#curl "http://127.0.0.1:5000/games"
@app.route('/games')
def getAll():
    results = gameDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/games/2"
@app.route('/games/<int:id>')
def findById(id):
    foundGames = gameDAO.findByID(id)
    return jsonify(foundGames)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"The Outer Worlds\",\"Developer\":\"Obsidian Entertainment\",\"Price\":50}" http://127.0.0.1:5000/games
@app.route('/games', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    # other checking 
    game = {
        "Title": request.json['Title'],
        "Developer": request.json['Developer'],
        "Price": request.json['Price'],
            }
    values = (game['Title'],game['Developer'],game['Price'])
    newID = gameDAO.create(values)
    game['id'] = newID
    
    return jsonify(game)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Price\":123}" http://127.0.0.1:5000/games/1
@app.route('/games/<int:id>', methods=['PUT'])
def update(id):
    foundGame = gameDAO.findByID(id)
    if not foundGame:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundGame['Title'] = reqJson['Title']
    if 'Developer' in reqJson:
        foundGame['Developer'] = reqJson['Developer']
    if 'Price' in reqJson:
        foundGame['Price'] = reqJson['Price']
    values = (foundGame['Title'],foundGame['Developer'],foundGame['Price'], foundGame['id'])
    gameDAO.update(values)
    return jsonify(foundGame)
        

    

@app.route('/games/<int:id>' , methods=['DELETE'])
def delete(id):
    gameDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= False)