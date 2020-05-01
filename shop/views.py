from django.shortcuts import render, redirect,get_object_or_404

from django.http import HttpResponse
from .models import Restaurant,Item,Menu,Order,orderItem
from math import ceil
from collections import Counter


def index(request):
     
    return render(request, 'shop/main.html')

def restaurant(request):
    rest_obj = Restaurant.objects.all()

    return render(request, 'shop/restaurant.html',{'rest_obj': rest_obj})



def restuarantMenu(request,pk=None):

	menu = Menu.objects.filter(r_id=pk)
	rest = Restaurant.objects.filter(id=pk)

	items =[]
	for i in menu:
		item = Item.objects.filter(fname=i.item_id)
		for content in item:
			temp=[]
			temp.append(content.fname)
			temp.append(content.category)
			temp.append(i.price)
			temp.append(i.id)
			temp.append(rest[0].status)
			temp.append(i.quantity)
			items.append(temp)
	context = {
		'items'	: items,
		'rid' 	: pk,
		'rname'	: rest[0].rname,
		'rmin'	: rest[0].min_ord,
		'rinfo' : rest[0].info,
		'rlocation':rest[0].location,
	}
	return render(request,'shop/menu.html',context)

 
def checkout(request):
	if request.POST:
		addr  = request.POST['address']
		ordid = request.POST['oid']
		Order.objects.filter(id=int(ordid)).update(delivery_addr = addr,
                                                    status=Order.ORDER_STATE_PLACED)
		return redirect('/orderplaced/')
	else:	
		cart = request.COOKIES['cart'].split(",")
		cart = dict(Counter(cart))
		items = []
		totalprice = 0
		oid = Order()
		for x,y in cart.items():
			item = []
			it = Menu.objects.filter(id=int(x))
			if len(it):
				oiid=orderItem()
				oiid.item_id=it[0]
				oiid.quantity=int(y)
				oid.r_id=it[0].r_id
				oid.save()
				oiid.ord_id =oid
				oiid.save()
				totalprice += int(y)*it[0].price
				item.append(it[0].item_id.fname)
				it[0].quantity = it[0].quantity - y
				it[0].save()
				item.append(y)
				item.append(it[0].price*int(y))
			
			items.append(item)
		oid.total_amount=totalprice
		oid.save()
		context={
			"items":items,
			"totalprice":totalprice,
			"oid":oid.id
		}	
		return render(request,'shop/checkout.html',context)
def about(request):
    return render(request,'shop/about.html' )
    
def contact(request):
    return HttpResponse("This is contact page")
    
def orderplaced(request):
	return render(request,'shop/orderplaced.html',{})
    
def productView(request):
    return HttpResponse("This is product view page")
   
    
def search(request):
    return HttpResponse("This is search page")
