from flask import Flask, send_from_directory
from main.views import main_blueprint
#from api.views import api_blueprint


app = Flask(__name__)

"""
импортируем и регистрируем блупринты main и api
"""

app.register_blueprint(main_blueprint)
#app.register_blueprint(api_blueprint)

app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(debug=True)


#@app.route("/uploads/<path:path>")
#def static_dir(path):
#    return send_from_directory("uploads", path)
