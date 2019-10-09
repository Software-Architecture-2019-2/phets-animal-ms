from flask import request
from flask_restful import Resource
from app.schema.animal import AnimalSchema
from app.service.animal import AnimalService

animal_schema = AnimalSchema()


class AnimalResource(Resource):
    def get(self, animal_id):
        animal = AnimalService.getById(animal_id)
        return animal_schema.dump(animal), 200

    def put(self, animal_id):
        animal = animal_schema.load(request.json)
        updated = AnimalService.update(animal_id, animal)
        if updated:
            return animal_schema.dump(updated), 200
        return None, 400


class AnimalListResource(Resource):
    def get(self):
        # page = request.args.get('page', type = int)
        # if (page):
        #     print(page)
        # filter_args = request.args.to_dict()
        # print(filter_args)
        # del filter_args['page']
        # print(filter_args)
        # animals = Animal.query.all()
        # animal_columns = Animal.__table__.columns
        # print(animal_columns)
        # print(animal_columns.keys())
        # animals = Animal.query.filter_by(**filter_args)
        animals = AnimalService.getAll()
        # print(animals)
        dumped = animal_schema.dump(animals, many=True)
        return dumped, 200

    def post(self):
        # Loads Animal Model
        animal = animal_schema.load(request.json)
        AnimalService.save(animal)
        return animal_schema.dump(animal), 200
