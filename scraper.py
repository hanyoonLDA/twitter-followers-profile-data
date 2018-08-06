import scraperwiki
import simplejson
import urllib2

myfollowers = []
twitter_handle = 'hanyoon'

base_url = 'https://api.twitter.com/1.1/followers/ids.json?screen_name=' + twitter_handle 
results_json = simplejson.loads(scraperwiki.scrape(base_url))
myfollowers = results_json['ids']
myfollowers_str = map(str, myfollowers) 

scraperwiki.swimport('twitter_bulk_users_lookup').bulklookup(myfollowers_str)
