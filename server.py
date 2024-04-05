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

@app.route('/get-trails-on-difficulty-rating', methods=['GET'])
def get_trails_on_difficulty_rating():
    data=request.get_json()
    difficulty_rating = 7
    if data:
        difficulty_rating = data['difficulty_rating']
    return jsonify(aws_controller.get_trails_on_difficulty_rating(difficulty_rating))

if __name__=='__main__':
    app.run()