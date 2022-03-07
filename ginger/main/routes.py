
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ginger.models import Project, User
""" from ginger.models import Post """

main = Blueprint('main', __name__)


@main.route('/')
def index():
    #flash("Hello", "success")

    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    return render_template('index.html')


@main.route('/home')
@login_required
def home():
    projects = ['project01', 'project02', 'project03']
    projects1 = []
    """ projects2 = Project.query.join(
        User, Project.member).filter_by(member=current_user) """
    projects2 = current_user.projects

    return render_template('home.html', projects=projects2)


""" page = request.args.get('page', 1, type=int)
posts = Post.query.order_by(
Post.date_created.desc()).paginate(per_page=5, page=page)
return render_template('home.html', posts=posts) """
