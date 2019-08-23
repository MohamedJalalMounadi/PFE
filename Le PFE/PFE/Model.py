from PFE import DB, LM
from flask_login import UserMixin


@LM.user_loader
def load_client(client_id):
    return Client.query.get(int(client_id))


class Client(DB.Model, UserMixin):
    id = DB.Column(DB.Integer, primary_key=True)
    Nom = DB.Column(DB.String(40), nullable=False)
    Prenom = DB.Column(DB.String(40), nullable=False)
    DateNaissance = DB.Column(DB.String(20), nullable=False)
    Telephone = DB.Column(DB.String(20), nullable=False)
    Email = DB.Column(DB.String(120), nullable=False)
    Login = DB.Column(DB.String(20), nullable=False)
    MotDePass = DB.Column(DB.String(60), nullable=False)
    Compte = DB.relationship('Compte', backref='Client', lazy=True)


class Agence(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    Responsable = DB.Column(DB.String(100), nullable=False)
    ville = DB.Column(DB.String(120), nullable=False)
    CodeGuichet = DB.Column(DB.Integer, nullable=False)
    Fax = DB.Column(DB.String(100, nullable=False)
    Conseiller = DB.relationship('Conseiller', backref='Agence', lazy=True)


class Compte(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    Numero = DB.Column(DB.Integer, nullable=False)
    Solde = DB.Column(DB.Float, nullable=False)
    DateOuverture = DB.Column(DB.DateTime, nullable=False)
    client_id = DB.Column(DB.Integer,
                          DB.ForeignKey('client.id'), nullable=False)

class Conseiller(DB.Model):
    id =  DB.Column(DB.Integer, primary_key=True)
    Nom = DB.Column(DB.String(40), nullable=False)
    Prenom = DB.Column(DB.String(40), nullable=False)
    DateNaissance = DB.Column(DB.String(20), nullable=False)
    Telephone = DB.Column(DB.String(20), nullable=False)
    Email = DB.Column(DB.String(120), nullable=False)
    agence_id = DB.Column(DB.Integer,
                          DB.ForeignKey('agence.id'), nullable=False)