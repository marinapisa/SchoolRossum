from main import db 

class Pessoa(db.Model):
   id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
   nome     = db.Column(db.String(15), nullable=False)
   idade    = db.Column(db.String(40), nullable=False)
   altura   = db.Column(db.String(20), nullable=False)

   def __repr__(self):
      return '<Name %r>' % self.name
   


