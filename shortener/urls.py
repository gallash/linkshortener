from django.urls import path, re_path
from . import views
import re


# This is how it will work
# <domain>/ -> Forms page that executes the shortener() function
# <domain>/Huahua -> Sends link directly to redirecter()

# The regex metacharacters
# ^ (caret) matches at the beginning of a string
# $ (dollar sign) binds re to end of string
# (?P<name>\<pattern>) passes the pattern as a Parameter of name <name> to the function

# regular expression for at least one alphanum + symbols: (?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W) 
urlpatterns = [
    re_path(r"^(?P<shortened_link>\w+)$", views.redirecter),
    path("", views.linkshortener, name="shortener-page")
]

