from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'myMembers' : myMembers, #'myMembers' is the name used in the template where as myMembers is the variable defined here  
                                 # key : value, thus: key is 'myMembers' and value would be 'Emil' and etc
    }

    return HttpResponse(template.render(context, request))