def first_middleware(get_response):
    print("One thime initialization")
    
    def first_func(request):
        print("Before views")
        response = get_response(request)
        print("After views")
        return response
    return first_func