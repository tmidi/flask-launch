from flask import render_template, request
import launchlibrary as ll
from app import app
import time
from datetime import datetime


@app.route('/', methods=['GET'])
def index():
    api = ll.Api()
    launches = ll.Launch.fetch(api, next=10)
    main_launch = launches[0].net
    return render_template('index.html', launches=launches,
                           main_launch=main_launch)


@app.route('/launch/<int:id>/<path:launch_name>', methods=['GET'])
def launch(id, launch_name):
    api = ll.Api()
    launch = ll.Launch.fetch(api, id=id)
    main_launch = launch[0].net
    rule_url = request.url
    time_utc = datetime.utcnow()
    social_message = 'Check this space launch: '

    return render_template('profile.html', launch=launch[0],
                           main_launch=main_launch,
                           utc=time_utc,
                           rule_url=rule_url,
                           social_message=social_message
                           )
