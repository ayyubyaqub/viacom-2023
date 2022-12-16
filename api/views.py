from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog
from categories.models import Categories
from home.models import SubCategories
from django.template.defaultfilters import slugify

from stories.models import Story


# datas = [
#   {
#     "KEYWORDS": [
#       "Ciena Network",
#       "video production company",
#       "corporate video",
#       "video agency",
#       "video company",
#       "advertising agency",
#       "corporate video production company"
#     ],
#     "META TITLE": "Ciena Network | Success Stories | Viacom India LLP",
#     "META DESCRIPTION": "Learn from the case study of Ciena digital network about how we make brand and business videos.",
#     "title": "Ciena Network"
#   },
#   {
#     "KEYWORDS": [
#       "REFORCE",
#       "video production company",
#       "corporate video",
#       "video agency",
#       "video company",
#       "advertising agency",
#       "corporate video production company"
#     ],
#     "META TITLE": "REFORCE | Success Stories | Viacom India LLP",
#     "META DESCRIPTION": "Explore the case study of Reforce to learn about how we make brand and business videos.",
#     "title": "REFORCE"
#   },
#   {
#     "KEYWORDS": [
#       "HP",
#       "video production company",
#       "corporate video",
#       "video agency",
#       "video company",
#       "advertising agency",
#       "corporate video production company"
#     ],
#     "META TITLE": "HP | Success Stories | Viacom India LLP",
#     "META DESCRIPTION": "Read the case study of printers and products company HP to learn about how we make brand and business videos.",
#     "title": "HP"
#   },
#   {
#     "KEYWORDS": [
#       "Shriram Pistons & Rings",
#       "shri ram piston",
#       "shriram pistons & rings ltd",
#       "video production company",
#       "corporate video",
#       "video agency",
#       "video company",
#       "advertising agency",
#       "corporate video production company"
#     ],
#     "SEARCH": "100 – 1K",
#     "META TITLE": "Shriram Pistons & Rings | Success Stories | Viacom India LLP",
#     "META DESCRIPTION": "Read the case study of industry leader Shiram Pistons and rings to learn about how we make brand and business videos.",
#     "title": "Shriram Pistons & Rings"
#   },
#   {
#     "KEYWORDS": [
#       "BilMed",
#       "video production company",
#       "corporate video",
#       "video agency",
#       "video company",
#       "advertising agency",
#       "corporate video production company"
#     ],
#     "META TITLE": "BilMed | Success Stories | Viacom India LLP",
#     "META DESCRIPTION": "Watch the case study of Bilmed to learn about how we make brand and business videos.",
#     "title": "BilMed"
#   },
#   {
#     "KEYWORDS": [
#       "Stellar Data Recovery Pvt. Ltd",
#       "video production company",
#       "corporate video",
#       "video agency",
#       "video company",
#       "advertising agency",
#       "corporate video production company"
#     ],
#     "META TITLE": "Stellar Data Recovery Pvt. Ltd | Success Stories | Viacom India LLP",
#     "META DESCRIPTION": "Read the case study of Stellar Data Recovery Pvt. Ltd to learn about how we make brand and business videos.",
#     "title": "Stellar Data Recovery Pvt. Ltd"
#   }
# ]
def index(request):

    return HttpResponse("Success")
