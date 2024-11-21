from django.shortcuts import render
from .models import DisplayData
def displaydata(request):
    if request.method == 'GET':
        data = DisplayData.objects.all()   #[---,---,---]
        return render(request,'displaydata.html', {'nth':data})
    else:
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        email1 = request.POST.get('email')
        mobile1 = request.POST.get('mobile')
        qualification1 = request.POST.get('qualification')
        percentage1 = request.POST.get('percentage')
        location1 = request.POST.get('location')
        DisplayData(
            first_name = fname1,
            last_name = lname1,
            email = email1,
            mobile = mobile1,
            qualification = qualification1,
            percentage = percentage1,
            location = location1
        ).save()
        data = DisplayData.objects.all()
        return render(request, 'displaydata.html', {'nth':data})
