from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, DateTimeField, EmailField, FileField,
                     SelectField, StringField, SubmitField, TextAreaField)

from wtforms.validators import DataRequired


class IssueForm(FlaskForm):

    issue_type = SelectField('Issue Type', choices=[(
        'bug', 'Bug'), ('task', 'Task')], validators=[DataRequired()])

    summary = StringField('Summary', validators=[DataRequired()])
    description = TextAreaField('Description')

    assignee = StringField('Assignee')

    labels = StringField('Labels')

    attachment = FileField('Attachment', validators=[
        FileAllowed(['jpg', 'png', 'pdf', 'docx', 'doc', 'txt'])])

    flagged = BooleanField('Flagged')

    submit = SubmitField('Create Issue')


class ProjectForm(FlaskForm):

    name = StringField('Project Name', validators=[DataRequired()])
    submit = SubmitField('Create Project')

class MemberForm(FlaskForm):
    
    name = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Add Member')


class CommentForm(FlaskForm):

    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class SprintForm(FlaskForm):

    name = StringField('Sprint Name', validators=[DataRequired()])

    duration = SelectField('Duration')
    start_date = DateTimeField(
        'Start Date', format="%d/%m/%y", validators=[DataRequired()])
    end_date = DateTimeField(
        'End Date', format="%d/%m/%y", validators=[DataRequired()])

    goal = TextAreaField('Goal')

    submit = SubmitField('Start Sprint')