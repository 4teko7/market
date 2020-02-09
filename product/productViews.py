# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,render_to_response,get_object_or_404
from django.contrib import messages
from .productForms import *
from .models import Product
# from todo.models import Todo
from comment.models import Comment
from comment.commentForms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import UserProfile
import json

contex = {}


def check(req):
    from .productLang import lang2
    global context
    if(req.user.is_authenticated):
        context = {
            "lang":lang2
             }
    else:
        context = {
                    "lang":lang2
            }
# "allArticles":allArticles,"myTodos":myTodos,"myArticles":myArticles

# Create your views here.



# Create your views here.

@login_required(login_url="/users/login/")
def addProduct(req):
    from .productLang import lang2
    form = addProductForm()
    check(req)
    global context
    context['form'] = form
    if(req.method == "POST"):
        form = addProductForm(req.POST,req.FILES or None)
        print(req.FILES)
        if(form.is_valid()):
            product = form.save(commit = False)
            product.author = req.user
            product.save()
            messages.success(req,lang2['articleAdded'])
            return HttpResponseRedirect("/products/myproducts/")
        else:

            return render(req,"addpPoduct.html",context)
    else:
        return render(req,"addProduct.html",context)

@login_required(login_url="/users/login/")
def myProducts(req):
    check(req)
    products = Product.objects.filter(author = req.user)
    products = products.order_by("createdDate")
    global context
    context['products'] = products
    return render(req,"myproducts.html",context)





def productDetail(req,id):
    parsed = []
    global context
    commentForm = CommentForm()
    check(req)
    product = Product.objects.filter(id = id)
    print(product[0])
    if(not product):
        return render(req,"warnings/pagenotfound.html",context)
    
    comments = Comment.objects.filter(product = product[0])
    if(comments):
        comments = comments.order_by('createdDate')
        comments = comments[::-1]
    context['product'] = product[0]
    context['commentForm'] = commentForm



    for comment in comments:
        if(comment.comments2):

            parsed = json.loads(comment.comments2)
            for com in parsed:
                user = User.objects.get(username = com["author"])
                profile = UserProfile.objects.filter(user = user)
                if(profile):
                    if(profile[0].profileImage):
                        com["userImage"] = profile[0].profileImage.url
                    else:
                        com["userImage"] = None
                comment.comments2 = parsed
        user = User.objects.get(username = comment.author)
        profile = UserProfile.objects.filter(user = user)
        if(profile):
            if(profile[0].profileImage):
                comment.userImage = profile[0].profileImage.url
            else:
                comment.userImage = None


    
    context['comments'] = comments
    if(product[0].productImage):
        context["image"] = product[0].productImage.url
    if(product[0].isPrivate):
        return render(req,"warnings/productprivate.html",context)
    else:
        return render(req,"productdetail.html",context)

    # return HttpResponseRedirect('/products/myproducts/')

def allProducts(req):
    products = Product.objects.all()
    check(req)
    global context
    context['products'] = products
    return render(req,"allproducts.html",context)

@login_required(login_url="/users/login/")
def editProduct(req,id):
    global context
    from .productLang import lang2

    check(req)

    productOld = Product.objects.filter(id=id,author = req.user)
    if(not productOld):
        return render(req,"warnings/canteditproduct.html",context)

    form = addProductForm(initial={'title': productOld[0].title,'content':productOld[0].content,'isPrivate':productOld[0].isPrivate,'productImage':productOld[0].productImage})
    context['form'] = form
    context['id'] = id
    if(req.method == "POST"):

        form = addpPoductForm(req.POST,req.FILES)
        if(form.is_valid()):
            productOld[0].content = form.cleaned_data.get("content")
            productOld[0].title = form.cleaned_data.get("title")
            productOld[0].isPrivate = form.cleaned_data.get("isPrivate")
            if(form.cleaned_data.get("productImage")):
                productOld[0].productImage = form.cleaned_data.get("productImage")
            else:
                if(req.POST.get("productImage-clear")):
                    productOld[0].productImage = None

            productOld[0].save()
            messages.success(req,lang2['productUpdated'])
            return HttpResponseRedirect("/products/myproducts/")
        else:
            return render(req,"editproduct.html",context)
    else:

        if(productOld):
            if(productOld[0].isPrivate):
                if(productOld[0].author == req.user):
                    return render(req,"editproduct.html",context)
                else:
                    return render(req,"warnings/productprivate.html",context)
            else:
                return render(req,"editproduct.html",context)

@login_required(login_url="/users/login/")
def deleteProduct(req,id):
    from .productLang import lang2
    product = Product.objects.filter(id = id , author = req.user)
    if(not product):
        return render(req,"warnings/pagenotfound.html",context)
    else:
        product.delete()
        messages.success(req,lang2['productDeleted'])
        return HttpResponseRedirect('/products/myproducts/')


def buyProduct(req,id):
    product = Product.objects.filter(id = id)
    check(req)
    global context
    context['product'] = product
    return render(req,"buyproduct.html",context)

def searchProduct(req):
    global context
    from .productLang import lang2
    check(req)
    context['lang'] = lang2
    keywords = req.GET.get('keywords')
    if(keywords):
        products = Product.objects.filter(title__contains = keywords)
        context['products'] = products
    return render(req,'allproducts.html',context)
