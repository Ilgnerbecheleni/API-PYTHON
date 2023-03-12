from flask_restful import Resource, reqparse
from Models.hotel import HotelModel


hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.4,
        'diaria': 420.2,
        'cidade': "Sao Paulo"
    },
    {
        'hotel_id': 'Omega',
        'nome': 'Alpha Hotel',
        'estrelas': 4.2,
        'diaria': 390.2,
        'cidade': "Rio de Janeiro"
    },
    {
        'hotel_id': 'Bravo',
        'nome': 'Alpha Hotel',
        'estrelas': 4.1,
        'diaria': 220.2,
        'cidade': "Sao Paulo"
    },
]


def json(self):
    return {
        'hotel_id': self.hotel_id,
        'nome': self.nome,
        'estrelas': self.estrelas,
        'diaria': self.diaria,
        'cidade': self.cidade,

    }


class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel  in HotelModel.query.all()]}


class Hotel (Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome" , type=str , required=True , help="este campo nao pode ser nulo")
    argumentos.add_argument("estrelas", type=float , required=True , help="este campo nao pode ser nulo")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json(), 200
        # status code HTTP not found
        return {'message': 'Hotel nao encontrado'}, 404

    def post(self, hotel_id):

        if HotelModel.find_hotel(hotel_id):
            return {'message': 'Hotel id "{}" ja existe'.format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'erro ao tentar salvar hotel'}, 500
        return hotel.json()

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200

        hotel = HotelModel(hotel_id, **dados)    # **kwargs desempacota todos os dados e cria instancia da classe
        try:
            dhotel.save_hotel()
        except:
            return {'message': 'erro ao tentar salvar hotel'}, 500
        return hotel.json(), 201  # created

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
             hotel.delete_hotel()
            except:
                return {'message': 'erro ao deletar '}, 500
            return {'message': 'Hotel deletado'}

        return {'message': 'Hotel nao encontrado'},404
