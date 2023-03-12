from flask_restful import Resource, reqparse
from Models.usuario import UserModel


class User (Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json(), 200
        # status code HTTP not found
        return {'message': 'Usuario nao encontrado'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'erro ao deletar '}, 500
            return {'message': 'user deletado'}

        return {'message': 'Usuario nao encontrado'}, 404


class UserRegister(Resource):

    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument(
            'login', type=str, required=True, help="campo login nao pode ser em branco")
        atributos.add_argument(
            'senha', type=str, required=True, help="campo senha nao pode ser em branco")
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {"message": "usuario '{}' ja existe".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {"message": "usuario criado com sucesso"}, 201
