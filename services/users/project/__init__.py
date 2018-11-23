# services/users/project/__init__.py

import os                                   #nuevo
from flask import Flask, jsonify


# Istanciado la app
app = Flask(__name__)

# estableciendo configuracion
app_settings = os.getenv('APP_SETTINGS')    #nuevo
app.config.from_object(app_settings)        #nuevo

# Establecer configuracion
app.config.from_object('project.config.DevelopmentConfig')

import sys
print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
