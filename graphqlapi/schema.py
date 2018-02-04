from graphene_django import DjangoObjectType
from todos.models import Todo, Author
from .helpers import raise_error_if_not_exist

import graphene

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class CreateAuthor(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, first_name, last_name):
        new_author = Author(first_name=first_name, last_name=last_name)
        new_author.save()
        return CreateAuthor(author=new_author)

class CreateTodo(graphene.Mutation):
    class Arguments:
        author_id = graphene.Int(required=True)
        text = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, author_id, text):
        raise_error_if_not_exist(Author, author_id)

        author = Author.objects.get(pk=author_id)
        new_todo = Todo(text=text, author=author)
        new_todo.save()
        return CreateTodo(todo=new_todo)

class UpdateTodoText(graphene.Mutation):
    class Arguments:
        todo_id = graphene.Int(required=True)
        new_text = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, todo_id, new_text):
        raise_error_if_not_exist(Todo, todo_id)

        edit_todo = Todo.objects.filter(pk=todo_id)
        edit_todo.update(text=new_text)

        return UpdateTodoText(todo=edit_todo.first())

class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)
    authors = graphene.List(AuthorType)
    todo_by_id = graphene.Field(TodoType, id=graphene.Int(required=True))
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))

    def resolve_todos(self, info):
        return Todo.objects.all()

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_todo_by_id(self, info, id):
        raise_error_if_not_exist(Todo, id)
        return Todo.objects.get(pk=id)            

    def resolve_author_by_id(self, info, id):
        raise_error_if_not_exist(Author, id)
        return Author.objects.get(pk=id)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_todo = CreateTodo.Field()
    update_todo_text = UpdateTodoText.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)