from nltk.corpus import twitter_samples,stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

#step1:Gather data
#step2:Clean,lemmatize and remove stop words from data
#step3:Transform data
#step4:Create data set
#step5:Train the model
#step6:Test Accuracy
#step7:Save the model




def clean_data(token):
    return [item for item in token if not item.startswith('@') and not item.startswith('http')]


def to_lower(token):
    return [item.lower() for item in token]


def lemmatize(token):
    lemmatizer=WordNetLemmatizer()


    result=[]
    for item,tag in pos_tag(token):
        if tag[0].lower() in "nva":   #n= noun v=verb a=adjective
            result.append(lemmatizer.lemmatize(item,tag[0].lower()))
        else:
            result.append((lemmatizer.lemmatize(item)))
    return result


def remove_stop_words(token,stop_words):
    return [item for item in token if item not in stop_words]



def main():
    #Step 1:Gather data
    positive_tweets=twitter_samples.tokenized('positive_tweets.json')
    negative_tweets=twitter_samples.tokenized('negative_tweets.json')
    print(positive_tweets[0])
    print(negative_tweets[0])

    #Step 2:Clean,lemmatize and remove stop words from data
    stop_words=stopwords.words('english')
    positive_tweets=[remove_stop_words(lemmatize(clean_data(to_lower(item))),stop_words) for item in positive_tweets]
    negative_tweets=[remove_stop_words(lemmatize(clean_data(to_lower(item))),stop_words) for item in negative_tweets]
    print(positive_tweets[0])
    print(negative_tweets[0])



if __name__=="__main__":
    main()

