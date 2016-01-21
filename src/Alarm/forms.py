from flask.ext.wtf import Form
from wtforms import StringField, SelectField, DateTimeField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

class AddAlarmForm(Form):
    def getChoices():
    	return [('1','user1'), ('2','user2')]

    track_uri = StringField('track_uri', validators=[DataRequired()])
    user = SelectField('user', choices=getChoices(), validators=[DataRequired()])
    repeat = IntegerField('repeat', validators=[DataRequired()])
    # datetime = DateTimeField('datetimepicker', format='%d-%m-%Y %H:%M') # , validators=[DataRequired()]
