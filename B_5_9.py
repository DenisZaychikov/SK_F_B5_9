from time import time

class SecundomerCls(object):

    def __call__(self, num_runs):
        def decorator(func):
            def new_func():
                avg_time = 0
                for _ in range(num_runs):
                    start_time = time()
                    func()
                    avg_time += start_time
                stop_time = time()
                return stop_time - avg_time / num_runs
            return new_func
        return decorator
            
time_this = SecundomerCls()

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

print('Время потраченное на обработку функции:', f())
