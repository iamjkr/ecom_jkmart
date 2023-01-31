from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View
from .models import Product, Customer
from django.db.models import Count
from .forms import UserRegistrationForm, CustomerProfileForm


# Create your views here.

def home_page(reuest):
    return render(reuest, 'index.html')

def about(reuest):
    return render(reuest, 'about.html')

def contact(reuest):
    return render(reuest, 'contact.html')



class CategoryView(View):
    def get(self, request,val):
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'category.html',locals())


class CategoryTitle(View):
    # def product_detail(request, title):
    #     product = Product.objects.get(title=title)
    #     return render(request, 'category.html', {'product': product})
    def get(self, request,val):
        products = Product.objects.filter(title=val)
        print(products)
        title = Product.objects.filter(category=products[0].category).values('title')
        print(title)
        return render(request, 'category.html',locals())


class CategoryDetail(View):
    def get(self, request,pk):
        product = Product.objects.get(id=pk)
        return render(request, 'product_detail.html',locals())


class RegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        #form.order_fields(field_order=['username','email','password1','password2'])
        return render(request, 'registraion.html',locals())
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data.get("username")}')
        else:
            messages.error(request, f'Invalid Information')
        return redirect('registration')


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm
        return render(request, 'profile.html',locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            location = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg_data =Customer(user=user,name=name,locality=location,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg_data.save()
            messages.success(request,'Profile Updated Successfully')
        else:
            messages.error(request, 'Invalid Information')
        return render(request, 'profile.html', locals())

def address(request):
    address = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', locals())


class UpdateAddress(View):
    # form_class = CustomerProfileForm
    # template_name = 'update_address.html'
    # def get(self, request, pk):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request, pk):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # Perform the update action here
    #         # For example, you could use the following code to update the address of a customer
    #         customer = Customer.objects.get(pk=pk)
    #         customer.address = form.cleaned_data['address']
    #         customer.save()
    #         return redirect('customer_list')
    #     else:
    #         return render(request, self.template_name, {'form': form}
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'update_address.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            address = Customer.objects.get(pk=pk)
            address.name = form.cleaned_data['name']
            address.locality = form.cleaned_data['locality']
            address.city = form.cleaned_data['city']
            address.mobile = form.cleaned_data['mobile']
            address.state = form.cleaned_data['state']
            address.zipcode = form.cleaned_data['zipcode']
            address.save()
            messages.success(request, 'Address Updated Successfully')
            return redirect('address')
        else:
            messages.error(request, 'Invalid Information')
            return render(request, 'update_address.html', locals())


class PasswordResetCompleteView(View):
    pass