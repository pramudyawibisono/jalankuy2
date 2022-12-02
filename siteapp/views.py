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

def sites(request, destareaid):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM SITE WHERE destareaid = {destareaid};"
    site_list = execute_query(query)
    # print(site_list) # debug

    query = f"SELECT name FROM DESTINATION_AREA WHERE ID = {destareaid}"
    dest_area_name = execute_query(query)[0][0]
    # print(dest_area_name) # debug

    context = {'site_list': site_list, 'dest_area_name': dest_area_name}
    print(context) # debug

    return render(request, 'site_list.html', context)

def site_detail(request, destareaid, siteid):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    query = f"SELECT * FROM SITE WHERE destareaid = {destareaid} AND id = {siteid};"
    site = execute_query(query)[0]
    # print(site) # debug

    query = f"SELECT * FROM SITE_REVIEW WHERE siteid = {siteid};"
    reviews = execute_query(query)
    # print(reviews) # debug

    query = f"SELECT name FROM DESTINATION_AREA WHERE ID = {siteid}"
    dest_area_name = execute_query(query)[0][0]
    # print(dest_area_name) # debug

    context = {
        'site': site, 
        'reviews': reviews, 
        'dest_area_name': dest_area_name,
        'ids': [destareaid, siteid]
        }
    print(context) # debug

    return render(request, 'site_detail.html', context)

def add_site_review(request, destareaid, siteid):
    # Cek udah login atau belum. Kalo belum, redirect ke login page
    reviewer = 'pram2' # debug, dummy value 
    if request.method == 'POST':
        form = SiteReviewForm(request.POST)
        if form.is_valid():
            score = int(form.cleaned_data['score'])
            comment = form.cleaned_data['comment']
            query = f"INSERT INTO SITE_REVIEW VALUES (\
                DEFAULT, {siteid}, '{reviewer}', {score}, '{comment}');"
            with connection.cursor() as cursor:
                cursor.execute(query)
            print(f"Sukses menambahkan review") # debug
            return HttpResponseRedirect(f'/destination-area/{destareaid}/sites/{siteid}')
    else:
        form = SiteReviewForm()

    return render(request, 'add_site_review.html', {'form': form})