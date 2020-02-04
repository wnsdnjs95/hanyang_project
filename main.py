from flask import Flask, render_template

app = Flask(__name__)

import list


@app.route('/')
def home():

	return render_template("home.html")



@app.route('/incruit')
def incruit():
	incruit_list, incruit_incruit_href = list.incruit()

	return render_template("incruit.html", data3=incruit_list, data3_href=incruit_incruit_href)


@app.route('/saram')
def saram():
	saram_list, saram_saram_href = list.saram()
	print(len(saram_list))

	return render_template("saram.html", data2=saram_list, data2_href=saram_saram_href, leng2=len(saram_list))


@app.route('/jobkor')
def jobkor():
	jobkor_list, jobkor_jobkor_href = list.jobkor()
	print(len(jobkor_list))

	return render_template("jobkor.html", data1=jobkor_list, data1_href=jobkor_jobkor_href, leng1=len(jobkor_list))


@app.route('/career')
def career():
	career_list, career_career_href = list.career()
	print(len(career_list))

	return render_template("career.html", data4=career_list, data4_href=career_career_href, leng4=len(career_list))


if __name__ == '__main__':
	app.run()
