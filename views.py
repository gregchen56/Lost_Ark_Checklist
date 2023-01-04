from django.shortcuts import render
from .models import RosterDaily, RosterWeekly, CharDaily, CharWeekly, User
from .forms import CharacterForm

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        roster_dailies = RosterDaily.objects.select_related('user').filter(user_id=request.user.id)
        roster_weeklies = RosterWeekly.objects.select_related('user').filter(user_id=request.user.id)
        char_dailies = CharDaily.objects.select_related('char__user').filter(char__user__id=request.user.id)
        char_weeklies = CharWeekly.objects.select_related('char__user').filter(char__user__id=request.user.id)
        char_checklist = {}

        for daily in char_dailies:
            if daily.char.char_name not in char_checklist:
                char_checklist[daily.char.char_name] = [[], []]

            char_checklist[daily.char.char_name][0].append(daily.name)

        for weekly in char_weeklies:
            if weekly.char.char_name not in char_checklist:
                char_checklist[weekly.char.char_name] = [[], []]

            char_checklist[weekly.char.char_name][1].append(weekly.name)

        context = {
            'roster_dailies': roster_dailies,
            'roster_weeklies': roster_weeklies,
            'char_checklist': char_checklist,
        }

    # Anonymous returning user
    elif request.session.session_key:
        char_dailies = CharDaily.objects.select_related('char__user').filter(char__user__session_key=request.session.session_key)
        context = {
            'char_dailies': char_dailies
        }
        request.session.save()

    # Session key is none. User's first time visiting the site.
    else:
        request.session.create()
        User.objects.create(
            username=f"Anonymous User - {request.session.session_key}",
            password="default",
            session_key=request.session.session_key
        )
        context = {}

    print("----------Request details below----------")

    return render(request, 'lost_ark_checklist/index.html', context)

def add_character_view(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    print("----------Request details below----------")
    cookies = request.COOKIES
    print(cookies)
    print(request.user)

    return render(request, 'lost_ark_checklist/add_character.html', context)