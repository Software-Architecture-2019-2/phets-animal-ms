from app.model.animal_type import AnimalType


class AnimalTypeService:
    @staticmethod
    def getAll():
        return AnimalType.query.all()
