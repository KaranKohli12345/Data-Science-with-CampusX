import nlpcloud

class API:
    def __init__(self):
        pass

    def Sentiment_Analysis(self, text):
        client = nlpcloud.Client("distilbert-base-uncased-emotion", "7e6fe564c0baa38b214a9eb574c3242d68bbe982", gpu=False)
        response = client.sentiment(text)

        return response


