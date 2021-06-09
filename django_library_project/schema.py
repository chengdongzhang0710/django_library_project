from graphene import Schema, ObjectType

import catalog.schema
import users.gql.schema


class Query(catalog.schema.Query, users.gql.schema.Query, ObjectType):
    pass


class Mutation(catalog.schema.Mutation, users.gql.schema.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
