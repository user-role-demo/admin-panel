from flask import Blueprint, render_template, redirect, url_for

from frontend.client.api import client
from frontend.forms.roles import CreateRoleForm
from frontend.forms.users import CreateUserForm

view = Blueprint('index', __name__)


@view.route('/')
def index():
    users = client.users.get_all()

    roles = client.roles.get_all()
    roles_with_users = []
    for role in roles:
        users_of_role = client.roles.get_users(uid=role.uid)
        role_with_users = role.dict()
        user_names = ', '.join([user.name for user in users_of_role])
        role_with_users['users'] = user_names
        roles_with_users.append(role_with_users)

    user_form = CreateUserForm()
    role_form = CreateRoleForm()

    return render_template(
        'index.html',
        users=[user.dict() for user in users],
        roles=roles_with_users,
        user_form=user_form,
        role_form=role_form,
        page_title='User-Role demo',
    )


@view.route('/add_user', methods=['POST'])
def add_user():
    user_form = CreateUserForm()
    if user_form.validate_on_submit():
        if user_form.create_user():
            return redirect(url_for('index.index'))


@view.route('/add_role', methods=['POST'])
def add_role():
    role_form = CreateRoleForm()
    if role_form.submit.data and role_form.validate():
        if role_form.create_role():
            return redirect(url_for('index.index'))
