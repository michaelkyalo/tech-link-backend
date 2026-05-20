from app import create_app
from app.extensions import socketio
import os   

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    socketio.run(
        app,
        debug=True,
        port=port
    )