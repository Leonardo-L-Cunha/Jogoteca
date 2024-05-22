import os

SECRET_KEY = 'pokemon123'

SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '1988',
    servidor = 'localhost',
    database = 'jogoteca'
)


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'