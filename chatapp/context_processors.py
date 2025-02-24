from .models import *
from django.db.models import Q

def my_custom_context(request):
    q = request.GET.get("q")
    if q is None:
        q = ""
    rooms = Rooms.objects.filter(Q(name__icontains=q) 
                                 | Q(topic__name__icontains=q)
                                 | Q(owner__username__icontains=q)
                                 | Q(description__icontains = q)
                                 )
    room_count = rooms.count()
    topics = Topic.objects.all()
    chats = Chatbot.objects.all()
    name = "ade"
    return {'topics': topics, "room_count":room_count, "chats":chats }
