# Djangoモジュール
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# 標準モジュール
import json
import random

# *******************
# 基本画面表示
# *******************
def init_request(request):
    
    return render(
        request,
        'api_test/index.html',
    )

# *******************
# 数字を返すだけのAPI
# *******************
@method_decorator(csrf_exempt)
def api_count_request(request):
    num = random.randint(0, 10000)
    
    ret = {
        'status_code': 200,
        'message': 'OK',
        'count': num,
    }
    # JSONに変換して戻す
    return JsonResponse(ret)
