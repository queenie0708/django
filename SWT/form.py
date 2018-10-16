from django import forms
from .models import *
import requests
import json

class SelectForm(forms.Form):
    r = requests.get('http://10.75.10.254/getdeviceinfo.php')
    line = r.text
    obj = json.loads(line)
    nickname = list()
    i = 0
    while i < len(obj):
        nickname.append(obj[i]['nickname'])
        i = i + 1
    PRJ_CHOICES = [(name, name) for name in nickname]

    PRJ_Select=forms.ChoiceField(choices=PRJ_CHOICES)

    List_swbuild=[]
    VERSION_CHOICE =forms.ChoiceField(choices=List_swbuild)


    class Meta:
        medel = Result
        fields = ('PRJ_Select','VERISON_Select')