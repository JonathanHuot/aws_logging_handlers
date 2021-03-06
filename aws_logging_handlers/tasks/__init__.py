class Task:
    def __init__(self, callable_func, *args, **kwargs):
        assert callable(callable_func), "First argument in task should be callable"
        self.callable_func = callable_func
        self.args = args
        self.kwargs = kwargs


def task_worker(q):
    while True:
        if not q.empty():
            task = q.get()
            if task == -1:
                return
            assert isinstance(task, (Task,)), "task should be of type `Task` only!"
            task.callable_func(*task.args, **task.kwargs)
            q.task_done()