"""
Schemas
"""
from marshmallow import Schema, fields


class AnimeSchema(Schema):
    """Schema for Anime."""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    gender_id = fields.Str(required=True)


class AnimeUpdateSchema(Schema):
    """Schema to Update an Anime."""

    name = fields.Str(required=True)
    description = fields.Str(required=True)


class GenderSchema(Schema):
    """Schema to the Gender of an Anime."""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class GenderUpdateSchema(Schema):
    """Schema to Update an Gender."""

    name = fields.Str(required=True)
