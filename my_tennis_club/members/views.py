from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'myMembers' : myMembers, #'myMembers' is the name used in the template where as myMembers is the variable defined here  
                                 # key : value, thus: key is 'myMembers' and value would be 'Emil' and etc
                                 # 'myMembers' in HTML gets replaced with MyMembers object.
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    myMember = Member.objects.get(id=id) # left side is part of get function. Can also work with pk (primary key). Right side ID is from our defined parameter.
    template = loader.get_template('details.html')
    context = {
        'myMember' : myMember,
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits' : ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))