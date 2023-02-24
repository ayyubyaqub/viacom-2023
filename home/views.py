import requests
from django.db.models import Q
from django.http import  HttpResponseNotAllowed, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from categories.models import Categories, SuperCategory
from django.core.mail import send_mail
from django.core.cache import cache
from django.core.paginator import Paginator
# models imported here
from django.contrib import messages
from django.core.mail import EmailMessage
from clients.models import Clients
from home.models import Academic_page, Academics, Contact_Us_Page, Home_work_youtube_video, Homecarousel, Media_Page,Shorts,Shorts_Page,Marketing_Page ,Marketing, Media,MetaTags, SubCategories, Subscription_Page, TermsAndCondition, Two_Four_Seven, Two_Four_Seven_Integrated, Two_Four_Seven_Page, Video_Marketing, Video_Marketing_Page, homePageHeading,career , career_table_header ,  Aboutus, Interest_Person, Home_page_video, work, aboutusteam, work_youtube_video, create_video, Image_client_logo_and_Vi, MarketPlaceVideo, contact_us_location, creators,Customer
# Create your views here.
from time import time

# MailID = 'contact@viacomindia.com'
# MailID = 'viacomindiavideo@gmail.com'
# MailID = 'viacomindia99@gmail.com'
MailID = 'contact@viacomindia.com'


def verifyHcaptchaToken(request):
    if request.method == "POST":
        SECRET_KEY = '0x27755d798822aB5939DAD45Dd32F4BB5bAe4462E'
        VERIFY_URL = 'https://hcaptcha.com/siteverify'

        token = request.POST.get('h-captcha-response')

        data = {'secret': SECRET_KEY, 'response': token}

        response = requests.post(url=VERIFY_URL, data=data)
        if response.json()['success']:
            return HttpResponse('SUCCESS')
        else:
            return HttpResponse('FAILED')
    else:
        return HttpResponseNotAllowed


