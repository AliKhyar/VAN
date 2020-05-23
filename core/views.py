from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project
from datetime import datetime, timedelta
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
    add_form = AddProduct()
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        description = form.get('description')
        capitale = int(form.get('capitale'))
        duration = timedelta(days=int(form.get('duration')))
        cfy = int(form.get('cfy'))
        taux = float(form.get('taux'))
        try:
            new_project = Project(
                nom = name, description=description, capitale=capitale,
                duration=duration, year_cash_flow=cfy, taux_actualisation=taux)
            new_project.save()

        except:
            print('saving failed')
    return render(
        request,
        template_name='core/add.html',
        context={
            'form':add_form,
            },
        )

def compare(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    if request.method == 'POST':
        # extract data to pass it to url
        project_1 = request.POST['project_1']
        project_2 = request.POST['project_2']
        # redirect(search_info(request,bac_plus, department, city))  #, kwargs={'request':request,'bac_plus':bac_plus, 'department':department, 'city':city})
        return redirect(f'compare/data={project_1}vs{project_2}')

    return render(
        request,
        template_name='core/compare.html',
        context=context,
        )
        
def compare_projects(request, project_1, project2):
    project_1 = Project.objects.filter(id=project_1)[0]
    project2 = Project.objects.filter(id=project2)[0]

    
    ""
    pass



# print(f"type name is {type(name)}")
    # print(f"type description is {type(description)}")
    # print(f"type capitale is {type(capitale)}")
    # print(f"type duration is {type(duration)}")
    # print(f"type cfy is {type(cfy)}")
    # print(f"type taux is {type(taux)}")