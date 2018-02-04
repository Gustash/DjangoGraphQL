from graphql import GraphQLError

def raise_error_if_not_exist(model, id):
    if not model.objects.filter(pk=id).exists():
        raise GraphQLError("No {0} exists with id {1}.".format(model.__name__, id))