from app import api
from app.resources.animal_type import AnimalTypeResource
from app.resources.animal import AnimalListResource, AnimalResource

api.add_resource(AnimalListResource, '/animals')
api.add_resource(AnimalResource, '/animals/<animal_id>')
api.add_resource(AnimalTypeResource, '/animal-types')