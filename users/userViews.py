# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .userForms import *
from .models import UserProfile
from guests.models import GuestProfile
from order.models import Order
from todo.models import Todo
from product.models import Product
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
context = {}

def check(req):
    from .userLang import lang2
    global context
    if(req.user.is_authenticated):
        context = {
            "lang":lang2
             }
    else:
        context = {"lang":lang2}

@login_required(login_url="/users/login/")
def about(req,id):

    from .userLang import lang2
    check(req)
    global context
    user = User.objects.get(id = id)
    profile = UserProfile.objects.filter(user = user)
    if(profile):
        if(profile[0].profileImage):
            context['profileImage'] = profile[0].profileImage
        context['profile'] = profile[0]
        context['user'] = user
    return render(req,"about.html",context)

def registerUser(req):

    from .userLang import lang2
    check(req)
    global context

    form = registerForm()
    context['form'] = form

    if(req.method == "POST"):
        print("POSTA GIRDI")
        form = registerForm(req.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()
            login(req,newUser)
            messages.success(req,lang2['registered'])
            return redirect("mainPage")
        else:
            username = User.objects.filter(username = req.user.username)
            if(username):
                messages.warning(req,lang2['usernameExists'])
            return render(req,"register.html",context)
    else:
        return render(req,"register.html",context)


def loginUser(req):
    from .userLang import lang2
    check(req)
    global context

    form = loginForm()
    context['form'] = form
    if(req.method == "POST"):
        form = loginForm(req.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username,password = password)
            if(user):
                messages.success(req,lang2['loggedIn'])
                login(req,user)
                return redirect("mainPage")
            else:
                messages.info(req,lang2['invalidUser'])
                return render(req,"login.html",context)
        else:
            return render(req,"login.html",context)

    else:
        return render(req,"login.html",context)


def logoutUser(req):
    from .userLang import lang2
    check(req)
    global context

    logout(req)
    messages.success(req,lang2['logoutMessage'])
    return HttpResponseRedirect('/')

@login_required(login_url="/users/login/")
def editProfile(req):
    from .userLang import lang2
    check(req)
    global context

    user = User.objects.filter(username = req.user.username)
    form = ProfileForm(initial={'firstname': user[0].first_name,'lastname':user[0].last_name,'email':user[0].email})
    context['form'] = form
    return render(req,'editprofile.html',context)

@login_required(login_url="/users/login/")
def saveProfile(req):
    from .userLang import lang2
    check(req)
    global context

    user = User.objects.get(username = req.user.username)
    form = ProfileForm(req.POST)
    profile = UserProfile.objects.get(user=user)
    if(form.is_valid()):
        user.first_name = form.cleaned_data.get("firstName")
        user.last_name = form.cleaned_data.get("lastName")

        profile.firstName = form.cleaned_data.get("firstName")
        profile.lastName = form.cleaned_data.get("lastName")
        profile.phone = form.cleaned_data.get("phone")
        profile.address = form.cleaned_data.get("address")

        user.save()
        profile.save()
        messages.success(req,lang2['profileUpdated'])
        return HttpResponseRedirect("/users/about/"+str(user.id)+"/")
    else:
        return HttpResponseRedirect('/users/editprofile/')

def addProfileImage(req):
    from .userLang import lang2
    check(req)
    global context
    profile = UserProfile.objects.get(user=req.user)

    if(req.method == "POST"):
        form = addProfileImageForm(req.POST,req.FILES or None)
        if(form.is_valid()):
            if(form.cleaned_data.get("profileImage")):
                profile.profileImage = form.cleaned_data.get("profileImage")
                profile.save()
            else:
                if(req.POST.get("profileImage-clear")):
                    if(profile.profileImage):
                        profile.profileImage = None
                        profile.save()
            # Product.author = req.user

            messages.success(req,lang2['profilImageUpdated'])
            return HttpResponseRedirect("/users/about/"+str(req.user.id)+"/")
        else:

            return render(req,"addprofileimage.html",context)
    else:
        form = addProfileImageForm()
        if(profile):
            if(profile.profileImage):
                context['profileImage'] = profile.profileImage
                form = addProfileImageForm(initial={'profileImage': profile.profileImage})
        context['form'] = form
        return render(req,"addprofileimage.html",context)

@login_required(login_url="/users/login/")
def changePassword(req):
    from .userLang import lang2
    check(req)
    global context

    form = ChangePassword()
    context['form'] = form
    if(req.method == "POST"):
        form = ChangePassword(req.POST)
        if(form.is_valid()):
            oldPassword = form.cleaned_data.get("oldPassword")
            newPassword = form.cleaned_data.get("newPassword")
            newPasswordConfirm = form.cleaned_data.get("newPasswordConfirm")
            user = User.objects.get(username = req.user.username)
            print(user.check_password(oldPassword))
            if(not user.check_password(oldPassword)):
                messages.warning(req,lang2['oldPasswordIncorrect'])
                return HttpResponseRedirect('/users/changepassword/')
            elif(not (oldPassword or newPassword or newPasswordConfirm)):
                messages.warning(req,lang2['fillFields'])
                return HttpResponseRedirect('/users/changepassword/')
            elif(newPassword != newPasswordConfirm):
                messages.warning(req,lang2['newsdiff'])
                return HttpResponseRedirect('/users/changepassword/')
            else:
                user.set_password(newPassword)
                user.save()
                login(req,user)
                messages.warning(req,lang2['passwordChanged'])
                return HttpResponseRedirect('/')
        else:
            messages.warning(req,lang2['formInvalid'])
            return HttpResponseRedirect('/users/changepassword/')
    else:
        return render(req,"changepassword.html",context)


@login_required(login_url="/users/login/")
def changeUsername(req):
    from .userLang import lang2
    check(req)
    global context

    form = ChangeUsername()
    context['form'] = form
    if(req.method == "POST"):
        form = ChangeUsername(req.POST)
        if(form.is_valid()):
            newUsername = form.cleaned_data.get("newUsername")
            user = User.objects.filter(username = newUsername)

            if(user):
                messages.warning(req,lang2['usernameExists'])
                form = ChangeUsername(initial = {'username':newUsername})
                context['form'] = form
                return render(req,'changeusername.html',context)

            else:
                req.user.username = newUsername
                req.user.save()
                messages.warning(req,lang2['usernameChanged'])
                return HttpResponseRedirect('/')
        else:
            messages.warning(req,lang2['formInvalid'])
            return HttpResponseRedirect('/users/changeusername/')
    else:
        return render(req,"changeusername.html",context)

@login_required(login_url="/users/login/")
def profile(req,id):
    from .userLang import lang2
    check(req)
    global context

    user = User.objects.get(id = id)
    context['user'] = user
    profile = UserProfile.objects.filter(user = user)
    if(profile):
        if(profile[0].profileImage):
            context['profileImage'] = profile[0].profileImage
    return render(req,'profile.html',context)


def buyProduct(req,id):
    from .userLang import lang2
    check(req)
    global context

    product = Product.objects.get(id = id)

    if(req.user.is_authenticated):
        profile = UserProfile.objects.get(user = req.user)
        form = buyProductForm(initial={'firstName': profile.firstName,'lastName':profile.lastName,'phone':profile.phone,"address":profile.address,"productAmount":1})
    else:form = buyProductForm()
    context['form'] = form
    context['product'] = product
    if(req.method == "POST"):
        form = buyProductForm(req.POST)
        if(form.is_valid()):


            if(req.user.is_authenticated):
                profile.firstName = req.POST.get("firstName")
                profile.lastName = req.POST.get("lastName")
                profile.phone = req.POST.get("phone")
                profile.address = req.POST.get("address")
                req.user.first_name = req.POST.get("firstName")
                req.user.last_name = req.POST.get("lastName")
                req.user.save()
                order = Order(user = req.user,product = product,title = product.title,productImage = product.productImage,productAmount = req.POST.get("productAmount"),totalPrice = float(req.POST.get("productAmount")) * product.productPrice,orderedDate=datetime.datetime.now())
                order.save()
                profile.currentOrders.add(order)
                profile.save()
            else:
                guest = GuestProfile(firstName = req.POST.get("firstName"),lastName = req.POST.get("lastName"),phone = req.POST.get("phone"),address = req.POST.get("address"))
                guest.save()
                order = Order(guestProfile = guest,product = product,title = product.title,productImage = product.productImage,productAmount = req.POST.get("productAmount"),totalPrice = float(req.POST.get("productAmount")) * product.productPrice,orderedDate=datetime.datetime.now(),isGuest = True)
                order.save()
            product.sold += int(req.POST.get("productAmount"))
            product.save()
            messages.warning(req,lang2['orderReceived'])

            return HttpResponseRedirect('/')
        else:
            messages.warning(req,lang2['formInvalid'])
            return HttpResponseRedirect('/users/buyproduct/'+str(id)+"/")
    else:
        return render(req,"buyproduct.html",context)


def preparing(req,id):
    from .userLang import lang2
    order = Order.objects.get(id = id)
    order.orderStatus = "Hazırlanıyor..."
    order.save()
    return HttpResponseRedirect("/products/allorders/")

def orderReceived(req,id):
    from .userLang import lang2
    order = Order.objects.get(id = id)
    order.orderStatus = "Sipariş Alındı..."
    order.save()
    return HttpResponseRedirect("/products/allorders/")

def shipped(req,id):
    from .userLang import lang2
    order = Order.objects.get(id = id)
    order.orderStatus = "Sipariş Gönderildi..."
    order.save()
    return HttpResponseRedirect("/products/allorders/")

def delivered(req,id):
    from .userLang import lang2
    order = Order.objects.get(id = id)
    order.orderStatus = "Sipariş Teslim Edildi..."
    order.save()
    return HttpResponseRedirect("/products/allorders/")

def completed(req,id):
    from .userLang import lang2
    order = Order.objects.get(id = id)
    order.orderStatus = "Sipariş Tamamlandı..."
    order.isFinished = True
    if(order.isGuest):
        pass
    else:
        profile = UserProfile.objects.get(user = order.user)
        profile.currentOrders.remove(order)
        profile.completedOrders.add(order)
    order.save()
    return HttpResponseRedirect("/products/allorders/")

