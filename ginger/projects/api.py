""" from .routes import projects
from ginger.models import Project, User
from flask import redirect, url_for

@projects.route('/project/<string:project_name>/user/<srting:username>', methods=['POST'])
def add_new_member(project_name,username):
    pass

@projects.route('/project/<string:project_name>/user/<srting:username>', methods=['DELETE'])
def add_new_member(project_name,username):
    project = Project.query.filter_by(name=project_name).first_or_404()
    user = User.query.filter_by(username=username).first_or_404()
    if project.is_member(user):
        project.remove_member(user)
        return redirect(url_for('projects.get_project',project_name=project_name))
     """