import datetime
import time

weekday = datetime.datetime.today().weekday()
hour = datetime.datetime.now().time().hour
minute = datetime.datetime.now().time().minute

mack_url = 'https://graduacao.mackenzie.br/course'
mack_launch_url = 'https://graduacao.mackenzie.br/mod/lti/launch.php?id='

######################## MACK URL ########################
analise_viabilidade_financeira = mack_url + '/view.php?id=108&section=0#tabs-tree-start'
comportamento_organizacional = mack_url + '/view.php?id=1207'
inovacao = mack_url + '/view.php?id=3092'
gestao_de_operacoes = mack_url + '/view.php?id=3116'
gestao_financeira = mack_url + '/view.php?id=3166'
logistica_empresarial = mack_url + '/view.php?id=3750'
politicas_e_praticas = mack_url + '/view.php?id=4527'
si = mack_url + '/view.php?id=5271'
######################## ELO URL ########################
gestao_financeira_elo = mack_launch_url + '69330'
logistica_empresarial_elo =  mack_launch_url + "141814"
gestao_de_operacoes_elo = mack_launch_url + "292517"
si_elo = mack_launch_url + "290130"
analise_viabilidade_financeira_elo = mack_launch_url + "134975"
comportamento_organizacional_elo = mack_launch_url + "148587"
politicas_e_praticas_elo = mack_launch_url + '140206'
inovacao_elo = 'https://shorturl.at/mwCEK'

gf_dict = {
    "url": gestao_financeira,
    "elo": gestao_financeira_elo
}
le_dict = {
    "url": logistica_empresarial,
    "elo": logistica_empresarial_elo
}
go_dict = {
    "url":gestao_de_operacoes,
    "elo": gestao_de_operacoes_elo
}
avf_dict = {
    "url": analise_viabilidade_financeira,
    "elo": analise_viabilidade_financeira_elo
}
co_dict = {
    "url": comportamento_organizacional,
    "elo": comportamento_organizacional_elo
}
si_dict = {
    "url": si,
    "elo": si_elo
}
# Noturno
inov_dict = {
    "url": inovacao,
    "elo": inovacao_elo
}
pol_prat_dict = {
    "url": politicas_e_praticas,
    "elo": politicas_e_praticas_elo
}

classes = [
    [gf_dict, le_dict, inov_dict],
    [go_dict, avf_dict, pol_prat_dict],
    [go_dict, {"url": '', "elo": ""}],
    [co_dict, le_dict],
    [si_dict, co_dict],
]

condition = (hour == 9 and minute > 10) or hour > 9



def getClassURL(URLType = "url"):
    if weekday == 6:
        return classes[0][0][URLType]
    if hour > 17 and weekday <= 1:
        return classes[weekday][2][URLType]
    if condition:
        return classes[weekday][1][URLType]
    else:
        return classes[weekday][0][URLType]

