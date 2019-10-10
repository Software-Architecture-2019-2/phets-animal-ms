from app.model.animal import Animal
from app.schema.animal_media import AnimalMediaSchema
from app.schema.animal_type import AnimalTypeSchema
from app import ma


class AnimalSchema(ma.ModelSchema):
    media = ma.Pluck(AnimalMediaSchema, "id", many=True)
    animal_type = ma.Nested(AnimalTypeSchema)
    class Meta:
        model = Animal
