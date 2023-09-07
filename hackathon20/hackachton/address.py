from wtforms import Form, StringField, SelectField, validators, DateField,FileField, SubmitField,RadioField
import wtforms.fields as fld
from wtforms.fields import EmailField,TelField


class addressform(Form):
    country = StringField("country", [validators.Length(min=1, max=30)])
    company = StringField("company", [validators.Length(min=1, max=30), validators.Optional()])
    address = StringField("address",[validators.Optional()])
    house = StringField("house", [validators.Length(min=1, max=30), validators.Optional()])
    postal_code = StringField("postal_code", [validators.Length(min=1, max=10), validators.Optional()])


class paymentform(Form):
    card_number = StringField("card number", [validators.Length(min=16, max=16), validators.Optional()])
    card_name = StringField("card name", [validators.Length(min=1, max=30), validators.Optional()])
    expiry_date = StringField("expiry date", [validators.Length(min=1, max=4), validators.Optional()])

class Updateprofileforstaff(Form):
    first_name = StringField("First Name", [validators.Length(min=1, max=30), validators.data_required()])
    last_name = StringField("Last Name", [validators.Length(min=1, max=30), validators.data_required()])
    email = EmailField("Email", [validators.data_required()])
    dob = DateField('Date of Birth', format='%Y-%m-%d')
    gender = SelectField('Gender', [validators.DataRequired()],
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    phonenumber = TelField("Phone Number", [validators.Length(min=8, max=8), validators.data_required()])
    image = FileField("Avatar")
    country = StringField("country", [validators.Length(min=1, max=30), validators.Optional()])
    company = StringField("company", [validators.Length(min=1, max=30), validators.Optional()])
    address = StringField("address", [validators.Optional()])
    house = StringField("house", [validators.Length(min=1, max=30), validators.Optional()])
    postal_code = StringField("postal code", [validators.Length(min=1, max=10), validators.Optional()])


