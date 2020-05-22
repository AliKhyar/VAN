from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project
from datetime import datetime
from .forms import AddProduct

# Create your views here.

def homepage(request):
    context = {}
    #return HttpResponse('Homepage')
    return render(
        request,
        template_name='core/homepage.html',
        context=context,
        )

@csrf_exempt
def add(request):
    f = AddProduct()
    if request.method == 'POST':
        add_project(request)
    return render(
        request,
        template_name='core/add.html',
        context={
            'form':f,
            },
        )

def compare(request):
    context = {}
    #return HttpResponse('Homepage')
    return render(
        request,
        template_name='core/compare.html',
        context=context,
        )
        
## to add comment
def add_project(request):
    form = request.POST
    name = form["name"]
    # description = form["description"]
    # start = form["start"].split('-')
    # st = ['0054', '12', '08']
    # std = datetime.date(st[0], st[1], st[2])
    #start = datetime.date(*(int(s) for s in form["start"].split('-'))) 
    # end = datetime.date(*(int(s) for s in form["end"].split('-')))
    # cfy = form["cfy"]
    # taux = form["taux"]
    # print(std)
    # print(type(std))
    # new_project = Project(
    #     name = name, description=description, Dure_start=start, 
    #     Duree_end=end, year_cash_flow=int(cfy), taux_actualisation=int(taux))
    # new_project.save()
    # if True:
    #     comment=form.data['comment']
    #     new_comment = Comment(forum=forum_id, user=request.user, body=comment, created=datetime.datetime.now() )
    #     new_comment.save()

    #     return redirect(f'{exo.type_exo}/{exo.slug}')
        