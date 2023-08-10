from django.shortcuts import redirect, render
from myapp.forms import ProjectForm
from .models import ProjectDetail


def storedata(request):
    if request.method == "POST":
        Form = ProjectForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('/myapp/showdata')
        else:
            Form = ProjectForm()
    return render(request,'student_project.html', {'Form' : Form})

        

def view_data(request):
    return render(request,'student_project.html')

def showdata(request):
    students = ProjectDetail.objects.all()
    return render(request,"show.html",{'students':students})
    
def deldata(request , roll):
    data = ProjectDetail.objects.get(roll=roll)
    data.delete()
    return redirect('/myapp/showdata')

def editdata(request,roll):
    data = ProjectDetail.objects.get(roll=roll)
    return render(request,'edit.html',{'data' : data})

def editrecord(request, roll):
    data = ProjectDetail.objects.get(roll=roll)
    form = ProjectForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect('/myapp/showdata')
    return render(request,'edit.html',{'data': data})

