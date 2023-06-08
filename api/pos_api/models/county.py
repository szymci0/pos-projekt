from mongoengine import DynamicDocument, StringField, ListField


class County(DynamicDocument):
    name = StringField()
    teryt = StringField()
    users = ListField()
