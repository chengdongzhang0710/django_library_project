from graphene import InputObjectType, String, ID, Int
from graphene_django import DjangoObjectType

from reviews.models import Review


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        convert_choices_to_enum = False


class ReviewInputType(InputObjectType):
    id = ID()
    book = ID()
    user = ID()
    value = Int()
    comment = String()
