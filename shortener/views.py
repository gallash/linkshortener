from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Link, ShortLink
from .forms import LinkForm
import random
import string
import requests 


# ==== Some thoughts on the project:
# Periodically run a crawler/requests on each link to see which are still active
# The ones that are not will be freed from the database
#
#
# ==== Things still underway:
# -- Core 1 
# 0. Learn how to delete items from the database
# 1. Add functionality for the user to set a link he/she desires (if available)
# 2. Add function to verify whether the site is forbidden: pornographic, darkweb, etc
# 3. Allow user input
# 4. Improve counter of shortened-link-size
# 4.0. How many 1 char links are there, and of 2 chars, etc
# 4.1. This is important to manage the database 
# 5. Forbid the creation of bad words (swear words)
#
# ===================================



base_link = 'tanshuku.pythonanywhere.com/'
puncts = '._-~'


# ---- Helper functions
def is_link_reachable(link: str) -> list:
    try:
        request = requests.get(link)
        if request.status_code == 200: # Success. In the return message, show the created link
            return [True, ""]
        else: 
            return [False, f"{link} is unreachable."]
    except requests.exceptions.RequestException as error:
        return [False, f"'{link}' is either unreachable or invalid."]


def random_link_generator(links: list) -> str:
    # Checks how many unique URLs there are in the database already to see if more characters 
    # for the URL generation are necessary

    l = len(links)
    n = 1
    total_valid_characters = string.ascii_letters + string.digits + puncts

    # 1 character -> 52 (alfa) + 10 (num) + 4 (punctuations) = 66 possibilities
    # 2 characters -> 66*66 = 66**2 possibilities, because they can be repeated 

    while (len(total_valid_characters)**n < l): 
        n+=1

    random_link = ''.join(random.choice(total_valid_characters) for _ in range(n))
    # print("Random Link: ", random_link)
    return random_link






# ---- Views
def linkshortener(request):
    # Create a page that provides a form that receives a link to be shortened
    # The backend processes the link and the page returns a shortened link
    if request.method == 'POST':
        form = LinkForm(request.POST)        
        check = is_link_reachable(form.data['original_link'])

        if check[0] is True:
            links = [ link.original_link for link in Link.objects.all() ]
            
            # Verify that the original link is unique
            if form.data['original_link'] in links:
                # Link is already stored in the system
                pk = Link.objects.get(original_link=form.data['original_link']).pk
                shortened_link = ShortLink.objects.get(pk=pk).shortened_link
                
            elif form.is_valid():
                # Create ShortLink object and assign to it the created shortened link
                shortlink = ShortLink(shortened_link=random_link_generator(links))
                # print(f"\n\nOriginal Link: {form.data['original_link']}\n")
                # print(f"Shortened Link: {shortlink.shortened_link}\n\n")
                shortened_link = shortlink.shortened_link
                form.save()
                shortlink.save()

            messages.success(request, f"{base_link + shortened_link}")

        else:
            # Couldn't create the shortened link
            messages.error(request, check[1])
            
    else:
        form = LinkForm()
    
    return render(request, 'shortener/form.html', context={'form': form}) 



def redirecter(request, shortened_link):
    # Function that redirects users to their destination
    if request.method == 'GET':
        links = [ link.shortened_link for link in ShortLink.objects.all() ]
        if shortened_link in links:
            pk = ShortLink.objects.get(shortened_link=shortened_link).pk
            original_link = Link.objects.get(pk=pk).original_link
            return redirect(original_link)
        else:
            # print("\n\nUnfortunately, the link is not registered in our databases\n\n")
            shortened_link = base_link + shortened_link
            return render(request, "shortener/not-found.html", {'shortened_link': shortened_link})