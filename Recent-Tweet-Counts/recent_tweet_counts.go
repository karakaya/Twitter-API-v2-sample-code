package Recent_Tweet_Counts

// Search for Tweets within the past
// https://developer.twitter.com/en/docs/twitter-api/tweets/search/quick-start/recent-search

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

type RecentTweets struct {
	Data []Data `json:"data"`
	Meta Meta   `json:"meta"`
}
type Data struct {
	End        time.Time `json:"end"`
	Start      time.Time `json:"start"`
	TweetCount int       `json:"tweet_count"`
}
type Meta struct {
	TotalTweetCount int `json:"total_tweet_count"`
}

func RecentTweetCount() {
	if os.Getenv("BEARER_TOKEN") == "" {
		log.Fatalln("set a bearer token")
	}

	const url = "https://api.twitter.com/2/tweets/counts/recent"

	// Sets the bearer token from your environment variables
	// To set environment variables on macOS or Linux, run the export command below from the terminal:
	// export BEARER_TOKEN='YOUR-TOKEN'
	bearerToken := os.Getenv("BEARER_TOKEN")
	client := http.Client{}

	request, errCreateReq := http.NewRequest("GET", url, nil)
	if errCreateReq != nil {
		log.Println(errCreateReq)
	}
	// Add Bearer Token to HTTP Header
	request.Header.Set("Authorization", "Bearer "+bearerToken)

	// Add Paramater
	q := request.URL.Query()
	q.Add("query", "from:TwitterDev")
	q.Add("granularity", "day")
	request.URL.RawQuery = q.Encode()

	// Send Request
	response, responseErr := client.Do(request)
	if responseErr != nil {
		log.Println(responseErr)
	}

	defer response.Body.Close()

	var recentTweet RecentTweets
	jsonDecodeErr := json.NewDecoder(response.Body).Decode(&recentTweet)
	if jsonDecodeErr != nil {
		log.Println(jsonDecodeErr)
	}

	fmt.Println(recentTweet)
}