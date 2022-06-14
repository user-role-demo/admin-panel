from flask import Blueprint, render_template, redirect, url_for

from frontend.client.api import client
from frontend.forms.roles import CreateRoleForm

view = Blueprint('index', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    roles = client.roles.get_all()
    roles_with_users = []
    for role in roles:
        users_of_role = client.roles.get_users(uid=role.uid)
        role_with_users = role.dict()
        user_names = ', '.join([user.name for user in users_of_role])
        role_with_users['users'] = user_names
        roles_with_users.append(role_with_users)

    role_form = CreateRoleForm()
    if role_form.validate_on_submit():
        if role_form.create_role():
            return redirect(url_for('index.index'))

    return render_template('index.html', roles=roles_with_users, role_form=role_form)
