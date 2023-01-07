from django.shortcuts import HttpResponse, render
from .models import RosterDaily, RosterWeekly, CharDaily, CharWeekly, User
from .forms import CharDailyForm
from .default_checklist_items import (
    DEFAULT_ROSTER_DAILIES,
    DEFAULT_ROSTER_WEEKLIES,
    DEFAULT_CHARACTER_DAILIES,
    DEFAULT_CHARACTER_WEEKLIES,
)

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        if request.POST:
            model_name = request.POST['modelName']
            item_name = request.POST['itemName']
            item_id = request.POST['itemID']
            checked = request.POST['checked']

            if model_name == "RosterDaily":
                checklist_item = RosterDaily.objects.filter(name=item_name, user_id=item_id).get()
            elif model_name == "RosterWeekly":
                checklist_item = RosterWeekly.objects.filter(name=item_name, user_id=item_id).get()
            elif model_name == "CharDaily":
                checklist_item = CharDaily.objects.filter(name=item_name, char_id=item_id).get()
            elif model_name == "CharWeekly":
                checklist_item = CharWeekly.objects.filter(name=item_name, char_id=item_id).get()
            else:
                # TODO implement this
                pass

            if checked == 'true':
                checklist_item.completed = True

            else:
                checklist_item.completed = False

            checklist_item.save()
            return HttpResponse('')

        else:
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
        print("------------------RETURNING ANON USER------------------")
        if request.POST:
            model_name = request.POST['modelName']
            item_name = request.POST['itemName']
            item_id = request.POST['itemID']
            checked = request.POST['checked']

            if model_name == "RosterDaily":
                checklist_item = RosterDaily.objects.filter(name=item_name, user_id=item_id).get()
            elif model_name == "RosterWeekly":
                checklist_item = RosterWeekly.objects.filter(name=item_name, user_id=item_id).get()
            elif model_name == "CharDaily":
                checklist_item = CharDaily.objects.filter(name=item_name, char_id=item_id).get()
            elif model_name == "CharWeekly":
                checklist_item = CharWeekly.objects.filter(name=item_name, char_id=item_id).get()
            else:
                # TODO implement this
                pass

            if checked == 'true':
                checklist_item.completed = True

            else:
                checklist_item.completed = False

            checklist_item.save()
            return HttpResponse('')

        else:
            user = User.objects.get(session_key=request.session.session_key)
            roster_dailies = RosterDaily.objects.select_related('user').filter(user_id=user.id)
            roster_weeklies = RosterWeekly.objects.select_related('user').filter(user_id=user.id)
            char_dailies = CharDaily.objects.select_related('char__user').filter(char__user__id=user.id)
            char_weeklies = CharWeekly.objects.select_related('char__user').filter(char__user__id=user.id)
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

        request.session.save()

    # Session key is none. User's first time visiting the site.
    else:
        print("------------------NEW USER------------------")
        request.session.create()
        User.objects.create(
            username=f"Anonymous User - {request.session.session_key}",
            password="default",
            session_key=request.session.session_key
        )

        user = User.objects.get(session_key=request.session.session_key)
        roster_dailies = [RosterDaily(user=user, name=rdaily[0], completed=False, img_name=rdaily[1]) for rdaily in DEFAULT_ROSTER_DAILIES]
        RosterDaily.objects.bulk_create(roster_dailies)
        roster_weeklies = [RosterWeekly(user=user, name=rweekly[0], completed=False, img_name=rweekly[1]) for rweekly in DEFAULT_ROSTER_WEEKLIES]
        RosterWeekly.objects.bulk_create(roster_weeklies)

        roster_dailies = RosterDaily.objects.select_related('user').filter(user_id=user.id)
        roster_weeklies = RosterWeekly.objects.select_related('user').filter(user_id=user.id)
        context = {
            'roster_dailies': roster_dailies,
            'roster_weeklies': roster_weeklies,
        }

    return render(request, 'lost_ark_checklist/index.html', context)

def add_character_view(request):
    if request.POST:
        model_name = request.POST['modelName']
        item_name = request.POST['itemName']
        item_id = request.POST['itemID']
        checked = request.POST['checked']

        if model_name == "RosterDaily":
            checklist_item = RosterDaily.objects.filter(name=item_name, user_id=item_id).get()
        elif model_name == "RosterWeekly":
            checklist_item = RosterWeekly.objects.filter(name=item_name, user_id=item_id).get()
        elif model_name == "CharDaily":
            checklist_item = CharDaily.objects.filter(name=item_name, char_id=item_id).get()
        elif model_name == "CharWeekly":
            checklist_item = CharWeekly.objects.filter(name=item_name, char_id=item_id).get()
        else:
            # TODO implement this
            pass

        if checked == 'true':
            checklist_item.completed = True

        else:
            checklist_item.completed = False

        checklist_item.save()
        return HttpResponse('')

    else:
        scrapper_una_daily1 = CharDaily.objects.get(id=2)
        form = CharDailyForm(instance=scrapper_una_daily1)
        context = {
            'form': form
        }

        return render(request, 'lost_ark_checklist/add_character.html', context)