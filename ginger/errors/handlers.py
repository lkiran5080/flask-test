

from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def page_note_found(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
