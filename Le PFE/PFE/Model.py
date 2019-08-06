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
