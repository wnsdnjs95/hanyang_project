from bs4 import BeautifulSoup
import requests

def jobkor():
	req = requests.get("http://www.jobkorea.co.kr/recruit/joblist?menucode=duty&dutyCtgr=10016")
	soup = BeautifulSoup(req.text, "html.parser")

	list = []
	jobkor_href = []

	for i in soup.select("#dev-gi-list > div > div.tplList.tplJobList > table > tbody > tr > td.tplTit") :
		list.append(i.find("a", class_="link normalLog").text)
		jobkor_href.append(i.find("a", class_="link normalLog")["href"])

	return list, jobkor_href


def saram():
	req = requests.get("http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&search_done=y&panel_count=y")
	soup = BeautifulSoup(req.text, "html.parser")

	list = []
	saram_href = []

	for i in soup.select("#default_list_wrap > table > tbody > tr > td.notification_info > div.job_tit") :
		list.append(i.find("a", class_="str_tit").text)
		saram_href.append(i.find("a", class_="str_tit")["href"])

	return list, saram_href


def incruit():
	req = requests.get("http://job.incruit.com/jobdb_list/searchjob.asp?ct=1&ty=2&cd=574")
	soup = BeautifulSoup(req.text, "html.parser")

	list = []
	incruit_href = []

	for i in soup.select("#container > div.n_job_list_default > div.n_job_list_table_a.list_full_default > table > tbody > tr > td > div > span.accent"):
		list.append(i.find("a", class_="links").text)
		incruit_href.append(i.find("a", class_="links")["href"])

	return list, incruit_href


def career():

	req = requests.get("http://www.career.co.kr/jobs/list/jc_list.asp?pageCnt=40&tab_gb=1&so1=&so2=&so3=0&sb=&sw_a=&sw_l=&sw_g=&ac=&ac2=&ec=&ec1=&ec2=&sc=&sa=&sachk=&age=&noage=&ck=&st=&wc=&jc=H005&jc2=&wf=&la=&la_1=&la_tx=&ct=&cf=&classlevel=&duty=&sqlgb1=&sqlgb2=&sx=&list=&g_MenuID=010101&isSearch=&kw=&sms_idnum=&sms_comname=&smsPhone1=010&smsPhone2=&smsPhone3=")
	soup = BeautifulSoup(req.text, "html.parser")

	list = []
	career_href = []

	for i in soup.find_all("div", class_="name") :
		list.append(i.find("a").text)
		career_href.append(i.find("a")["href"])

	return list, career_href
