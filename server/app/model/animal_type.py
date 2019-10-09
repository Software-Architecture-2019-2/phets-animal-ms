from app import db


class AnimalType(db.Model):
    __tablename__ = "animal_type"
    id = db.Column(db.SmallInteger, primary_key=True)
    value = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "<AnimalType(id='%d', value='%s')>" % (
            self.id, self.value)
