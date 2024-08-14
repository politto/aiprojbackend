from flask import Blueprint, request, jsonify
from service.service import predict_emotion, predict_fallacy

blueprint = Blueprint('ai', __name__)

@blueprint.route('/predictemotion', methods=['POST'])
def predict_emotion():
    data = request.json
    result = predict_emotion(data)
    return jsonify({'result': result}), 200

def predict_fallacy():
    data = request.json
    result = predict_fallacy(data)
    return jsonify({'result': result}), 200

@blueprint.route('/', methods=['GET'])
def test():
    return jsonify('Hello!', 200)



    

