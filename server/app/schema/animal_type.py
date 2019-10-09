from app.model.animal_type import AnimalType
from app import ma


class AnimalTypeSchema(ma.ModelSchema):
    class Meta:
        model = AnimalType
