# Flask API about recipes
import flask
import json
from flask import request, jsonify
from datetime import datetime

# App is a Flask object.
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Welcome- Recipes
@app.route('/', methods=['GET'])
def welcome():
    # returning recipes
    return "<h1>Welcome to Recipes!</h1><p>This is a recipe list over how to get via a API using Flask.</p>"

# READ - GET
@app.route('/lunch', methods=['GET'])
def getRecipes():
    with open('ingredients.json', 'r') as ingredientFile:
        ingredientList = json.loads(ingredientFile.read())
        
        expiredIngredients = []
        expiredBestIngredients = []
        for item in ingredientList['ingredients']:
            useBy = datetime.strptime(item['use-by'], "%Y-%m-%d")
            bestBefore = datetime.strptime(item['best-before'], "%Y-%m-%d")
            present = datetime.now()
            if(useBy.date() < present.date()):
                expiredIngredients.append(item['title'])
            elif(useBy.date() > present.date() and bestBefore.date() < present.date()):
                expiredBestIngredients.append(item['title'])

    with open('recipes.json', 'r') as recipeFile:
        recipeList = json.loads(recipeFile.read())
        for i, item in enumerate(recipeList['recipes']):
            if (set(item['ingredients']) & set(expiredIngredients)):
                recipeList['recipes'].pop(i)
            elif (set(item['ingredients']) & set(expiredBestIngredients)):
                recipeList['recipes'].append(recipeList['recipes'].pop(i))
    return jsonify(recipeList), 200

#BONUS - ERROR HANDLING
@app.errorhandler(404)
def notFound(error=None):
    return jsonify({"error": "Sorry we don't recognize this endpoint"}), 404

app.run()