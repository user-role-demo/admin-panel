import httpx
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from http import HTTPStatus

from frontend.config import app_config

url = f'{app_config.backend_url}/users/'


class CreateUserForm(FlaskForm):
    name = StringField(
        'User name',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField('Create', render_kw={"class": "btn btn-success"})

    def create_user(self) -> bool:
        data = {'name': self.name.data}
        answer = httpx.post(url, json=data)
        if answer.status_code != HTTPStatus.CREATED:
            return False

        return True


class UpdateUserForm(FlaskForm):
    name = StringField(
        'Updated user name',
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField('Update', render_kw={"class": "btn btn-primary"})

    def update_user(self, user_id: int) -> bool:
        data = {'name': self.name.data}
        answer = httpx.put(f'{url}{user_id}', json=data)
        if answer.status_code != HTTPStatus.OK:
            return False

        return True


class DeleteUserForm(FlaskForm):
    submit = SubmitField('Delete', render_kw={"class": "btn btn-danger"})

    def delete_user(self, user_id: int) -> bool:
        answer = httpx.delete(f'{url}{user_id}')
        if answer.status_code != HTTPStatus.NO_CONTENT:
            return False

        return True


class AddRoleToUserForm(FlaskForm):
    role_select = SelectField('Add role to user', coerce=int, render_kw={"class": "form-select"})
    submit = SubmitField('Add role', render_kw={"class": "btn btn-success"})

    def add_role_to_user(self, user_id: int) -> bool:
        data = {"role_id": self.role_select.data}
        answer = httpx.post(f'{url}{user_id}/roles', json=data)
        if answer.status_code != HTTPStatus.CREATED:
            return False

        return True


class RemoveRoleFromUserForm(FlaskForm):
    role_select = SelectField(
        'Remove role from user',
        coerce=int,
        render_kw={"class": "form-select"},
    )
    submit = SubmitField('Remove role', render_kw={"class": "btn btn-warning"})

    def remove_role_from_user(self, user_id: int) -> bool:
        answer = httpx.delete(f'{url}{user_id}/roles/{self.role_select.data}')
        if answer.status_code != HTTPStatus.NO_CONTENT:
            return False

        return True
