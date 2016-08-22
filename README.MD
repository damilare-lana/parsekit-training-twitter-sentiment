# Twitter API Stock News Parser

This parser ingests tweets from Twitter about a user selected stock. 

## Parsing Strategy

The Tweepy Python library is leveraged to connect to the Twitter Search API. Retweets are filtered out using the `filter.FilterRecords` step on the `was_retweeted` field. Tweets are output into files on Amazon S3 based on the search query that yielded the tweet from the API. 

## Installation & Usage
First install the required depedencies:

`pip install -r requirements.txt`

Then create a local context json with Twitter and S3 credentials that looks like the following:

```json
{
    "consumer_key": "<Twitter API Consumer Key>",
    "consumer_secret": "<Twiter API Consumer Secret>",
    "access_token": "<Twitter API Access Token>",
    "access_token_secret": "<Twitter API Token Secret>",
	"bucket": "<S3 Bucket Name>",
	"credentials": {
		"aws_access_key_id": "<ID>",
		"aws_secret_access_key": "<KEY>"
	},
}
```

Finally to run the parser, execute:

`parsekit run -c /path/to/context.json --allow-unsafe`

### Custom Steps

#### lib/twitter.py
The Twitter Emitter takes in a twitter search query and yields out tweet records.


#### lib/sentiment.py
The sentiment step appends a sentiment score to each input record based on a field specified in the option `field`.



## Datasource Notes

The data is accessed via the Twitter API. Each subsequent query to the API will yield different results than the last. The API is rate limited to 180 requests every 15 minutes. 



## Contacts

Niger Little-Poole <niger.little-poole@enigma.io>