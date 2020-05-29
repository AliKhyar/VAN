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
        capitale = float(form.get('capitale'))
        duration = timedelta(days=int(form.get('duration')))
        cfy = form.get('cfy')
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
        return redirect(f'compare/data=<project_1>vs<project_2>')

    return render(
        request,
        template_name='core/compare.html',
        context=context,
        )
def npv(taux, var):
    
    total = 0.0
    for i, var in enumerate(var):
        total += var / (1 + taux)**i
    return total

def irr(var, iterations=100):
    rate = 1.0
    investment = var[0]
    for i in range(1, iterations+1):
        rate *= (1 - npv(rate, var) / investment)
    return rate
def payback_of_investment(investment, cashflows):
    
    total, years, cumulative = 0.0, 0, []
    if not cashflows or (sum(cashflows) < investment):
        return 0 #raise Exception("insufficient cashflows")
    for cashflow in cashflows:
        total += cashflow
        if total < investment:
            years += 1
        cumulative.append(total)
    A = years
    B = investment - cumulative[years-1]
    C = cumulative[years] - cumulative[years-1]
    return A + (B/C)

def project_detail(request, project_id):
    project = Project.objects.filter(id=project_id)[0]
    cfy = map(float, project.year_cash_flow.strip().split(','))
    var = [-project.capitale] + list(cfy)
    taux = project.taux_actualisation
    capitale = project.capitale
    #print(project.year_cash_flow.strip().split(','))
    #################
    ##van

    #####

    ##tir

    #####
    vaan=npv(1, var)
    vaan_text = "Net present value of the investment:%3.2f"%vaan

    tiir=irr(var)
    tiir_text = "Net present value of the investment:%3.2f"%tiir

    drci=payback_of_investment(capitale, cfy)
    drci_text = "Net present value of the investment:%3.2f"%drci
    
    context = {
        'project':project,
        'van':1,
        'tir':1,
        'vaan_text':vaan_text,
        'drci':drci,
        'tiir_text':tiir_text,
        'drci_text':drci_text,
    }
    return render(
        request=request,
        template_name='core/project_detail.html',
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