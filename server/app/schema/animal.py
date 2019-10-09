from app.model.animal import Animal
from app import ma


class AnimalSchema(ma.ModelSchema):
    class Meta:
        model = Animal
