# Project Title

Testing the waters of GraphQL. Thought I'd create a simple backend in Django utilising GraphQL.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this project you will need to have Python 3 installed on your machine. Just Google how to install it for your platform, but unless you are a Windows user, you'll probably have it installed already.

### Installing

To setup a dev environment for this project you will need to install pipenv. After this you'll need to tell it to install all dependencies on the Pipfile.lock and to create a virtualenv using Python 3.

Just run these steps on your terminal/command line after you cd to the project folder.

```
pip install pipenv
pipenv install --three
```

After this you are ready to run the app. Just run ```pipenv run python manage.py runserver``` inside the project directory.

## Heroku app

You can find this project on heroku by following https://graphql-django.herokuapp.com/graphiql/ and checking out the documentation or running queries. Go nuts!

## Built With

* [Django](https://docs.djangoproject.com/en/2.0/) - The web framework used
* [pip](https://pypi.python.org/pypi/pip) - Dependency Management
* [pipenv](https://docs.pipenv.org/) - Packaging tool and virtualenv management
* [GraphQL](http://graphql.org/learn/) - Used for backend queries
* [Graphene Django](http://docs.graphene-python.org/projects/django/en/latest/) - Integration of GraphQL in Django app

## Contributing

This project was just a quick test of GraphQL, but if you want to add more stuff to it, feel free to contribute. I don't have a standard for contributions as I don't see this project as something to be worked on except for testing GraphQL, to be honest.

## Authors

* **Gustavo Parreira** - *Initial work* - [Gustash](https://github.com/Gustash)

See also the list of [contributors](https://github.com/Gustash/DjangoGraphQL/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
