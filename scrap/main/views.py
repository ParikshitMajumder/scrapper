from django.shortcuts import render,redirect
from django.contrib import messages
from . import scalper
from .models import price_data,product_name

# Create your views here.
def index(request):
    if request.method=='POST':
        url=request.POST.get('url')
        name=request.POST.get('name_class')
        price=request.POST.get('price_class')
        website=request.POST.get('website')

        if website == 'Flipkart':
            data=scalper.scalp_data.scalp_flipkart(url,name,price,website)
            if data:
                print("Saved Successfully")
                return redirect("/")
            else:
                messages.info(request,'Internal Server Error')
                print("Internal Server Error ")
                return redirect("/")
            #try:
              #scalper.scalp_data.scalp_flipkart(url,name,price,website)
            #except Exception as e :
                #messages.info(request,'Some exceptions occurred.')
                
                #print(e)
                #return redirect("/")

        else : 
            messages.info(request,'Website is not supported currently.')
            print("unknown website ")
            return redirect("/")

        return redirect("/")

    else:
      data=price_data.objects.all()
      names=product_name.objects.all()
      
      return render(request,'index.html',{"data" : data,"names":names})
