"""
Schemas - User
"""
from marshmallow import Schema, fields


class UserSchema(Schema):
    """Schema to the User of the Catalog."""

    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)
