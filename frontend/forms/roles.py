import httpx
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from http import HTTPStatus

from frontend.config import app_config

url = f'{app_config.backend_url}/roles/'


class CreateRoleForm(FlaskForm):
    name = StringField(
        'Role name',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField('Create', render_kw={"class": "btn btn-success"})

    def create_role(self) -> bool:
        data = {'name': self.name.data}
        answer = httpx.post(url, json=data)
        if answer.status_code != HTTPStatus.CREATED:
            return False

        return True


class UpdateRoleForm(FlaskForm):
    name = StringField(
        'Updated role name',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField('Update', render_kw={"class": "btn btn-primary"})

    def update_role(self, role_id: int) -> bool:
        data = {'name': self.name.data}
        answer = httpx.put(f'{url}{role_id}', json=data)
        if answer.status_code != HTTPStatus.OK:
            return False

        return True


class DeleteRoleForm(FlaskForm):
    submit = SubmitField('Delete', render_kw={"class": "btn btn-danger"})

    def delete_role(self, role_id: int) -> bool:
        answer = httpx.delete(f'{url}{role_id}')
        if answer.status_code != HTTPStatus.NO_CONTENT:
            return False

        return True