def index(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    clients = Clients.objects.all()[:10]
    super_categories = SuperCategory.objects.order_by('serial_number')
    homecarousel = Homecarousel.objects.all()
    work_video = Home_work_youtube_video.objects.all().first()
    homepageheading = homePageHeading.objects.all()
    homevideo = Home_page_video.objects.first()

    params = {
        'meta_title': 'Viacom India',
        'meta_description': "We create videos for brands, businesses, and agencies anywhere in India. See our video marketplace & Start creating videos for creative representation of your brand.",
        'meta_keywords':'video production company, corporate video, video agency, video company, advertising agency, corporate video production company',
        'clients': clients,
        'super_categories': super_categories,
        'carousels': homecarousel,
        'homepageheading': homepageheading,
        'homevideo': homevideo,
        'work_video': work_video,
        'imageclientand_vi': imageclientand_vi,
    }
    return render(request, 'components/home.html', params)
#     return HttpResponse('''<!doctype html>
# <title>Site Maintenance</title>
# <style>
#   body { text-align: center; padding: 150px; }
#   h1 { font-size: 50px; }
#   body { font: 20px Helvetica, sans-serif; color: #333; }
#   article { display: block; text-align: left; width: 650px; margin: 0 auto; }
#   a { color: #dc8100; text-decoration: none; }
#   a:hover { color: #333; text-decoration: none; }
# </style>

# <article>
#     <h1>We&rsquo;ll be back soon!</h1>
#     <div>
#         <p>Sorry for the inconvenience but we&rsquo;re performing some maintenance at the moment. If you need to you can always <a href="contactus">contact us</a>, otherwise we&rsquo;ll be back online shortly!</p>
#         <p>&mdash; The Team</p>
#     </div>
# </article>''')


def category(request, slug):
    supercategory = SuperCategory.objects.filter(slug=slug).first()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    if supercategory:
        supercategory = SuperCategory.objects.get(slug=slug)
        params = {
            'meta_title': supercategory.super_category_name,
            'meta_description': supercategory.description,
            'supercategory': supercategory,
            'imageclientand_vi': imageclientand_vi
        }
        
        return render(request, 'components/allcategories.html', params)
    category = Categories.objects.filter(slug=slug).first()
    if category:

        supercategory = SuperCategory.objects.filter(sp__slug=slug).first()
        params = {
            # 'metas':metas,
            'meta_title': category.meta_title,
            'meta_description': category.meta_description,
            'meta_keywords': category.meta_keywords,
            'category': category,
            'supercategory': supercategory,
            'imageclientand_vi': imageclientand_vi,
            'og_image':category.image.url
        }
        return render(request, 'components/homecategory.html', params)
    subcategory = SubCategories.objects.filter(slug=slug).first()
    if subcategory:
        category = Categories.objects.filter(categories__slug=slug).first()
        supercategory = SuperCategory.objects.filter(
            sp__categories__slug=slug).first()
        params = {
            # 'metas':metas,
            # 'meta_title': subcategory.subcategory,
            # 'meta_description': category.brief,
            'meta_title': subcategory.meta_title,
            'meta_description': subcategory.meta_description,
            'meta_keywords': subcategory.meta_keywords,
            'subcategory': subcategory,
            'category': category,
            'imageclientand_vi': imageclientand_vi,
            'supercategory': supercategory,
            'og_image':subcategory.image.url
        }
        return render(request, 'components/subcategory.html', params)
    return redirect('/')


def categories(request):
    if request.GET.get('query') == 'get_searched_query':
        search = request.GET.get('search')
        categories = list(SubCategories.objects.filter(
            Q(category__category__icontains=search) | Q(subcategory__icontains=search)).values())

        return JsonResponse(categories, safe=False)
    s = time()
    supercategories = SuperCategory.objects.exclude(
        slug='explore-our-most-popular-trending-video-content-types').defer('description').order_by('serial_number')
    e = time()
    print(e-s)
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    # print(supercategories[0].sp )
    params = {
        'meta_title': 'All categories',
        'meta_description': 'India’s Preferred Content Production Services',
        'supercategories': supercategories,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/categories.html', params)


def create_videos(request):
    print('i am here,158')
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name')
        website = request.POST.get('website')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        video_categories = request.POST.get('video_categories')
        other_project_details = request.POST.get('other_project_details')
        project_description = request.POST.get('project_description')
        project_country = request.POST.get('project_country')
        project_city_state = request.POST.get('project_city_state')
        project_pincode = request.POST.get('project_pincode')
        delivery_speed = request.POST.get('delivery_speed')
        project_budget = request.POST.get('project_budget')
        reference_link = request.POST.get('reference_link[]')
        Customer.objects.create(brand_name=brand_name, website=website, first_name=first_name, last_name=last_name, email=email, phone=phone, video_categories=video_categories, other_project_details=other_project_details,
                                project_description=project_description, project_country=project_country, project_city_state=project_city_state, project_pincode=project_pincode, delivery_speed=delivery_speed, project_budget=project_budget, reference_link=reference_link)
        send_mail(
            "A customer booked our service",
            "Brand Name : " +  str(brand_name) + "\nWebsite : " + str(website) + "\nFirst Name : " + str(first_name) + "\nLast Name : "
            + str(last_name) + "\nEmail : " + str(email) + "\nPhone number : " + str(phone) + "\nVideo Category : " + str(video_categories) + "\nOther Project Details : " 

            +  str(other_project_details) + "\nProject Description : " + str(project_description) + "\nProject Country : " + str(project_country) + "\nCity State : " + str(project_city_state) +
            "\nPincode : " + str(project_pincode) + "\nDelivery Speed : " + str(delivery_speed) +
            "\nBudget : " + str(project_budget) + "\nReference Link : " + str(reference_link),

            MailID,
            ['viacomindiavideo@gmail.com', 'contact@viacomindia.com','ayyubkhan4341@gmail.com'],

            fail_silently=False,
        )
        messages.success(request, 'Message has been sent successfully!')
    obj = create_video.objects.all().first()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        "meta_keywords" : obj.meta_keywords,
        "meta_description" : obj.meta_description,
        "meta_title" : obj.meta_title,
        'create_video': obj,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/createvideo.html', params)


def about(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    aboutus = Aboutus.objects.all().first()
    Aboutusteam = aboutusteam.objects.order_by('serial_number')
    params = {
        "meta_keywords" : aboutus.meta_keywords,
        "meta_description" : aboutus.meta_description,
        "meta_title" : aboutus.meta_title,
        'aboutus': aboutus,
        'Aboutusteam': Aboutusteam,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/about.html', params)


def two_four_seven(request):
    cards = Two_Four_Seven.objects.all()
    integrated = Two_Four_Seven_Integrated.objects.all()
    page = Two_Four_Seven_Page.objects.all().first()
    
    params = {
        'meta_title': page.meta_title,
        'meta_description': page.meta_description,
        'meta_keywords': page.meta_keywords,
        'cards' : cards,
        "integrated" : integrated,
        "page" : page, 
    }
    return render(request, 'components/twoFourSeven.html', params)


def experimental_marketing_view(request):
    
    return render(request, 'components/experimental-marketing.html', {})


def academics_view(request):
    academics = Academics.objects.all()
    academic_page = Academic_page.objects.first()
    
    params = {
        'meta_title': academic_page.meta_title,
        'meta_description': academic_page.meta_description,
        'meta_keywords': academic_page.meta_keywords,
        "academics" : academics, 
        "academic_page" : academic_page 
    }
    return render(request, 'components/academic.html', params)

def career_view(request):
    career_obj = career.objects.all().first()
    table = career_table_header.objects.order_by("serial_number")
    params = {
        'meta_title': career_obj.meta_title,
        'meta_description': career_obj.meta_description,
        'meta_keywords': career_obj.meta_keywords,
        'table' : table,
        'career': career_obj
    }
    return render(request, 'components/career.html', params)


def media_view(request):
    media_obj = Media.objects.all()
    media_page = Media_Page.objects.all().first()
    params = {
        'meta_title': media_page.meta_title,
        'meta_description': media_page.meta_description,
        'meta_keywords': media_page.meta_keywords,
        'media': media_obj,
        'media_page': media_page,
        'create_video_footer' : False
    }
    return render(request, 'components/media.html', params)


def video_marketing_view(request):
    video_marketing_obj = Video_Marketing.objects.all()
    video_marketing_page = Video_Marketing_Page.objects.all().first()
    params = {
        'meta_title': video_marketing_page.meta_title,
        'meta_description': video_marketing_page.meta_description,
        'meta_keywords': video_marketing_page.meta_keywords,
        'video_marketing_obj': video_marketing_obj,
        'video_marketing_page': video_marketing_page,
    }
    
    return render(request, 'components/video_marketing.html', params)

def marketing_view(request):
    marketing_obj = Marketing.objects.all()
    marketing_page = Marketing_Page.objects.all().first()
    params = {
        'meta_title': marketing_page.meta_title,
        'meta_description': marketing_page.meta_description,
        'meta_keywords': marketing_page.meta_keywords,
        'marketing': marketing_obj,
        'marketing_page': marketing_page,
        'create_video_footer' : False
    }
    return render(request, 'components/marketing.html', params)

def shorts_view(request , num=1):
    # print(num  +  " uebfbkhbvj")
    shorts_obj = Shorts.objects.all()
    shorts_page = Shorts_Page.objects.all().first()
    pagination = Paginator(shorts_obj, 9)
    page_obj = pagination.page(num)

    params = {
        'meta_title': shorts_page.meta_title,
        'meta_description': shorts_page.meta_description,
        'meta_keywords': shorts_page.meta_keywords,
        'shorts_page': shorts_page,
        'shorts_obj' : page_obj,
        'pagination' : pagination,
        'num' : num,
        'create_video_footer' : False
    }
    return render(request, 'components/shorts.html', params)


from django.views.decorators.csrf import csrf_exempt

import json
@csrf_exempt
def contactus(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        requirement = request.POST.get('website')
        message = request.POST.get('description')
        Interest_Person.objects.create(fullname=fullname, email=email, mobile=mobile, requirement=requirement, message=message)
        email = EmailMessage(
            "A customer contacted us",
            'Name :'+str(fullname) + '\nEmail :'+str(email)+'\nMobile :' + str(mobile) +
            '\nRequirement :' + str(requirement)+'\nMessage :' + str(message),
            MailID,
            ['viacomindiavideo@gmail.com', 'contact@viacomindia.com','ayyubkhan4341@gmail.com']
            
        )
        email.send(fail_silently=False)
        
        messages.success(request, 'Message has been sent successfully!')
    Contact_us_location = contact_us_location.objects.all()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    contact_us_page = Contact_Us_Page.objects.all().first()
    params = {
        # "meta_keywords" : contact_us_page.meta_keywords,
        # "meta_description" : contact_us_page.meta_description,
        # "meta_title" : contact_us_page.meta_title,
        'contact_us_location': Contact_us_location,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/contactus.html', params)
 


def works(request):
    our_woks = work.objects.all().first()
    videolinks = work_youtube_video.objects.order_by('serial_number')
    carousel = Homecarousel.objects.all()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        "meta_keywords" : our_woks.meta_keywords,
        "meta_description" : our_woks.meta_description,
        "meta_title" : our_woks.meta_title,
        'carousels': carousel,
        'our_woks': our_woks,
        'videolinks': videolinks,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/work.html', params)


def marketplace(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    marketplace = MarketPlaceVideo.objects.all().first()
    supercategory = SuperCategory.objects.filter(
        super_category_name='Curated Video Marketplace').first()
    params = {
        'meta_title': supercategory.super_category_name,
        'meta_description': supercategory.description,
        'supercategory': supercategory,
        'marketplace': marketplace, 'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/marketplace.html', params)


def industry(request):
    supercategory = SuperCategory.objects.filter(
        Q(slug__icontains='industry')).all()

    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()

    params = {
        'meta_title': "Industry",
        'meta_description': "Industry presented by viacom india",
        'supercategories': supercategory,
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/industry.html', params)



def subscription(request):
    supercategory = SuperCategory.objects.filter(slug='subscription').first()
    subscription_page = Subscription_Page.objects.all().first()
    param = {
        "meta_keywords" : subscription_page.meta_keywords,
        "meta_description" : subscription_page.meta_description,
        "meta_title" : subscription_page.meta_title,
        'supercategory': supercategory
    }
    return render(request, 'components/subscription.html', param)





def allTermsAndCondition(request):
    terms_and_condition = TermsAndCondition.objects.all()
    params = {
        'meta_title': "Terms and conditions",
        'meta_description': "Viacom india terms and conditions",
        "terms_and_condition": terms_and_condition
    }
    return render(request, 'components/all-terms-and-conditions.html', params)


def termsAndCondition(request, slug):
    terms_and_condition = TermsAndCondition.objects.get(Q(slug=slug))
    params = {
        'meta_title': terms_and_condition.terms_and_condition_name,
        'meta_description': "Viacom india terms and conditions",
        "terms_and_condition": terms_and_condition
    }
    return render(request, "components/terms-and-condition.html", params)


def pricing(request):
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        'meta_title': "Pricing",
        'meta_description': "Viacom india terms and conditions",
        'imageclientand_vi': imageclientand_vi
    }
    return render(request, 'components/pricing.html', params)


def creator(request):
    creator = creators.objects.all().first()
    imageclientand_vi = Image_client_logo_and_Vi.objects.all().first()
    params = {
        "meta_keywords" : creator.meta_keywords,
        "meta_description" : creator.meta_description,
        "meta_title" : creator.meta_title,
        'creator': creator,
        'imageclientand_vi': imageclientand_vi,
    }
    return render(request, 'components/creators.html', params)
