from main import db 

class Pessoa(db.Model):
   id       = db.column(db.integer, primary_key=True, autoincrement=True)
   nome     = db.column(db.string(15), nullable=False)
   idade    = db.column(db.integer(40), nullable=False)
   altura   = db.column(db.string(20), nullable=False)

   def __repr__(self):
      return '<Name %r>' % self.name
   


