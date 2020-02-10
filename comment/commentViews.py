# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,render_to_response
from django.contrib import messages

from comment.commentForms import *
from product.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import UserProfile
import json
# Create your views here.


context = {}



def check(req):
    from .commentLang import lang2
    global context
    if(req.user.is_authenticated):
        context = {
            'lang':lang2
             }
    else:
        context = {"lang":lang2}

@login_required(login_url="/users/login/")
def addComment(req,id):
    from .commentLang import lang2
    form = CommentForm()
    if(req.method == "POST"):
        form = CommentForm(req.POST)
        if(form.is_valid()):
            comment = form.save(commit = False)

            comment.author = req.user
            comment.product = Product.objects.filter(id = id)[0]
            comment.save()
            messages.success(req,lang2['commentAdded'])
            return HttpResponseRedirect("/products/productdetail/"+id + "/")
        else:
            messages.success(req,lang2['formInvalid'])
            return HttpResponseRedirect("/products/productdetail/"+id + "/")
@login_required(login_url="/users/login/")
def addCommentComment(req,id):
    from .commentLang import lang2
    form = CommentForm(req.POST)
    productId = req.POST.get("productId")
    print("PRoduct ID : ",productId)
    user = User.objects.get(username = req.user.username)
    profile = UserProfile.objects.filter(user = user)


    if(form.is_valid()):
        superComment = Comment.objects.get(id = id)
        content = form.cleaned_data.get("content")
        con = {"author":req.user.username,"content":content,"id":int(id)}
        if(profile):
            if(profile[0].profileImage):
                con = {"author":req.user.username,"content":content,"id":int(id),"userImage":profile[0].profileImage.url}

        if(superComment.comments2):
            com = json.loads(superComment.comments2)
            com.append(con)
        else:
            com = []
            com.append(con)

        superComment.comments2 = json.dumps(com)
        # print("SUPER COMMENT : ",superComment.comments2)
        superComment.save()
        messages.success(req,lang2['commentAdded'])
        
        return HttpResponseRedirect("/products/productdetail/" + productId + "/")
    else:
        messages.info(req,lang2['Comment is not Added'])
        return HttpResponseRedirect("/products/productdetail/" + productId + "/")

