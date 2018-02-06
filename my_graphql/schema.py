from .types import TodoType, AuthorType, UserType
from .mutations import CreateTodo, CreateAuthor, UpdateTodoText
from .helpers import raise_error_if_not_exist, json2obj, raise_error_if_not_valid_nat, raise_error_if_page_and_no_seed

from graphqlapi.settings import RANDOMUSER_API_VERSION
from todos.models import Author, Todo

import graphene
import requests
import json

class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)
    authors = graphene.List(AuthorType)
    todo = graphene.Field(TodoType, _id=graphene.Int(required=True))
    author = graphene.Field(AuthorType, _id=graphene.Int(required=True))
    users = graphene.List(
        UserType, 
        results=graphene.Int(default_value=1), 
        gender=graphene.String(default_value=''),
        nat=graphene.List(graphene.String, default_value=[]),
        seed=graphene.String(default_value=''),
        page=graphene.Int(default_value=1)
    )

    def resolve_todos(self, _):
        return Todo.objects.all()

    def resolve_authors(self, _):
        return Author.objects.all()

    def resolve_todo(self, _, _id):
        raise_error_if_not_exist(Todo, _id)
        return Todo.objects.get(pk=_id)            

    def resolve_author(self, _, _id):
        raise_error_if_not_exist(Author, _id)
        return Author.objects.get(pk=_id)

    def resolve_users(self, _, results, gender, nat, seed, page):
        raise_error_if_not_valid_nat(nat)
        raise_error_if_page_and_no_seed(seed, page)
        nat_str = ','.join(nat)
        url = 'https://randomuser.me/api/{0}/?results={1}&gender={2}&nat={3}&seed={4}&page={5}' \
            .format(RANDOMUSER_API_VERSION, results, gender, nat_str, seed, str(page))
        response = requests.get(url).json()['results']
        return json2obj(json.dumps(response))

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_todo = CreateTodo.Field()
    update_todo_text = UpdateTodoText.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)