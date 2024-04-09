from flask import Flask, jsonify, request
import aws_controller

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "<p>Hello, World! How are you?</p>"

@app.route('/get-trail-details', methods=['GET'])
def get_trail_details():
    data=request.get_json() 
    return jsonify(aws_controller.get_trail_details(data))

@app.route('/get-trails-by-difficulty-rating', methods=['GET'])
def get_trails_by_difficulty_rating():
    data=request.get_json()
    return jsonify(aws_controller.get_trails_by_difficulty_rating(data))

@app.route('/get-trails-by-length')
def get_trails_by_length():
    data=request.get_json()
    return  jsonify(aws_controller.get_trails_by_length(data))

@app.route('/get-trails-by-rating', methods = ['GET'])
def get_trails_by_rating():
    data=request.get_json()
    return jsonify(aws_controller.get_trails_by_rating(data))


if __name__=='__main__':
    app.run()