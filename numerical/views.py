from django.http import request
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from braces import views
from .utils import (
    areBracketsBalanced,
    evaluate
)


class Home(View):
    def get(self, *args, **kwargs):
        return render(self.request, template_name='Home.html')


@method_decorator(csrf_exempt, name='dispatch')
class Calculate(views.JSONResponseMixin, views.AjaxResponseMixin, View):
    def post_ajax(self, request, *args, **kwargs):
        equation_string = request.POST.get('equation_string')
        print(equation_string)
        message = ''
        whitelist = set('()')
        bracket_string = ''.join([c for c in equation_string if c in whitelist])
        result = None
        if equation_string:
            status = 200
            if areBracketsBalanced(bracket_string):
                message = "Calculation Successful"
                result = evaluate(equation_string)
            else:
                message = "Incorrect Bracket Placement"
                status = 400
            return self.render_json_response({'status': status, 'message': message, 'result': result})
        else:
            message = "No Equation Received"
            return self.render_json_response({'status': 400, 'message': message})
