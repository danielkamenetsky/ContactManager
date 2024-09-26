from django.shortcuts import render, redirect

from.models import Contact
from .forms import ContactForm


def home(request):
    return render(request, 'contacts/home.html')



def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})




def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contacts_detail', pk=contact.id)
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

# def edit_contact(request, contact_id):
#     contact = get_object_or_404(Contact, id=contact_id)
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')  # Redirect to your contact list view
#     else:
#         form = ContactForm(instance=contact)

#     return render(request, 'contacts/edit_contact.html', {'form': form, 'contact': contact})