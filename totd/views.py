from flask import render_template, Markup
import random
from . import app, totd


def pick():
    # calculate total balls in the bowl
    total = 0
    for fav in app.favs:
        total = total + fav['random_change']
    pick = random.randint(0, total)
    for fav in app.favs:
        pick = pick - fav['random_change']
        if pick <= 0:
            print(fav['text'])
            fav['random_change'] = 0
            return fav['id']
            # return totd.twitter.statuses.oembed(
            #     url=totd.build_url(fav),
            #     omit_script=False,
            #     align='center',
            #     maxwidth=550)['html']


def reset_changes(fav_list):
    for fav in fav_list:
        fav['random_change'] = 0


@app.route("/")
def root():
    return(render_template('index.html', tweet=Markup(pick())))


@app.route("/newtweet")
def newtweet():
    return Markup(pick())


@app.route('/dump')
def dump():
    if app.config['DEBUG']:
        return(render_template('dump.html', tweets=app.favs))
    else:
        return
