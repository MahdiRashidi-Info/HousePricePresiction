import pandas as pd
import os
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse


file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance/static/addresses.csv')
def examine_view(request):

    df = pd.read_csv(file_path)      
    original_addresses = df['Original_Address'].tolist()
    return render(request, 'main_form.html' ,{'city' : original_addresses})


def form_submit_view(request):

    if request.method == 'POST':
        print(request.POST)
        
        state = request.POST.get('state')
        # print(state)
        
        
        return HttpResponse('Your data has been sent')
    else:
        return HttpResponse('Not allowed to call!')
    
    # return render(request, 'result.html')