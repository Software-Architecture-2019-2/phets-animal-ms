from app import db

class Animal(db.Model):
    __tablename__ = "animal"
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(30))
    user = db.Column(db.String(40))
    breed = db.Column(db.String(50))
    adoption = db.Column(db.Boolean)
    birthdate = db.Column(db.Date)
    type_id = db.Column(db.SmallInteger, db.ForeignKey('animal_type.id'))
    animal_type = db.relationship("AnimalType")

    def __repr__(self):
        return "<Animal(id='%d', name='%s', type='%s')>" % (
            self.id, self.name, self.animal_type.value)
