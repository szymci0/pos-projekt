from mongoengine import DynamicDocument, StringField


class BlacklistedTokens(DynamicDocument):
    token = StringField()