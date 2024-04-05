from urllib import request
from flask import app, jsonify

from src.database.trails_repository import TrailRepository


trail_repository = TrailRepository()
@app.route('/')
def helloworld():
    return "<p>Hello, World! How are you?</p>"

@app.route('/get-trail-details', methods=['GET'])
def get_trail_details():
    data=request.get_json() 
    return jsonify(trail_repository.get_trail_details(data))

@app.route('/get-trails-by-difficulty-rating', methods=['GET'])
def get_trails_by_difficulty_rating():
    data=request.get_json()
    return jsonify(trail_repository.get_trails_by_difficulty_rating(data))

@app.route('/get-trails-by-length')
def get_trails_by_length():
    data=request.get_json()
    return  jsonify(trail_repository.get_trails_by_length(data))