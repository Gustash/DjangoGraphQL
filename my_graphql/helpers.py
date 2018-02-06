from graphql import GraphQLError
from collections import namedtuple
from graphqlapi.settings import VALID_NATIONALITIES

import json

def raise_error_if_not_exist(model, _id):
    if not model.objects.filter(pk=_id).exists():
        raise GraphQLError("No {0} exists with id {1}.".format(model.__name__, _id))

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

def raise_error_if_not_valid_nat(nat_list):
    non_valid = set([nat.lower() for nat in nat_list]) - set(VALID_NATIONALITIES)
    # is_valid = set([nat.lower() for nat in nat_list]).issubset(VALID_NATIONALITIES)
    if non_valid:
        non_valid_str = ', '.join([non_valid_str.lower() for non_valid_str in non_valid])
        raise GraphQLError("Nationalities {0} are not valid".format(non_valid_str))

def raise_error_if_page_and_no_seed(seed, page):
    if page > 1 and not seed:
        raise GraphQLError(
"Page {0} will have random values if no seed is provided, so there is no point in fetching a specific page" \
            .format(str(page)))