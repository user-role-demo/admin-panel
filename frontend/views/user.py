from flask import Blueprint, render_template, redirect, url_for, request

from frontend.client.api import client
from frontend.forms.users import DeleteUserForm, UpdateUserForm
from frontend.forms.users import AddRoleToUserForm, RemoveRoleFromUserForm

view = Blueprint('users', __name__)


@view.route('/<int:uid>', methods=['GET', 'POST'])
def user(uid):
    user = client.users.get_by_id(uid)
    roles = client.roles.get_all()
    added_roles = client.users.get_roles(uid)
    available_roles = [role for role in roles if role not in added_roles]
    title = user.name

    update_form = UpdateUserForm(csrf_enabled=False)
    if update_form.validate_on_submit():
        if update_form.update_user(user_id=uid):
            return redirect(request.url)

    add_role_form = AddRoleToUserForm()
    role_choices = [(role.uid, role.name) for role in available_roles]
    add_role_form.role_select.choices = role_choices
    if add_role_form.validate_on_submit():
        if add_role_form.add_role_to_user(uid):
            return redirect(request.url)

    remove_role_form = RemoveRoleFromUserForm()
    remove_role_form.role_select.choices = [(role.uid, role.name) for role in added_roles]
    if remove_role_form.validate_on_submit():
        if remove_role_form.remove_role_from_user(uid):
            return redirect(request.url)

    delete_form = DeleteUserForm()
    if delete_form.validate_on_submit():
        if delete_form.delete_user(user_id=uid):
            return redirect(url_for('index.index'))

    return render_template(
        'user.html',
        page_title=title,
        user=user.dict(),
        added_roles=', '.join([role.name for role in added_roles]),
        update_form=update_form,
        delete_form=delete_form,
        add_role_form=add_role_form,
        remove_role_form=remove_role_form,
    )
