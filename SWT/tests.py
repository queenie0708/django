from django.test import TestCase
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Prj
import requests
import json


def getPrj():
   r= requests.get('http://10.75.10.254/getdeviceinfo.php')
   line= r.text
   obj = json.loads(line)
   i = 0
   while i < len(obj):
       prj = Prj()
       prj =Prj.object.create(name= obj[i]['nickname'] ,dut_id= obj[i]['dut_id'],sku_id = obj[i]['sku_id'])
       prj.save()
       i=i+1
       

