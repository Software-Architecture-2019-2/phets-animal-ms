from app import db


class AnimalMedia(db.Model):
    __tablename__ = "animal_media"
    id = db.Column(db.String(36), primary_key=True)
    animal_id = db.Column(db.BigInteger, db.ForeignKey(
        'animal.id'), nullable=False)
    animal = db.relationship("Animal", backref='media', cascade="all,delete", lazy="subquery")

    def __repr__(self):
        return "<AnimalMedia(id='%d', animal.id='%d', animal.name='%s')>" % (
            self.id, self.animal.id, self.animal.name)
