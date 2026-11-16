# Import necesary libraries
import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from nltk.corpus import stopwords
import random

# Download the NLTK data files
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess the dataset and extract features
def extract_features(words):
    return {word: True for word in words}

# Load the moview_reviews dataset from NLTK
documents = [(list(movie_reviews.words(fileid)), category)
                for category in movie_reviews.categories() 
                for fileid in movie_reviews.fileids(category)
            ]

# Shuffle the dataset to ensure random distribution
random.shuffle(documents)

# Prepare the dataset for training and testing
featuresets = [(extract_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[:1600], featuresets[1600:]

# Train the Nive Bayes Classifier
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the classifier on the test set
accuracy = nltk_accuracy(classifier, test_set)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Show the most informative features
classifier.show_most_informative_features(10)

# Test on new input sentences
def analyze_sentiment(text):
    # Tokenize and remove stopwords
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.lower() not in stopwords.words('english')]

    # Predict sentiment
    features = extract_features(words)
    return classifier.classify(features)

# Test the classifier with some custom text inputs
test_scentances = [
    "This movie is absolutely fantastic! The acting, the story, everything was amazing",
    "I hated this movie. It was a waste of time and money.",
    "The plot was a bit dull, but the performances were great.",
    "I have mixed feelings about this film. It was okay, not great but not terrible either."
]


for scentence in test_scentances:
    print(f"Sentence: {scentence}")
    print(f"Predicted sentiment: {analyze_sentiment(scentence)}")
    print()