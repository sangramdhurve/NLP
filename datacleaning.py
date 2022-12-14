class Preprocessing():
    def __init__(self, filepath):
        self.filepath = filepath
        self.stopwords = set(stopwords.words('english'))
        self.regex_patten = r'[^a-zA-Z]'
        self.regex_patten = re.compile(self.regex_patten)

    def readline(self):
        with open(self.filepath, encoding= "utf-8") as input_file:
            return input_file.readlines()

    def cleandata(self, data):
        #data = nltk.sent_tokenize(data)
        corpus = []
        for text in data:
            text = re.sub(self.regex_patten, ' ', str(data))
            text = text.lower()
            text = text.split()
            text = [wordnet.lemmalize(word) for word in text if not word in self.stopwords]
            text = " ".join(text)
            print("text :", text)

            corpus.append(text)
        return corpus


input_filename = input("Enter the path of csv or txt file")
preprocessor = Preprocessing(input_filename)
data = preprocessor.readline()
clean_data = preprocessor.cleandata(data)
print(clean_data)





        