import os

class Config:
  SECRET_KEY = "sua_chave_secreta_super_segura"

  SQLALCHEMY_DATABASE_URI = (
      f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False
