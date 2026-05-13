from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_socketio import SocketIO

bcrypt = Bcrypt()
cors = CORS()
migrate = Migrate()
socketio = SocketIO(cors_allowed_origins="*")
api = Api(prefix="/api")