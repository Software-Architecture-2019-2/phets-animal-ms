from app.model.animal import Animal
from app import db


class AnimalService:
    @staticmethod
    def getAll():
        return Animal.query.all()

    @staticmethod
    def getById(id):
        return Animal.query.get(id)

    @staticmethod
    def save(entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    @staticmethod
    def update(id, entity):
        saved = AnimalService.getById(id)
        if saved:
            db.session.merge(entity)
            db.session.flush()
            db.session.commit()
            return saved
        return None

    @staticmethod
    def delete(id):
        saved = db.session.query(Animal).get(id)
        if saved:
            db.session.delete(saved)
            db.session.commit()
            return saved
        return None
