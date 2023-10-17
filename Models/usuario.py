from main import db 

class Usuarios(db.Model):
   nickname    = db.column(db.string(8), primary_key=True)
   nome        = db.column(db.string(20), nullable=False)
   senha       = db.column(db.string(100), nullable=False)

   def __repr__(self):
      return '<Name %r>' % self.name
