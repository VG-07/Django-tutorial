from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product , Category
from .models import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

# Create your views here.
# def index(request):
#     prds=Product.get_all_Product();
#     return render(request,'index.html',{'products': prds})

# def index(request):
#     # Retrieve all products
#     products = Product.objects.all();
#     categories = Category.objects.all()
#     data={}
#     data['products']=products
#     data ['categories']= categories
#     # Pass the products to the template
#     return render(request, 'index.html', data)

# def index(request):
#     # Retrieve all products
#     products = Product.objects.all();
#     categories = Category.objects.all()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = products.objects.all()
#         return render(request, 'index.html',products)
#     data={}
#     data['products']=products
#     data ['categories']= categories
#     # Pass the products to the template
#     return render(request, 'index.html', data)


class Index(View):
      def post (self,request):
             product = request.POST.get('product')
             cart = request.session.get("cart")
             if cart:
                    quantity = cart.get(Product)
                    if quantity:
                           cart[product] = quantity + 1
                    else:
                        cart[product] = 1
             else:
                    cart = {}
                    cart[product]=1
             request.sesseion['cart'] = cart
             return redirect('homepage')

                


      def get(self, request):
             products = Product.objects.all()
             
             category_id = request.GET.get('category')
             categories = Category.objects.all()
             
             if category_id:
                     products = Product.objects.filter(category_id=category_id)
                     
             data = {
                     'products': products,
                     'categories': categories
             }
             
             # Pass the products to the template
             return render(request, 'index.html', data)
                        

                
             



class Signup(View):
      def get(self,request):
            return render(request,'signup.html')
      def post(self, request):
            postData = request.POST
            first_name =postData.get('firstname')
            last_name = postData.get('lastname')
            phone = postData.get('phone')
            email = postData.get('email')
            password = postData.get('password')
            
            # validation

            value = {
                "first_name": first_name,
                "last_name" :last_name,
                "phone": phone,
                "email" : email    
            } 
            #customer Object
            error_message=None
            customer =Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
            error_message=self.validateCustomer(customer)

        
        # saveing
            if not error_message: 
                print(first_name, last_name,phone,email,password)
                customer.password = make_password(customer.password) # for the password show in ####
                customer.register() #if i want  the write save()
                return redirect('homepage')
            else: # if error then go to the sign-up page  
                data = {
                    'error' : error_message,
                    'values' :value
                }
                return render(request,'signup.html', data) 
        
        
      def validateCustomer(self,customer):
            error_message=None
            if (not customer.first_name ):
                    error_message="first Name Requred !!"
            elif len(customer.first_name)<=4:
                    error_message="First Name must be 4 char log or more"
            elif (not customer.last_name):
                    error_message="last name Requred !!"
            elif len(customer.last_name)<= 4:
                    error_message="First Name must be 4 char log or more"
            elif (not customer.phone):
                    error_message="Phone number Requred !!"
            elif len(customer.phone)< 10:
                    error_message="Number must be 10 digit !!"
                
            elif len(customer.password)< 6:
                    error_message="password Requred More than ^ digit"
            elif len(customer.email) < 10:
                    error_message="Email requred !!"
            elif customer.isExists():
                    error_message="Email address allready Exist"
        
        

class Login(View):
      def get(self, request):
            return render(request,'login.html')
      def post(self,request):
            email =request.POST.get('email')
            password =request.POST.get('password')
            customer= Customer.get_customer_by_email(email)
            error_massage =None
            if customer:
                  flag=check_password(password,customer.password) #check password
                  if flag: 
                        request.session['customer_id'] = customer.id
                        request.session['email'] = customer.email
                        return redirect('homepage')
                  else:
                        error_massage="Email or password invalid "
            else:
                  error_massage="Email or password invalid "
            return render(request,'login.html',{"error":error_massage}) # if wrong password then redirect in login page and show pop pop



