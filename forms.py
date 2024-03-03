from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtf.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """form for adding pet"""
    
    name = StringField(
        'Pet Name',
        validators=[InputRequired()],
    )
    
    species = SelectField(
        'Species',
        choices=[('cat', 'cat'), ('dog', 'dog'), ('fish', 'fish')],
    )
    
    photo_url = StringField(
        'Photo URL',
        validators=[Optional(). URL()],
    )
    
    age = IntegerField(
        'Age',
        validators=[Optional(), NumberRange(min=0, max=30)],
    )
    
    notes = TextAreaField(
        'Comments',
        validators=[Optional(), Length(min=10)],
    )
    
    
class EditPetForm(FlaskForm):
    """form for editing pet info"""
    
    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()],
    )
    
    notes = TextAreaField(
        'Comments',
        validators=[Optional(), Length(min=10)],
    )
    
    available = BooleanField('Available?')