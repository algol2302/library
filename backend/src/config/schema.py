import graphene
import library.schema


class Query(library.schema.Query, graphene.ObjectType):
    """
    Projects main Query class, this will inherit multiple queries.
    """
    pass


class Mutation(library.schema.Mutation, graphene.ObjectType):
    """
    Projects main Mutation class, this will
    inherit multiple mutations.
    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
