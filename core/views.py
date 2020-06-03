from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project
from datetime import datetime, timedelta
from .forms import AddProduct
from django.urls import reverse
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

@csrf_exempt
def compare(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    if request.method == 'POST':
        # extract data to pass it to url
        project_1 = request.POST['project_1']
        project_2 = request.POST['project_2']
        print(f'project 1 {project_1}')
        print(f'project 2 {project_2}')
        #return redirect('core.views.compare_projects', project_1=project_1, project_2=project_2)
        return redirect(
            f'search/data={project_1}+{project_2}'
            )

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
        
def compare_projects(request, project_1, project_2):
    project_1 = Project.objects.filter(id=project_1)[0]
    project_2 = Project.objects.filter(id=project_2)[0]

    cfy_1 = map(float, project_1.year_cash_flow.strip().split(','))
    var1 = [-project_1.capitale] + list(cfy_1)
    vaan1=npv(1, var1)
    cfy_2 = map(float, project_2.year_cash_flow.strip().split(','))
    var2 = [-project_2.capitale] + list(cfy_1)
    vaan2=npv(1, var2)

    context = {
        'project_1': project_1,
        'project_2': project_2,
        'vaan1': vaan1,
        'vaan2': vaan2,
    }
    return render(
        request,
        template_name='core/compare_projects.html',
        context=context,
        )

