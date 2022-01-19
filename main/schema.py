import graphene
from event import schema


class Query(schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
