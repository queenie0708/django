from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
import requests
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    prj= Prj.objects.all()
    version = Version.objects.all()
    return render(request, 'home.html', {'prj': prj,'version':version})


def get_Prj(request,pk):
   prj=get_object_or_404(Prj,pk=pk)
   r = requests.get('http://10.75.10.254/getbuildinfo.php?deviceid='+ prj.dut_id)
   line = r.text
   obj = json.loads(line)
   sw_version = list()
   i = 0
   while i < len(obj):
       sw_version.append(obj[i]['sw_version'])
       i = i + 1
   name= prj.name
   return render(request, 'getPrj.html', {'sw_version': sw_version, 'name': name})


def menu(request):
    prj = Prj.objects.all()
    version = Version.objects.all()
    return render(request, 'menu.html', {'prj': prj, 'version': version})

def jsMenu(request):
    prj = Prj.objects.all()
    return render(request, 'jsMenu.html', {'prj': prj})

def dropdown(request):
    prj = Prj.objects.all()

    return render(request, 'dropdown.html', {'prj': prj})



@csrf_exempt
def ajax_load_versions(request):
   dut_id= request.GET.get('dut_id')
   r = requests.get('http://10.75.10.254/getbuildinfo.php?deviceid=' + dut_id)
   line = r.text
   version = json.dumps(line)
   return JsonResponse(version, safe=False)

@csrf_exempt
def ajax_load_results(request):
   sw_version= request.GET.get('sw_version')
   r = requests.get('http://10.75.10.254/gettestresult.php?build=' + sw_version)
   line = r.text
   result = json.dumps(line)
   return JsonResponse(result, safe=False)