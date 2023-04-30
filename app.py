from flask import Flask, jsonify, request
import twint

app = Flask(__name__)

@app.route('/getTweets')
def getTweets():
    queries = request.args.getlist("query")
    tweets = fetchTweets(queries)
    tweets_list = [
        {
            'tweet': tweet.tweet,
            'username': tweet.username,
            'timestamp': tweet.datetime,
        }
        for tweet in tweets
    ]
    return jsonify(tweets_list)

def fetchTweets(queries):
    tweets = []

    config = twint.Config()
    config.Search = queries
    config.Limit = 50
    config.Store_object = True
    config.Store_object_tweets_list = tweets
    config.Hide_output = True
    # config.Store_csv = True
    # config.Output = "Output.csv"

    twint.run.Search(config)

    return tweets

if __name__ == "__main__":
    app.run(debug=True)
