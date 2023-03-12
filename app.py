from flask import Flask
from flask_restful import  Api
from resources.hotel import Hoteis ,Hotel
from resources.usuario import User, UserRegister


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


api.add_resource(Hoteis, '/hoteis')  #cria a api
api.add_resource(User, '/usuarios/<int:user_id>')  #cria a api
api.add_resource(UserRegister, '/cadastro')  #cria a api
api.add_resource(Hotel ,'/hoteis/<string:hotel_id>')

@app.before_first_request
def cria_banco():
     banco.create_all()

if __name__ == '__main__':
     from sql_alchemy import banco
     banco.init_app(app)
     app.run(debug=True)
