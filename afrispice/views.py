from django.http import HttpResponse

def project_home(request):
    """
    View function for the project's home page.
    """
    message = "Welcome to AfriSpice, the home of all African meal recipes"
    return HttpResponse(message)