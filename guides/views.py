from django.shortcuts import render
from guides.models import Guide
from django.template import Template, RequestContext

def guide_description(request, page="0"):
	page = int(page)
	guide_list= []
	first = page * 12
	last = page * 12 + 12
	last_page = ""
	next_page = ""
	if page > 0: 
		last_page = str(int(page) - 1)
	try:
		guide_list = Guide.objects.defer("guide_content")[first:last:-1]
	except Guide.DoesNotExist:
		guide_list = []
	if guide_list != []:
		next_page = str(int(page) + 1)
	try:
		guide_list_1 = guide_list[0::3]
       		guide_list_2 = guide_list[1::3]
        	guide_list_3 = guide_list[2::3]
	except IndexError:
		guide_list_1 = []
		guide_list_2 = []
		guide_list_3 = []
        return render(request, "pick_guide.html", {"last_page":last_page, "next_page":next_page, "guide_list_1":guide_list_1, "guide_list_2":guide_list_2, "guide_list_3":guide_list_3})

def guide_page(request, guide_name):
	user = request.user
	try:
		new_guide_name = str(guide_name)
	except ValueError:
		raise Http404()
	guide = Guide.objects.get(guide_page=new_guide_name)
	content = Template(guide.guide_content)
	c = RequestContext(request, {})
	content = content.render(c)
	if guide.pay == True and user.pay == False:
		return redirect("/upgrade_needed/")
	related_list = Guide.objects.filter(guide_meta=guide.guide_meta)
	return render(request, "page_guide.html", {"guide":guide, "content":content, "related_list":related_list})
