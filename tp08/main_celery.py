from celery import Celery

def main():
    app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="rpc://")
    # celery_tasks.add

    result = app.send_task("celery_tasks.add",args=(2,3))
    print(result.get())

if __name__=='__main__':
    main()
    