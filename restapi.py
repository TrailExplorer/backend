from flask import Flask, jsonify, request
import aws_controller

app=Flask(__name__)

@app.route('/')
def helloworld():
    return "<p>Hello, World! How are you?</p>"

@app.route('/get-trail-details', methods=['GET'])
def  get_items():
    data=request.get_json() 
    return jsonify(aws_controller.get_items(data))


if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)