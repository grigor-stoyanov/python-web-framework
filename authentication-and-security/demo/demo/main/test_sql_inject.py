from demo.main.models import Todo

x = Todo()
# avoid sql injections by using the ORM
todos = Todo.objects.all()
# now we can type SQL
param = 'the; DROP DATABASE;'
todos = Todo.objects.raw('SELECT * FROM main_todo'
                         f'WHERE title LIKE "%s"',
                         (param,))
print(todos)
