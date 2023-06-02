from mongoengine import DynamicDocument, StringField


class County(DynamicDocument):
    name = StringField()
    teryt = StringField()
