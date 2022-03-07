from flask import current_app
import secrets
import os


def save_attachment(form_attachment):

    random_hex = secrets.token_hex(8)

    # print(form_attachment)
    _, f_ext = os.path.splitext(form_attachment.filename)

    attachment_fn = random_hex + f_ext

    attachment_path = os.path.join(
        current_app.root_path, 'static/profile_pics', attachment_fn)

    if (f_ext == 'jpeg' or f_ext == 'jpg' or f_ext == 'png'):
        pass

    if (f_ext == 'docx' or f_ext == 'doc' or f_ext == 'pdf'):
        pass

    form_attachment.filename = attachment_fn

    form_attachment.save(attachment_path)

    return attachment_fn
