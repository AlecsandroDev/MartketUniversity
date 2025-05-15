from app import db

class Administrator(db.Model):
    __tablename__ = 'administrator'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Administrator {self.nome}>'


class User(db.Model):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    idade = db.Column(db.Integer, nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "idade": self.idade,
            "cidade": self.cidade,
            "estado": self.estado,
        }

    def __repr__(self):
        return f'<Pessoas {self.nome}>'


class Anuncio(db.Model):
    __tablename__ = 'anuncios'

    id = db.Column(db.Integer, primary_key=True) 
    titulo = db.Column(db.String(100), nullable=False) 
    info = db.Column(db.String(100), nullable=False) 
    preco = db.Column(db.Integer, nullable=False) 
    vendedor = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        
        return f'<Anuncio {self.titulo} - {self.vendedor}>'


class Reports(db.Model):
    __tablename__ = 'reportes'
    id = db.Column(db.Integer, primary_key=True) 
    chamado = db.Column(db.Integer, nullable=False)  
    usuario = db.Column(db.String(100), nullable=False)  
    titulo = db.Column(db.String(100), nullable=False) 
    info = db.Column(db.String(100), nullable=False)  

    def __repr__(self):
        
        return f'<Reportes {self.titulo} - {self.vendedor}>'
    