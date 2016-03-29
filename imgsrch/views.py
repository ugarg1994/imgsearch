from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from imgsrch.models import ImageDB
import json


from mongoengine import *

def test(request):
	#image = ImageDB.objects().first();
	#print image.img_name
	img_url = []
	#image_data["response"] = ImageDB.objects(Q(keywords='utkarsh') | Q(keywords='home'))
	for img in ImageDB.objects(Q(keywords='utkarsh') | Q(keywords='home')):
		img_url.append(img.image_url)
		print img.image_url
	image_data = {}
	image_data['img_url'] = img_url
	return HttpResponse(json.dumps(image_data), content_type="application/json")
	#img_name = "mridul.jpg"
	#img_url = "bcbdj"
	#keywords = ["mridul","mundhra","data","analytics"]

def insertDoc(request):
	image = ImageDB(img_name="home.jpg",image_url="https://s3-us-west-2.amazonaws.com/cyware/home.jpg",keywords=["house","exterior","home"])
	image.save()
	return HttpResponse("Saved")

def image_list(request):
	image_list = ImageDB.objects
	return render_to_response('imgsrch/image_list.html', {'image_list':image_list}, context_instance=RequestContext(request))

def image_detail(request):
	return HttpResponse("OK")

class Home(generic.ListView):
    model = ImageDB
    template_name = 'imgsrch/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        search_text = request.POST.get('srchtxt', False)

        words = search_text.split()
        img_url = []
        #print words
        image = ImageDB.objects(keywords__in=words)
        if image:
            for img in image:
                img_url.append({"name":img.img_name,"url":img.image_url})
            print img.image_url
            return HttpResponse(json.dumps(img_url), content_type="application/json")
        else:
            return HttpResponse(json.dumps(""), content_type="application/json")

        """
        sessionid = request.session.session_key
        session = Session.objects.get(session_key=sessionid)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        uname = user.username
        a=request.POST
        form = UploadFileForm(request.POST, request.FILES)
        path = os.path.dirname(os.path.abspath(__file__))
        myfiles = os.path.join(path, "document")
        myfiles = os.path.join(myfiles, uname)
        os.chdir(myfiles) 
        total_size = 0
        t = 0
        fsize = 0
        for file in os.listdir("."):
            total_size += os.path.getsize(file)
        total_size1 = total_size/1048576
        t = 1073741824 - total_size
        print request.FILES['file'].size
        if request.FILES['file'].size < t:
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'], uname)
                return HttpResponseRedirect(reverse('minor:uploadsuccess'))
        else:
            return HttpResponseRedirect(reverse('minor:sizeerror'))
            """

