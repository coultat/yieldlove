from flask_wtf import Form
from wtforms import BooleanField 

class check(Form):
    gomapping = BooleanField('Get mapping?')
