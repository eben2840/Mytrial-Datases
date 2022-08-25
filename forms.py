from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    lastname = StringField('Lastname', [validators.Length(min=4, max=25)])
    Othername= StringField('Othername', [validators.Length(min=4, max=25)])
    Gender = StringField('Gender', [validators.Length(min=4, max=25)])
    BirthDate = StringField('BirthDate', [validators.Length(min=4, max=25)])
    Age = StringField('Age', [validators.Length(min=2, max=25)])
    Age = StringField('Age', [validators.Length(min=2, max=25)])
    Primary = StringField('Primary', [validators.Length(min=4, max=25)])
    Other = StringField('OtherContact', [validators.Length(min=4, max=25)])
    School = StringField('School', [validators.Length(min=4, max=25)])
    Kin = StringField('Kin', [validators.Length(min=4, max=25)])
    Relationship= StringField('Relationship', [validators.Length(min=4, max=25)])
    Home = StringField('Home', [validators.Length(min=4, max=25)])
    Current = StringField('Current', [validators.Length(min=4, max=25)])
    Nationality = StringField('Nationality', [validators.Length(min=4, max=25)])
    Guardian = StringField('Guardian', [validators.Length(min=4, max=25)])
    Year = StringField('Year', [validators.Length(min=4, max=25)])
    Marital = StringField('Marital', [validators.Length(min=4, max=25)])
    Health = StringField('Health', [validators.Length(min=4, max=25)])
    Extra = StringField('Extra', [validators.Length(min=4, max=25)])
    
    submit =SubmitField('submit')