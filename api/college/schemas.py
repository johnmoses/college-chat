from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    avatar = fields.String()
    mobile = fields.String()
    email = fields.String()
    gender = fields.String()
    bio = fields.String()
    address = fields.String()
    is_bot = fields.Boolean()
    is_verified = fields.Boolean()
    is_used = fields.Boolean()
    is_admin = fields.Boolean()
    is_staff = fields.Boolean()
    is_active = fields.Boolean()
    date_joined = fields.DateTime()
    is_deleted = fields.Boolean()
    modified_at = fields.DateTime()
    deleted_at = fields.DateTime()
    restored_at = fields.DateTime()


class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()
    description = fields.String()

class CourseItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()
    description = fields.String()

class RegistrationSchema(Schema):
    id = fields.Int(dump_only=True)
    comment = fields.String()
    attachment = fields.String()
    student_id = fields.Int()
    created_at = fields.DateTime()
    course = fields.Nested(CourseSchema(), dump_only=True)