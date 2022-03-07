from ginger import create_app, db
from ginger.models import User, Project, Issue, Comment
app = create_app()


@app.cli.command()
def createdb():
    db.create_all()
    
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Project': Project, 'Issue':Issue, 'Comment':Comment}


if __name__ == '__main__':
    app.run(debug=True)
