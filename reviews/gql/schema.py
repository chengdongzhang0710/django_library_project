from graphene import ObjectType, Schema

from .mutations import ReviewCreate, ReviewUpdate, ReviewDelete


class Mutation(ObjectType):
    review_create = ReviewCreate.Field()
    review_update = ReviewUpdate.Field()
    review_delete = ReviewDelete.Field()


schema = Schema(mutation=Mutation)
