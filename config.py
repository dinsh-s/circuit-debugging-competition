import os

# Database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# File upload configuration
UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB
