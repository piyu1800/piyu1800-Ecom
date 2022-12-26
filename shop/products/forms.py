# from flask_wtf.file import FileAllowed, FileField, FileRequired
# from wtforms import Form,  IntegerField, StringField, BooleanField, TextAreaField,validators




# class Addproducts(Form):
#     name = StringField('Name',[validators.DataRequired()])
#     price = IntegerField('Price',[validators.DataRequired()])
#     discount = IntegerField('Discount', default =0)
#     stock = IntegerField('Stock', [validators.DataRequired()])
#     discription = TextAreaField('Discription', [validators.DataRequired()])
#     colors = TextAreaField('Colors',[validators.DataRequired()])

#     image_1 = FileField('Image_1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
#     image_2 = FileField('Image_2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
#     image_3 = FileField('Image_3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])


from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators,DecimalField
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Addproducts(Form):
    # id = IntegerField('id', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colors = StringField('Colors', [validators.DataRequired()])
    discription = TextAreaField('Discription', [validators.DataRequired()])
    

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])

