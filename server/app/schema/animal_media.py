from app.model.animal_media import AnimalMedia
from app import ma


class AnimalMediaSchema(ma.ModelSchema):
    class Meta:
        model = AnimalMedia
