from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')



class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Music review', validators=[Required()])
    submit = SubmitField('Submit')


class SongForm(FlaskForm):

    title = StringField('Song title',validators=[Required()])
    artist=StringField('Artist',validators=[Required()])
    category = SelectField('Category',
                                 choices=[('Select category',
                                           'Select category'),
                                          ('gospel', 'gospel'),
                                          ('reggae', 'reggae'),
                                          ('hiphop', 'hiphop'),
                                          ('R&B', 'R&B')],
                                 validators=[Required()])
    # song_url= TextAreaField('Enter URL To Song', validators=[Required()])
    submit = SubmitField('Submit')
