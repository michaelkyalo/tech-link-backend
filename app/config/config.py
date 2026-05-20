import os
from dotenv import load_dotenv


load_dotenv()


class Config:

    
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "super-secret-key"
    )

    
    SQLALCHEMY_DATABASE_URI = os.getenv( "DATABASE_URL" )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

  
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "jwt-secret-key"
    )

    JWT_ACCESS_TOKEN_EXPIRES = 86400

    
    CLOUDINARY_CLOUD_NAME = os.getenv(
        "CLOUDINARY_CLOUD_NAME"
    )

    CLOUDINARY_API_KEY = os.getenv(
        "CLOUDINARY_API_KEY"
    )

    CLOUDINARY_API_SECRET = os.getenv(
        "CLOUDINARY_API_SECRET"
    )

    
    SENDGRID_API_KEY = os.getenv(
        "SENDGRID_API_KEY"
    )