from app import db


class AnimalType(db.Model):
    __tablename__ = "animal_type"
    id = db.Column(db.SmallInteger, primary_key=True)
    value = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "<AnimalType(id='%d', value='%s')>" % (
            self.id, self.value)

@db.event.listens_for(AnimalType.__table__, 'after_create')
def insertInitialValues(*args, **kwargs):
    db.session.add(AnimalType(value='Perro'))
    db.session.add(AnimalType(value='Gato'))
    db.session.add(AnimalType(value='Pájaro'))
    db.session.add(AnimalType(value='Conejo'))
    db.session.add(AnimalType(value='Hamster'))
    db.session.commit()