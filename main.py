from app import create_app, db
from app.models import User, Post

app = create_app()
app.run()
