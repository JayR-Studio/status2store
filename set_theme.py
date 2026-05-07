from app import app
from models import db, SiteSettings

with app.app_context():
    settings = SiteSettings.query.first()

    if settings:
        settings.theme = "luxury"
        db.session.commit()
        print("Theme changed to luxury.")
    else:
        print("No settings found.")