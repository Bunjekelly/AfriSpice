from django.http import HttpResponse

def api_home(request):
    """
    View function for the home page.
    """
    message = "Welcome to AfriSpice, the home of all African meal recipes"
    return HttpResponse(message)
