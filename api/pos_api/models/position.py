from mongoengine import DynamicDocument, StringField, FloatField


class Position(DynamicDocument):
    email = StringField()
    x = FloatField()
    y = FloatField()
