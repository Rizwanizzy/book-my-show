from home.models import UserProfile
from django.contrib.auth.models import User


def user_profile_details(request):
    user = User.objects.get(username=request.user)
    user_profile = UserProfile.objects.get(user=user)
    context={'user_profile':user_profile}
    return context