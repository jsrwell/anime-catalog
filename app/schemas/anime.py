"""
Schemas - Anime
"""
from marshmallow import Schema, fields


class AnimeSchema(Schema):
    """Schema for Anime."""

    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    gender_id = fields.Integer(required=True)


class AnimeUpdateSchema(Schema):
    """Schema to Update an Anime."""

    name = fields.Str(required=True)
    description = fields.Str(required=True)
