from flask import jsonify, request, render_template
from lyrica import lyrica, db
from lyrica.helpers import helper

# Test page, to check if app is running.
@lyrica.route('/')
@lyrica.route('/index')
def index():
    #return jsonify({"test": True})
    return render_template('index.html')

# GET 
@lyrica.route('/v1/api/lyrica', methods=['GET'])
@lyrica.route('/v1/api/lyrica/<id>', methods=['GET'])
def get_lyrica(id=None):
    lyrica = helper.get_lyrica(id)
    r = {
            "success": True,
            "lyrica": lyrica,
        }
    return jsonify(r)

# DELETE 
@lyrica.route('/v1/api/lyrica/<id>', methods=['DELETE'])
def delete_lyrica(id=None):
    r = {'success': False, 'lyrica': {}}

    if id is not None:
        lyrica = helper.delete_lyrica(id)
        r['success'] = True

    return jsonify(r)

# POST 
@lyrica.route('/v1/api/lyrica', methods=['POST'])
def insert_lyrica(id=None):
    data = request.get_json(force=True)

    lyrica = helper.insert_lyrica(data)
    r = {
            "success": True,
            "lyrica": lyrica,
        }

    return jsonify(r)

# UPDATE 
@lyrica.route('/v1/api/lyrica/<id>', methods=['PUT'])
def update_lyrica(id=None):
    data = request.get_json(force=True)
    r = {'success': False, 'lyrica': {}}

    lyrica = helper.update_lyrica(id, data)
    r = {
            "success": True,
            "lyrica": lyrica,
        }

    return jsonify(r)
