from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from ginger import db
from ginger.projects.forms import ProjectForm, IssueForm, CommentForm, MemberForm
from ginger.projects.utils import save_attachment
from ginger.models import Project, Issue, Comment, User
from flask_login import current_user
from datetime import datetime


projects = Blueprint('projects', __name__)


@projects.route('/project/new', methods=['GET', 'POST'])
def create_project():
    form = ProjectForm()

    if form.validate_on_submit():

        project = Project(name=form.name.data,
                          created_by=current_user.username)
        current_user.projects.append(project)

        db.session.add(project)
        db.session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('new_project.html', form=form)


@projects.route('/project/<string:project_name>',methods=['GET','POST'])
def get_project(project_name):
    form = MemberForm()
    project = Project.query.filter_by(name=project_name).first_or_404()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user:
            if project.is_member(user):
                flash('Already a member !', 'warning')
                return redirect(url_for('projects.get_project',project_name=project_name))
            
            project.add_member(user)
            db.session.commit()
        else:
            flash("User doesn't exist !", 'danger')
            form = MemberForm()
            return redirect(url_for('projects.get_project',project_name=project_name,form=form))

    return render_template('project.html', project=project,form=form)

@projects.route('/project/<string:project_name>/user/<string:username>', methods=['DELETE'])
def add_new_member(project_name,username):
    project = Project.query.filter_by(name=project_name).first_or_404()
    user = User.query.filter_by(username=username).first_or_404()
    if project.is_member(user):
        project.remove_member(user)
        db.session.commit()
        return '', 204

""" @projects.route('/project/<string:project_name>/members')
def get_members(project_name):
    
    project = Project.query.filter_by(name=project_name).first_or_404()
    
    members = projects.members.all()
    
    return  """
    
'''
project/<string:project_name>/user/<string:username> POST
project/<string:project_name>/user/<string:username> DELETE
project/member/remove
'''

@projects.route('/project/<int:id>/update')
def update_project():
    pass


@projects.route('/project/<int:id>/delete')
def delete_project():
    pass


@projects.route('/issue/new', methods=['POST', 'GET'])
def create_issue():
    form = IssueForm()

    if form.validate_on_submit():

        project_name = request.args.get('project')

        if project_name:

            parent_project = Project.query.filter_by(
                name=project_name).first_or_404()

            if form.attachment.data:
                attachment_name = save_attachment(form.attachment.data)
            else:
                attachment_name = ''

            issue = Issue(created_by=current_user.username, issue_type=form.issue_type.data,
                          summary=form.summary.data, description=form.description.data, assignee=form.assignee.data, labels=form.labels.data, attachment=attachment_name, flagged=form.flagged.data, parent_project=parent_project, issue_author=current_user)

            db.session.add(issue)
            db.session.commit()

            flash('Your issue has been created!', 'success')
            return redirect(url_for('projects.get_project', project_name=project_name))

    return render_template('new_issue.html', form=form)


@projects.route('/issue/<int:id>', methods=['GET', 'POST'])
def get_issue(id):

    comment_form = CommentForm()
    issue = Issue.query.filter_by(id=id).first_or_404()

    comments = Comment.query.order_by(Comment.date_created.desc()).filter_by(
        comment_parent=issue).all()
    comment_list = []
    for comment in comments:
        user_id = comment.user_id
        user = User.query.get(user_id)
        comment_list.append({
            'user': user,
            'comment': comment
        })

    # print(comment_list)

    if comment_form.validate_on_submit():

        comment = Comment(content=comment_form.content.data, date_created=datetime.utcnow(),
                          comment_author=current_user, comment_parent=issue)

        db.session.add(comment)

        db.session.commit()

        return redirect(url_for('projects.get_issue', id=id))

    return render_template('issue.html', issue=issue, comments=comment_list, form=comment_form)


@projects.route('/issue/<int:id>/update')
def update_issue():
    pass


@projects.route('/issue/<int:id>/delete')
def delete_issue():
    pass
