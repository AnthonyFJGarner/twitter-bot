def like_tweets_with_hashtag(api, search_hashtags):
    a=0
    search_query = f"{search_hashtags} -filter:retweets"
    for tweet in tweepy.Cursor(api.search, q=search_query,lang ='en',tweet_mode='extended' ).items(3):
            a += 1
            #logger.info(f"{tweet.user.name} said: {tweet.text}")  
            hashtags = [i['text'].lower() for i in tweet.__dict__['entities']['hashtags']]
            
            try:
                list_hashtags=search_hashtags.replace('#',"").split(' OR ')
                print ('list_hashtags',set(list_hashtags))
                print ('hashtags',set(hashtags))
                if set(hashtags) & set(list_hashtags):
                    if tweet.user.id != api.me().id and not tweet.favorited:
                            tweet.favorite()
                            logger.info(f"Liked tweet by {api.me().name}")
                            logger.info(a)
                            time.sleep(55)
            except tweepy.TweepError:
                logger.error("Error on liking", exc_info=True)
                
search_hashtags = '#stockmarket OR #stock OR #algo OR #crypto'
like_tweets_with_hashtag(api,search_hashtags)
