from django.shortcuts import HttpResponse, render
from .models import RosterDaily, RosterWeekly, CharDaily, CharWeekly, User
from .forms import CharacterForm, CharDailyForm
from django.template import RequestContext
import json

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

            char_checklist[daily.char.char_name][0].append(daily)

        for weekly in char_weeklies:
            if weekly.char.char_name not in char_checklist:
                char_checklist[weekly.char.char_name] = [[], []]

            char_checklist[weekly.char.char_name][1].append(weekly)

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
    if request.POST:
        checked = request.POST['checked']
        item_name = request.POST['itemName']
        item_id = request.POST['itemID']
        char_daily = CharDaily.objects.filter(name=item_name, char_id=item_id).get()

        if checked == 'true':
            char_daily.completed = True

        else:
            char_daily.completed = False

        char_daily.save()
        return HttpResponse('')

    else:
        scrapper_una_daily1 = CharDaily.objects.get(id=2)
        form = CharDailyForm(instance=scrapper_una_daily1)
        context = {
            'form': form
        }

        return render(request, 'lost_ark_checklist/add_character.html', context)