from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Statistics, SocialaccountSocialaccount, MaViolations, MaPlayers
from django.db import models, connections
from steam.steamid import *
from statisticsDJ import settings
from datetime import datetime


def page_not_found(request, template_name='error404.html'):
    response = render(request, template_name=template_name)
    response.status_code = 404
    return response


def server_error(request, template_name='error500.html'):
    response = render(request, template_name=template_name)
    response.status_code = 500
    return response


class MainPage(TemplateView):
    template_name = "login.html"
    model = User


class JoinServer(TemplateView):
    template_name = "server_join.html"
    model = User


class General(TemplateView):
    template_name = "general.html"
    model = User

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SID = None

    def __get_info(self):
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apikey}&steamids={steamid}"

        request = requests.get(url.format(apikey=settings.STEAM_API, steamid=self.SID))
        data = request.json()
        return data

    def get(self, request, *args, **kwargs):
        if request.user.id:
            context = super().get_context_data(**kwargs)
            soc_app = SocialaccountSocialaccount.objects.get(user_id=request.user.id)
            SID = SteamID(soc_app.uid.split("/")[-1])
            self.SID = SID
            data = self.__get_info()

            try:
                player = MaPlayers.objects.get(sid=SID.as_steam2_zero)
                first_enter = eval(player.status)
            except models.ObjectDoesNotExist:
                return redirect('/serverjoin/')

            violations = MaViolations.objects.filter(sid=SID.as_steam2_zero).count()

            with connections['default'].cursor() as cursor:
                cursor.execute("SELECT all_time_on_server "
                               "FROM player_group_time "
                               "WHERE SID_id = '{}'".format(SID.as_steam2_zero))
                all_time = cursor.fetchone()[0]

            context['extend_data'] = {
                'nick': data["response"]["players"][0]["personaname"],
                'avatar': data["response"]["players"][0]["avatarfull"],
                'violation': violations,
                'all_time': all_time // 3600,
                'first_enter': datetime.utcfromtimestamp(int(first_enter['date']) + 10800).strftime("%d.%m.%Y %H:%M"),
                'sid': SID.as_steam2_zero
            }

            return render(request, self.template_name, context=context)


class PageStatistics(TemplateView):
    template_name = "statistics.html"
    model = User

    def get(self, request, *args, **kwargs):

        if request.user.id:
            train = request.GET.get("train", "")
            train_name = request.GET.get("name", "")
            context = super().get_context_data(**kwargs)
            context['client'] = User.objects.get(id=request.user.id)
            soc_app = SocialaccountSocialaccount.objects.get(user_id=request.user.id)
            SID = SteamID(soc_app.uid.split("/")[-1])

            statistics = Statistics.objects.filter(sid=SID.as_steam2_zero).values()[:20]
            values = list()
            dates = list()
            percent_data = list()
            percent_values = list()
            play_time = 0
            number_of_times = 0
            comment = None

            for value, i in zip(statistics, range(len(statistics) - 2)):
                if value[train] == 0 and statistics[i + 1][train] == 0:
                    percent_values.append(0)
                elif statistics[i + 1][train] == value[train]:
                    percent_values.append(0)
                elif value[train] == 0 or statistics[i + 1][train] == 0:
                    if statistics[i + 1][train] == 0:
                        percent_values.append(-100)
                    else:
                        percent_values.append(100)
                else:
                    one_percent = value[train] / 100
                    odds = statistics[i + 1][train] - value[train]
                    percent_values.append(odds // one_percent)

            for value in statistics:
                play_time += value[train]
                if value[train] > 600:
                    number_of_times += 1
                values.append(value[train])
                dates.append(f"{value['date'].strftime('%d.%m.%Y')}")

            if number_of_times < 3:
                comment = f"вы не особо катаетесь на данном составе, потому что каждый раз катаетесь на нем меньше<br>" \
                          f"10 минут, а возможно вам этого вполне достаточно."
            elif number_of_times >= 3:
                comment = f"этот состав является для вас интересным экспериментом,<br>" \
                          f"потому что количество раз, когда вы катались на нем больше 10 минут было " \
                          f"равно {number_of_times}."
            elif number_of_times >= 10:
                comment = f"этот состав является для вас одним из любимых,<br>" \
                          f"потому что количество раз, когда вы катались на нем больше 10 минут было " \
                          f"равно {number_of_times}."

            context['values'] = values
            context['train_name'] = train_name
            context['dates'] = dates
            context['label'] = f"График по составу {train_name}"
            context['percent_data'] = percent_data
            context['percent_values'] = percent_values
            context['play_time'] = play_time
            context['hours'] = datetime.utcfromtimestamp(play_time).strftime("%Hh %Mm %Ss.") \
                .replace("h", "ч").replace("m", "м").replace("s", "с")
            context['comment'] = comment

            return render(request, self.template_name, context=context)
        else:
            return redirect('/')
