from SparseArray import SparseArray
import os
from flask import Flask, abort, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)    
"""
swagger declaration
"""
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "SparseArray matching strings method"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

"""
API Endpoint declaration
"""
@app.route('/api/sparsearray', methods=['POST'])
def sparsearray():
    """
    Get the SPARSE_ARRAY_STRINGS environment variable as a list of strings
    """
    strings = os.environ.get('SPARSE_ARRAY_STRINGS').split(',') 

    """
    Get a list of query as a Get request of format json
    """
    if not request.json or not 'queries' in request.json:
        abort(400)        
    task = {
            'queries': request.json['queries'],
            }
    queries = task['queries'].split(',')

    """
    Apply the matching_string() function of class SparseArray
    to the list of query and the list of strings 
    """    
    with SparseArray(strings,queries) as sparse_array:
        return jsonify(sparse_array.matching_strings()), 201
   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
