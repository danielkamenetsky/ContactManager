from django.shortcuts import render

from.models import Contact

def home(request):
    return render(request, 'home.html')



def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})



# def add_contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')

#         contact = Contact(name=name, email=email, phone=phone, address=address)
#         contact.save()

#         return render(request, 'contacts/contact_detail.html', {'contact': contact})
#     else:
#         return render(request, 'contacts/add_contact.html')
