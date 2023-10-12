"""
Schemas - Gender
"""
from marshmallow import Schema, fields


class GenderSchema(Schema):
    """Schema to the Gender of an Anime."""

    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)


class GenderUpdateSchema(Schema):
    """Schema to Update a Gender."""

    name = fields.Str(required=True)
