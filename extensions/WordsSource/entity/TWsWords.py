class TWsWords:
    """
    ws_words
    """

    def __init__(self, id_, word, mean):
        self.id = id_
        self.word = word
        self.mean = mean

    def show(self):
        print("id:{}, word:{}, mean:{}".format(self.id, self.word, self.mean))
