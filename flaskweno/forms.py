from flask_wtf import Form
from wtforms import StringField, TextField, validators, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField
from models import User

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacío mendrugo')

def setupcheckup(form, field):
    if field.data.find("/") > -1:
        print("Por el momento va bien")
    else:
        raise validators.ValidationError('Esto no parece una setup')

class doritos(Form):
    username = StringField('username del carajo',
                [validators.length(min = 4, max= 25, message="pon un nombre de usuário válido, melón!"),
                 validators.Required(message = 'Tonto, pon un nombre de usuario')
                ])
    email = EmailField('email',
            [validators.Required(message = 'a ver carallo, pon un email para que podamos seguri'),
             validators.Email(message = 'pon una dirección de correo válida'),
             validators.length(min=4, max=50, message="Mínimo 4 caracteres y máximo 50 por favor")
             ])
    password = PasswordField('Password', [validators.Required(message="Esa contraseña te la metes por el culo")])
    comment = TextField('Comment')
    honeypot = HiddenField('',[length_honeypot])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError("Menda ya registrado")

class LoginForm(Form):
    username = StringField('Nombre de usuario',
                [validators.Required(message="Pon un nombre carajo!"),
                 validators.length(min=4, max=25, message="Mínimo 4 caracteres y máximo 25")
                 ])
    password = PasswordField('Password', [validators.Required(message="pon la contraseña del demonio")])

class PrebidOrPostbid(Form):
    setup = StringField('Write the setup structure',
            [validators.Required(message="You have to put something inside the field"),
            setupcheckup
            ])
class comment(Form):
    comment = TextField('Write the shit you want to say',
                [validators.Required(message =  "mira me cago en Dios, mete algo o explota")])
