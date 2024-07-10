from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def sumNumbers(start_num, end_num):
    if start_num > end_num:
        start_num, end_num = end_num, start_num
    sum = 0
    for i in range(start_num, end_num + 1):
        sum += i
    return sum


@api_view(['Post'])
def sumNumbersView(request):
    if request.method == 'POST':
        start_num = request.data['start_num']
        end_num = request.data['end_num']
        result = sumNumbers(start_num, end_num)
        return Response({'result': result})

# def sorting_number(number_list):
#     sorted_list = []
#     while number_list:
#
#         min_number = min(number_list)
#         sorted_list.append(min_number)
#         number_list.remove(min_number)
#     return sorted_list
#
# def add_numbers(number_list):
#     sum = 0
#     for number in number_list:
#         sum += number
#     return sum