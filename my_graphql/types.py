from graphene_django import DjangoObjectType
from graphene import ObjectType, String, Field
from todos.models import Todo, Author

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class UserType(ObjectType):
    class NameType(ObjectType):
        title = String()
        first = String()
        last = String()

    class LocationType(ObjectType):
        street = String()
        city = String()
        state = String()
        postcode = String()

    class LoginType(ObjectType):
        username = String()
        password = String()
        salt = String()
        md5 = String()
        sha1 = String()
        sha256 = String()

    class IdType(ObjectType):
        name = String()
        value = String()

    class PictureType(ObjectType):
        large = String()
        medium = String()
        thumbnail = String()

    gender = String()
    name = Field(NameType)
    location = Field(LocationType)
    email = String()
    login = Field(LoginType)
    dob = String()
    registered = String()
    phone = String()
    cell = String()
    id = Field(IdType)
    picture = Field(PictureType)
    nat = String()