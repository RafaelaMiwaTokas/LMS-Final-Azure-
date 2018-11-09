from django.shortcuts import render
from django.http import HttpResponse

# Páginas gerais

def index(request):
	return render(request, "index.html")

def lista_de_cursos(request):
	return render(request, "lista_de_cursos.html")

try:
	def disciplinas(request):
		return render(request, "disciplinas/disciplinas.html")
except:
	def disciplinas(request):
		return render(request, "disciplinas.html")

def noticias(request):
	return render(request, "noticias.html")

# Detalhes de curso

def adm(request):
	return render(request, "detalhes_curso/adm.html")

def ads(request):
	return render(request, "detalhes_curso/ads.html")

def adsead(request):
	return render(request, "detalhes_curso/adsead.html")

def bancodedados(request):
	return render(request, "detalhes_curso/bancodedados.html")

def detalhe_de_curso(request):
	return render(request, "detalhes_curso/detalhe_de_curso.html")

def eng_comput(request):
	return render(request, "detalhes_curso/eng_comput.html")

def gestao_ti(request):
	return render(request, "detalhes_curso/gestao_ti.html")

def jogos_digitais(request):
	return render(request, "detalhes_curso/jogos_digitais.html")

def processos_gerenciais(request):
	return render(request, "detalhes_curso/processos_gerenciais.html")

def producao_multimedia(request):
	return render(request, "detalhes_curso/producao_multimedia.html")

def redes_computadores(request):
	return render(request, "detalhes_curso/redes_computadores.html")

def si(request):
	return render(request, "detalhes_curso/si.html")

# Disciplinas

def disciplinas_adm(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm.html")

def disciplinas_adm_1s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_1s.html")

def disciplinas_adm_2s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_2s.html")

def disciplinas_adm_3s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_3s.html")

def disciplinas_adm_4s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_4s.html")

def disciplinas_adm_5s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_5s.html")

def disciplinas_adm_6s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_6s.html")

def disciplinas_adm_7s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_7s.html")

def disciplinas_adm_8s(request):
	return render(request, "disciplinas/disciplinas_adm/disciplinas_adm_8s.html")

def disciplinas_ads_1s(request):
	return render(request, "disciplinas/disciplinas_ads/disciplinas_ads_1s.html")

def disciplinas_ads_2s(request):
	return render(request, "disciplinas/disciplinas_ads/disciplinas_ads_2s.html")

def disciplinas_ads_3s(request):
	return render(request, "disciplinas/disciplinas_ads/disciplinas_ads_3s.html")

def disciplinas_ads_4s(request):
	return render(request, "disciplinas/disciplinas_ads/disciplinas_ads_4s.html")

def disciplinas_ads(request):
	return render(request, "disciplinas/disciplinas_ads/disciplinas_ads.html")

def disciplinas_ads_ead_1s(request):
	return render(request, "disciplinas/disciplinas_ads_ead/disciplinas_ads_ead_1s.html")

def disciplinas_ads_ead_2s(request):
	return render(request, "disciplinas/disciplinas_ads_ead/disciplinas_ads_ead_2s.html")

def disciplinas_ads_ead_3s(request):
	return render(request, "disciplinas/disciplinas_ads_ead/disciplinas_ads_ead_3s.html")

def disciplinas_ads_ead_4s(request):
	return render(request, "disciplinas/disciplinas_ads_ead/disciplinas_ads_ead_4s.html")

def disciplinas_ads_ead(request):
	return render(request, "disciplinas/disciplinas_ads_ead/disciplinas_ads_ead.html")

def disciplinas_ec(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec.html")

def disciplinas_ec_1s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_1s.html")

def disciplinas_ec_2s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_2s.html")

def disciplinas_ec_3s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_3s.html")

def disciplinas_ec_4s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_4s.html")

def disciplinas_ec_5s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_5s.html")

def disciplinas_ec_6s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_6s.html")

def disciplinas_ec_7s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_7s.html")

def disciplinas_ec_8s(request):
	return render(request, "disciplinas/disciplinas_ec/disciplinas_ec_8s.html")

def disciplinas_gt_1s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_1s.html")

def disciplinas_gt(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt.html")

def disciplinas_gt_1s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_1s.html")

def disciplinas_gt_2s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_2s.html")

def disciplinas_gt_3s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_3s.html")

def disciplinas_gt_4s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_4s.html")

def disciplinas_gt_5s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_5s.html")

def disciplinas_gt_6s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_6s.html")

def disciplinas_gt_7s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_7s.html")

def disciplinas_gt_8s(request):
	return render(request, "disciplinas/disciplinas_gt/disciplinas_gt_8s.html")

def disciplinas_jd(request):
	return render(request, "disciplinas/disciplinas_jd/disciplinas_jd.html")

def disciplinas_jd_2s(request):
	return render(request, "disciplinas/disciplinas_jd/disciplinas_jd_2s.html")

def disciplinas_jd_1s(request):
	return render(request, "disciplinas/disciplinas_jd/disciplinas_jd_1s.html")

def disciplinas_jd_3s(request):
	return render(request, "disciplinas/disciplinas_jd/disciplinas_jd_3s.html")

def disciplinas_jd_4s(request):
	return render(request, "disciplinas/disciplinas_jd/disciplinas_jd_4s.html")

def disciplinas_rc_1s(request):
	return render(request, "disciplinas/disciplinas_rc/disciplinas_rc_1s.html")

def disciplinas_rc_2s(request):
	return render(request, "disciplinas/disciplinas_rc/disciplinas_rc_2s.html")

def disciplinas_rc_3s(request):
	return render(request, "disciplinas/disciplinas_rc/disciplinas_rc_3s.html")

def disciplinas_rc_4s(request):
	return render(request, "disciplinas/disciplinas_rc/disciplinas_rc_4s.html")

def disciplinas_rc(request):
	return render(request, "disciplinas/disciplinas_rc/disciplinas_rc.html")

def disciplinas_si_1s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_1s.html")

def disciplinas_si_2s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_2s.html")

def disciplinas_si_3s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_3s.html")

def disciplinas_si_4s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_4s.html")

def disciplinas_si_5s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_5s.html")

def disciplinas_si_6s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_6s.html")

def disciplinas_si_7s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_7s.html")

def disciplinas_si_8s (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si_8s.html")

def disciplinas_si (request):
	return render(request, "disciplinas/disciplinas_si/disciplinas_si.html")

