# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem
from django.urls import reverse

def index(request):

    # todo_items = TodoItem.objects.all()
    # print(todo_items)
    #
    # output = '<html><head></head><body>'
    # output += '<ul>'
    #
    # for todo_items in todo_items:
    #     output += f'<li>{todo_items.todo_text}</li>'
    #
    # output += '</ul>'
    # output += '</body></html>'
    # return HttpResponse(output)
    # #return HttpResponse('hello world!')

    todo_items = TodoItem.objects.all()

    context = {'todo_items': todo_items}

    return render(request, 'todo/index.html', context)




def temp(request):
    return HttpResponse('temp')

def savetodo(request):

    todo_text = (request.POST['todo_text'])

    todo_item = TodoItem(todo_text=todo_text)
    todo_item.save()

    #return HttpResponse('OK')
    return HttpResponseRedirect(reverse('todo:index'))

def completetodo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.completed = True
    todo_item.save()

    return HttpResponseRedirect(reverse('todo:index'))