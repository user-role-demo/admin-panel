from flask import Blueprint, render_template, redirect, url_for, request

from frontend.client.api import client
from frontend.forms.roles import DeleteRoleForm, UpdateRoleForm

view = Blueprint('roles', __name__)


@view.route('/<uid>', methods=['GET', 'POST'])
def role(uid):
    role = client.roles.get_by_id(uid)
    title = role.name

    update_form = UpdateRoleForm(csrf_enabled=False)
    if update_form.validate_on_submit():
        if update_form.update_role(role_id=uid):
            return redirect(request.url)

    delete_form = DeleteRoleForm()
    if delete_form.validate_on_submit():
        if delete_form.delete_role(role_id=uid):
            return redirect(url_for('index.index'))

    return render_template(
        'role.html',
        page_title=title,
        role=role.dict(),
        update_form=update_form,
        delete_form=delete_form,
    )
