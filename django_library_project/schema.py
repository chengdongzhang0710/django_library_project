from graphene import Schema, ObjectType

import catalog.schema


class Query(catalog.schema.Query, ObjectType):
    pass


class Mutation(catalog.schema.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
