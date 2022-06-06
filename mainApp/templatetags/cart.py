from django import template
register= template.Library()

@register.filter(name="filesize")
def filesize(request,num):
    size= round (num/(1024*1024),2)
    return size
    
   