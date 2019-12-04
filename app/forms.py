from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField, TextAreaField
from werkzeug.security import generate_password_hash,check_password_hash
from wtforms.validators import Email,EqualTo,DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField

class QueryForm(FlaskForm):
    query = StringField('Query', render_kw={"placeholder":"What do you want to search?"})
    submit = SubmitField('Search!')


class NewDocForm(FlaskForm):
    document = TextAreaField('New Document', render_kw={"placeholder":"Enter documents here, seperated by \n\n"})
    submit = SubmitField('Add')