class Config:
    SECRET_KEY = 'labinfo'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://usuario:senha@localhost/sistema_objetos_perdidos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False