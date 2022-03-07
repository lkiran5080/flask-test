from flask import url_for, current_app
from datetime import datetime
from ginger import db, login_manager, bcrypt
from flask_login import UserMixin
import jwt
from time import time
import json

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


members_table = db.Table('members',
                         db.Column('user_id', db.Integer, db.ForeignKey(
                             'users.id')),
                         db.Column('project_id', db.Integer, db.ForeignKey(
                             'projects.id')))

followers_table = db.Table('followers',
                           db.Column('follower_id', db.Integer, db.ForeignKey(
                               'users.id')),
                           db.Column('followed_id', db.Integer, db.ForeignKey(
                               'users.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    account_created = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    image_file = db.Column(db.String(20),
                           default='default.jpg')

    # self referential relationship
    followed = db.relationship(
        'User', secondary=followers_table,
        primaryjoin=(followers_table.c.follower_id == id),
        secondaryjoin=(followers_table.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    # many to many
    projects = db.relationship(
        'Project', secondary=members_table, 
        backref=db.backref('members', lazy='dynamic'), lazy='dynamic')

    # one to many relationship
    issues = db.relationship('Issue', backref="issue_author", lazy='dynamic')
    comments = db.relationship(
        'Comment', backref='comment_author', lazy='dynamic')
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def get_avatar(self):
        return url_for(
        'static', filename=f'profile_pics/{self.image_file}')
        
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
    
    def add_notification(self, name, data):
        self.notifications.filter_by(name=name).delete()
        n = Notification(name=name, payload_json=json.dumps(data), user=self)
        db.session.add(n)
        return n
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers_table.c.followed_id == user.id).count() > 0
        
    def join_project(self,project):
        if not self.is_member_of(project):
            self.projects.append(project)
    
    def leave_project(self,project):
        if self.is_member_of(project):
            self.projects.remove(project)
    
    def is_member_of(self,project):
        return self.projects.filter(
            members_table.c.project_id == project.id
        ).count() > 0
    


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True, unique=True, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    created_by = db.Column(db.String(), nullable=False)

    # one to many
    issues = db.relationship('Issue', backref="parent_project", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Project('{self.name}', '{self.date_created}')"
    
    def add_member(self,user):
        if not self.is_member(user):
            self.members.append(user)
        
    def remove_member(self,user):
        if self.is_member(user):
            self.members.remove(user)
        
    def is_member(self, user):
        return self.members.filter(
            members_table.c.user_id == user.id
            ).count() > 0


class Issue(db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    created_by = db.Column(db.String(), nullable=False)

    issue_type = db.Column(db.String(), nullable=False)
    summary = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text)

    status = db.Column(db.String, default='todo', nullable=False)

    completed_on = db.Column(db.DateTime)

    assignee = db.Column(db.String())

    labels = db.Column(db.String())
    attachment = db.Column(db.String())
    flagged = db.Column(db.Boolean)

    project_id = db.Column(
        db.Integer, db.ForeignKey('projects.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship(
        'Comment', backref='comment_parent', lazy='dynamic')

    def __repr__(self) -> str:
        return f"Issue('{self.issue_type}', '{self.summary}')"


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, index=True, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    issue_id = db.Column(db.Integer, db.ForeignKey(
        'issues.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Comment('{self.content}', '{self.date_created}')"

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
        return json.loads(str(self.payload_json))

""" class Sprint(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow)

    name = db.Column(db.String(), unique=True)
    goal = db.Column(db.Text ) """
#issues = db.relationship('Issue', backref="parent_sprint", lazy = 'dynamic')
