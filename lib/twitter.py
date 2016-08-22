import datetime
import pytz

import tweepy
import parsekit
from parsekit_tools.formats.util import Emitter


class SearchRecords(Emitter):

    _accepts_iterable = False
    _accepts_raw_data = True

    lang = parsekit.Argument(
        'The language code tweets must conform to',
        required=False,
        type=basestring)

    result_type = parsekit.Argument(
        'recent, mixed, or top',
        required=False,
        type=basestring)

    count = parsekit.Argument(
        'The number of results per request, max 100',
        required=False,
        type=int)

    fields = parsekit.Argument(
        'Which fields to extract from Twitter API response',
        required=True,
        type=list)

    def configure(self, options):
        auth = tweepy.OAuthHandler(
            options.consumer_key, options.consumer_secret)
        auth.set_access_token(options.access_token,
                              options.access_token_secret)
        self.api = tweepy.API(auth)
        self.tz = pytz.timezone('UTC')

    def emit_records(self, stock):
        for result in self.api.search(stock,
                                      lang=self.options.lang,
                                      result_type=self.options.result_type,
                                      count=self.options.count):
            record = []
            for field in self.options.fields:
                if hasattr(result, field):
                    value = getattr(result, field)
                    if isinstance(value, datetime.datetime):
                        value = self.tz.localize(value)
                    elif isinstance(value, bool):
                        value = str(value)
                    elif isinstance(value, basestring):
                        value = unicode(value).encode('ascii', 'ignore')
                        print value
                else:
                    value = None
                record.append(value)
            yield record
