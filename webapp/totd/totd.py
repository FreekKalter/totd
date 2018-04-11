import json
from twitter import Twitter, OAuth
from . import app

twitter = Twitter(auth=OAuth(app.config['TOKEN'],
                             app.config['TOKEN_SECRET'],
                             app.config['CONSUMER_KEY'],
                             app.config['CONSUMER_SECRET']),
                  retry=3)


def init():
    app.favs = []
    try:  # try to load saved tweets
        with open('tweets.json', 'r') as fh:
            app.favs = json.load(fh)
        print(len(app.favs), 'tweets loaded from tweets.json')
    except FileNotFoundError:
        # load all tweets, because nothing has been saved yet
        app.favs = get_all_tweets()
        for index, fav in enumerate(app.favs):
            fav['random_change'] = index
        print('no tweets.json found,', len(app.favs), 'tweets loaded from twitter.com')
    else:
        # get new tweets that are not saved yet
        new = update()
        print('got', len(new), 'new tweets from twitter.com')
        app.favs = new + app.favs
    # update all random_changes for this day
    for fav in app.favs:
        fav['random_change'] = fav['random_change'] + 1


def get_all_tweets():
    favs = twitter.favorites.list(count=200)
    nomore = False
    while nomore is not True:
        older = twitter.favorites.list(max_id=favs[-1]['id'] - 1, count=200)
        if len(older) < 1:
            nomore = True
        favs = favs + older
    return favs


def save():
    # save tweets to file
    print('number of tweets stored:', len(app.favs))
    with open('tweets.json', 'w') as fh:
        json.dump(app.favs, fh)


def update():
    all = get_all_tweets()
    ids = [fav['id'] for fav in app.favs]
    new = []
    for fav in all:
        if fav['id'] not in ids:
            new.append(fav)
            print(fav['text'])
    print(len(new), 'new tweets downloaded from twitter.com')
    for fav in new:
        fav['random_change'] = 0
    return new


def build_url(fav):
    return 'https://twitter.com/{}/status/{}'.format(fav['user']['screen_name'], fav['id_str'])
