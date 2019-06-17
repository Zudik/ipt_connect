import os
from IPTdev.models import *
from urllib import quote


def list_url():

    url_team = '/IPTdev/teams/';
    url_round = '/IPTdev/rounds/';

    urls_menu = ['/IPTdev/physics_fights',
                 '/IPTdev/poolranking',
                 '/IPTdev/problems',
                 '/IPTdev/participants',
                 '/IPTdev/jurys',]

    urls_other = ['/IPTdev/tournament',
                  '/IPTdev/ranking',]

    urls_external_link = ['https://github.com/IPTnet/ipt_connect',
                          'https://connect.iptnet.info/',]

    teams_name = [team.name for team in Team.objects.all()]
    numbers_participant = [part.pk for part in Participant.objects.all()]
    numbers_round = [rn.pk for rn in Round.objects.all()]
    numbers_physics_fights = [fights for fights in range(1, npf_tot + 1)]
    numbers_problem = [p.pk for p in Problem.objects.all()]
    numbers_jury = [jury.pk for jury in Jury.objects.all()]

    urls_teams = [url_team + quote(i.encode('utf-8')) + '/' for i in teams_name]
    urls_rounds = [url_round + str(i) + '/' for i in numbers_round]
    urls_participants = [urls_menu[3] + '/' + str(i) + '/' for i in numbers_participant]
    urls_physics_f = [urls_menu[0] + '/' + str(i) + '/' for i in numbers_physics_fights]
    urls_problems = [urls_menu[2] + '/' + str(i) + '/' for i in numbers_problem]
    urls_jury = [urls_menu[4] + '/' + str(i) + '/' for i in numbers_jury]

    urls = urls_external_link +  urls_menu + urls_other  + urls_rounds + urls_teams + urls_participants + urls_problems + urls_jury  + urls_physics_f

    path_for_urls = 'C:\Users\Den\PycharmProjects\git\ipt\ipt_connect\ipt_connect\IPTdev\url'

    with open(os.path.join(path_for_urls, 'urls.txt'), "wb") as file:
        for u in urls:
            file.write(u + '\n')

    return urls