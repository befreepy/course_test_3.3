from flask import Flask
from main.views import main_blueprint
from api.views import api_blueprint

app = Flask(__name__)

"""
импортируем и регистрируем блупринты main и api
"""

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

"""
обработчик ошибок
"""
@app.errorhandler(404)
def page_not_found():
    return "<h1>Страница не найдена</h1>"


@app.errorhandler(500)
def server_error():
    return "<h1>Неожиданная ошибка</h1>"


if __name__ == '__main__':
    app.run(debug=True)
