from app import app
from models import db

with app.app_context():
    try:
        db.session.execute(db.text(
            "ALTER TABLE products ADD COLUMN sizes VARCHAR(200) DEFAULT 'S,M,L,XL,XXL'"
        ))
        db.session.commit()
        print("sizes column added successfully.")
    except Exception as e:
        db.session.rollback()
        print("Could not add sizes column. It may already exist.")
        print(e)