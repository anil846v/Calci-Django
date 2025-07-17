from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'calci/index.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation')
        result = None

        if operation == 'ADD':
            result = num1 + num2
        elif operation == 'SUBTRACT':
            result = num1 - num2
        elif operation == 'MULTIPLY':
            result = num1 * num2
        elif operation == 'DIVISION':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'

        return render(request, 'calci/index.html', {'result': result})
    
    return HttpResponse("Invalid request")
