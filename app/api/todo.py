from app.api import api


@api.route('/v1.0/todos')
def todo_list():
    pass


@api.route('/v1.0/todo/<id>')
def todo_item(id):
    pass
