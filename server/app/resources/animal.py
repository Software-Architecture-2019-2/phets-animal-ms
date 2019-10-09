from flask import request
from flask_restful import Resource
from app.schema.animal import AnimalSchema
from app.service.animal import AnimalService

animal_schema = AnimalSchema()


class AnimalResource(Resource):
    def get(self, animal_id):
        animal = AnimalService.getById(animal_id)
        if animal:
            return animal_schema.dump(animal), 200
        return None, 204

    def put(self, animal_id):
        animal = animal_schema.load(request.json)
        updated = AnimalService.update(animal_id, animal)
        if updated:
            return animal_schema.dump(updated), 200
        return None, 204

    def delete(self, animal_id):
        deleted = AnimalService.delete(animal_id)
        if deleted:
            return animal_schema.dump(deleted), 200
        return None, 204


class AnimalListResource(Resource):
    def get(self):
        animals = AnimalService.getAll()
        dumped = animal_schema.dump(animals, many=True)
        return dumped, 200

    def post(self):
        animal = animal_schema.load(request.json)
        AnimalService.save(animal)
        return animal_schema.dump(animal), 200
