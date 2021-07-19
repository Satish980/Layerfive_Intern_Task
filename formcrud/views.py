## import statements
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import HttpResponse
from formcrud.models import Details


# Create your views here.

@csrf_exempt
## route for displaying data
def index(response):
    try:
        ## retrieving data from database
        details = Details.objects.all()
        return render(response,"index.html",{"DetailsList":details})
    ## exception case
    except Exception as e:
        return HttpResponse(str(e))
    
# route for adding details
def formApi(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        addLine1 = request.POST['addline1']
        addLine2 = request.POST['addline2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        ## retrieving data from POST request and adding it into database
        try:
            user = Details(fname = fname, lname = lname, email = email,
                           phone = phone, addressLine1 = addLine1, addressLine2 = addLine2,
                           city = city, state = state, zipcode = zipcode)
            ## saving into database
            user.save()
            ## console methods
            print("FormApi Method Called")
            print(user)
            details = Details.objects.all()
            return render(request,"index.html",{"DetailsList":details})
        ## exceptional case
        except Exception as e:
            return HttpResponse(str(e))
    return render(request,"add.html")
        