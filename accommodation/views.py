from django.shortcuts import render
from .forms import *
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def execute_query(query):
    result = None
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

def accommodations(request, destareaid):
    # Cek udah login atau belum. Kalo belum redirect ke login page
    query = f"SELECT * FROM ACCOMMODATION WHERE destareaid = {destareaid};"
    result = execute_query(query)
    # print(result) # debug
    return render(request, 'accommodation_list.html')

def accommodation_detail(request, destareaid, accommid):
    # Cek udah login atau belum. Kalo belum redirect ke login page
    query = f"SELECT * FROM ACCOMMODATION WHERE destareaid = {destareaid} AND id = {accommid};"
    result = execute_query(query)
    # print(result) # debug
    return render(request, 'accommodation_detail.html')

def accommodation_review(request, accommid):
    # Cek udah login atau belum. Kalo belum redirect ke login page
    query = f"SELECT * FROM ACCOMMODATION_REVIEW WHERE accommodationID = {accommid};"
    result = execute_query(query)
    # print(result) # debug
    return render(request, 'accommodation_review.html')

def add_accommodation_review(request, accommid):
    # Cek udah login atau belum. Kalo belum redirect ke login page
    return render(request, 'add_accommodation_review.html')