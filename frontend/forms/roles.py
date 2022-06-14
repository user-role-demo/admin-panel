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
