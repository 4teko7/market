# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from .todoForms import *
from django.contrib import messages
from .models import Todo
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

context = {}

def check(req):

    from .todoLang import lang2
    global context
    if(req.user.is_authenticated):
        context = {
            "lang":lang2
             }
    else:
        context = {"lang":lang2}

@login_required(login_url="/users/login/")
def addTodo(req):
    from .todoLang import lang2
    form = addTodoForm()
    check(req)
    global context
    context['form'] = form
    allInfo(req)
    if(req.method == "POST"):
        print("POSTA GIRDI")
        form = addTodoForm(req.POST)
        if(form.is_valid()):
            content = form.cleaned_data.get("content")
            date = form.cleaned_data.get("date")
            newTodo = Todo(content = content , date = date,author = req.user)
            newTodo.save()
            messages.success(req,lang2['todoAdded'])
            return HttpResponseRedirect('/todos/mytodos/')
        else:
            return render(req,"addtodo.html",context)
    else:
        return render(req,"addtodo.html",context)



@login_required(login_url="/users/login/")
def editTodo(req,id):
    from .todoLang import lang2
    todo = Todo.objects.get(id = id)
    if(req.method == "POST"):
        form = addTodoForm(req.POST)
        if(form.is_valid()):
            content = form.cleaned_data.get("content")
            date = form.cleaned_data.get("date")
            todo.content = content
            todo.date = date
            todo.save()
            messages.success(req,lang2['todoAdded'])
            return HttpResponseRedirect('/todos/mytodos/')
        else:
            return HttpResponseRedirect('/todos/mytodos/')
    else:
        return HttpResponseRedirect('/todos/mytodos/')



@login_required(login_url="/users/login/")
def myTodos(req):

    form = addTodoForm()



    check(req)
    todos = Todo.objects.filter(author = req.user)
    todos = todos.order_by('date')
    todos = list(filter(lambda x: not x.iscompleted, todos))


    todosCompleted = Todo.objects.filter(author = req.user)
    todosCompleted = todosCompleted.order_by('date')
    todosCompleted = list(filter(lambda x: x.iscompleted, todosCompleted))
    todos += todosCompleted


    global context
    context['todos'] = todos
    context['form'] = form
    context['date'] = datetime.datetime.now()
    return render(req,"mytodos.html",context)

@login_required(login_url="/users/login/")
def completeTodo(req):
    from .todoLang import lang2

    id = req.POST.get('id')
    todo = Todo.objects.filter(id = id,author = req.user)
    if(todo):
        if(todo[0].iscompleted): todo[0].iscompleted = False
        else: todo[0].iscompleted = True
        todo[0].save()
        messages.success(req,lang2['todoCompleted'])
    return HttpResponseRedirect('/todos/mytodos/')

@login_required(login_url="/users/login/")
def deleteTodo(req,id):
    from .todoLang import lang2

    todo = Todo.objects.filter(id = id,author = req.user)
    todo.delete()
    messages.success(req,lang2['todoDeleted'])
    return HttpResponseRedirect('/todos/mytodos/')

