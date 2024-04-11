from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import aws_controller

app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def helloworld():
    return "<p>Hello, World! How are you?</p>"

@app.route('/get-trail-details', methods=['GET'])
@cross_origin()
def get_trail_details():
    state_name=request.args.get('state_name')
    trail_id=request.args.get('trail_id')
    return jsonify(aws_controller.get_trail_details(state_name, trail_id))

@app.route('/get-trails-by-difficulty-rating', methods=['GET'])
@cross_origin()
def get_trails_by_difficulty_rating():
    state_name=request.args.get('state_name')
    difficulty_rating=request.args.get('difficulty_rating')
    return jsonify(aws_controller.get_trails_by_difficulty_rating(difficulty_rating, state_name))

@app.route('/get-trails-by-length', methods=['GET'])
@cross_origin()
def get_trails_by_length():
    state_name=request.args.get('state_name')
    length=request.args.get('length')
    return  jsonify(aws_controller.get_trails_by_length(length,state_name))

@app.route('/get-trails-by-rating', methods = ['GET'])
@cross_origin()
def get_trails_by_rating():
    data=request.get_json()
    return jsonify(aws_controller.get_trails_by_rating(data))

if __name__=='__main__':
    app.run()