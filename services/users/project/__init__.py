# services/users/project/__init__.py


from flask import Flask, jsonify


# Istanciado la app
app = Flask(__name__)

# Establecer configuracion
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
