from wtforms import Form, StringField, SelectField, validators, DateField,SubmitField,IntegerField,PasswordField
import wtforms.fields as fld


class Staff_Login(Form):
    Admin = StringField("Admin",[validators.Length(min=6,max=6), validators.data_required()])
    password = PasswordField('Password')
    btn = SubmitField(label='SUMBIT')