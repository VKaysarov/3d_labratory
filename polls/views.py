from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from .forms import mainForm

def index(request):
    form = mainForm(request.POST or None)
    # coment = comentForm()

    if request.method == "POST" and form.is_valid():
    	form = form.save()
    	# coment = coment.save()

    return render(request, 'polls/index.html', context={'form': form})

def clip(request):
	return render(request, 'polls/clip.html')

def plan_work(request):
    return render(request, 'polls/plan_work.html')

def vis(request):
    return render(request, 'polls/vis.html')

def visualization(request):
    return render(request, 'polls/visualization.html')

def exteriors(request):
    return render(request, 'polls/3D Visualization/exteriors.html')

def interior(request):
    return render(request, 'polls/3D Visualization/interior.html')

def object_visualization(request):
    return render(request, 'polls/3D Visualization/object_visualization.html')

def modeling(request):
    return render(request, 'polls/3D Visualization/modeling.html')


