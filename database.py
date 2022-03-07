from ginger import db, create_app
from ginger.models import User, Project, Issue, Comment
from pprint import pprint
app = create_app()

with app.app_context():
    
    print(User.query.all())
    
    """ user = User.query.filter_by(username='newuser01').first()
    print(user)
    
    project = Project.query.filter_by(name='Test Project').first()
    print(project)
    
    print(project.members.all())
    
    project.add_member(user)
    
    db.session.commit()
    
    print(project.members.all()) """
    
    
    
    """ pprint(Comment.query.first().user_id)
    
    l = []
    for comment in Comment.query.all():
        user_id = comment.user_id
        user = User.query.get(user_id)
        l.append({'user':user,'comment':comment}) """
        
        
    # pprint(Comment.query.all())
    # print(Project.query.first().issues)
    # print(Project.query.first().member)
    # print(Project.query.all())
    # print(User.query.first().projects)
