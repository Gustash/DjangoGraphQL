from graphene import Mutation, String, Int, Field
from todos.models import Author, Todo

from .types import AuthorType, TodoType

class CreateAuthor(Mutation):
    class Arguments:
        first_name = String(required=True)
        last_name = String(required=True)

    author = Field(AuthorType)

    def mutate(self, _, first_name, last_name):
        new_author = Author(first_name=first_name, last_name=last_name)
        new_author.save()
        return CreateAuthor(author=new_author)

class CreateTodo(Mutation):
    class Arguments:
        author_id = Int(required=True)
        text = String(required=True)

    todo = Field(TodoType)

    def mutate(self, _, author_id, text):
        raise_error_if_not_exist(Author, author_id)

        author = Author.objects.get(pk=author_id)
        new_todo = Todo(text=text, author=author)
        new_todo.save()
        return CreateTodo(todo=new_todo)

class UpdateTodoText(Mutation):
    class Arguments:
        todo_id = Int(required=True)
        new_text = String(required=True)

    todo = Field(TodoType)

    def mutate(self, _, todo_id, new_text):
        raise_error_if_not_exist(Todo, todo_id)

        edit_todo = Todo.objects.filter(pk=todo_id)
        edit_todo.update(text=new_text)

        return UpdateTodoText(todo=edit_todo.first())