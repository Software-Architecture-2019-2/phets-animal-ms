from flask_restful import Resource
from app.schema.animal_type import AnimalTypeSchema
from app.service.animal_type import AnimalTypeService

animal_type_schema = AnimalTypeSchema()
animal_type_service = AnimalTypeService()

class AnimalTypeResource(Resource):
    def get(self):
        animal_types = animal_type_service.getAll()
        dumped = animal_type_schema.dump(animal_types, many=True)
        return dumped, 200
