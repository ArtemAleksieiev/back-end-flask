from app import app, db
from app.models import Users, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Post': Post}
