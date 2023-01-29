from app.extensions import db

class User(db.Model):
    fname = db.Column(db.String(50) , primary_key=True)
    lname = db.Column(db.String(50))

    def __repr__(self) -> str:
        return self.fname , self.lname