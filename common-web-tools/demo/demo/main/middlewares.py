import time


def measure_time_middleware(get_response):
    def middleware(request):
        # allows us to attach properties to request
        request.profile = {
            'name': 'Doncho'
        }
        start_time = time.time()
        # connect with Django pipeline
        # move on to the next middleware or view!
        response = get_response(request)
        end_time = time.time()
        print(f'Executed in {end_time - start_time}s')
        # middlewares gives us abstract functionalities to all views

    return middleware
