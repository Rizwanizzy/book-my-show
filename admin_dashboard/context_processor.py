from home.models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from room.models import *


def admin_side_messages(request):
    context = {}
    if request.user.is_superuser:
        chat_messages = (
            ChatMessage.objects
            .filter(recipient=request.user)
            .select_related('sender')
            .distinct('sender')
        )
        try:
            chat_messages_list = list(chat_messages)  # Convert queryset to list
            for message in chat_messages_list:
                print('username:', message.sender.username)
            context = {'chat_messages': chat_messages_list}
        except ObjectDoesNotExist:
            pass
    return context
