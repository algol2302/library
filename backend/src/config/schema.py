import graphene
import library.schema


class Query(library.schema.Query, graphene.ObjectType):
    """
    Projects main Query class, this will inherit multiple queries.
    """
    pass


schema = graphene.Schema(query=Query)
