from flask import Flask
from main.views import main_blueprint
from api.views import api_blueprint
from errors.views import errors_blueprint


app = Flask(__name__)

"""
импортируем и регистрируем блупринты main и api
"""

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(errors_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
