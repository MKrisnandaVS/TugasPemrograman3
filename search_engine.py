from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SearchEngine:
    def __init__(self, dataset_path):
        with open(dataset_path, 'r') as file:
            self.documents = file.readlines()
        self.vectorizer = TfidfVectorizer()
        self.document_vectors = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_n=5):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.document_vectors).flatten()
        ranked_indices = similarities.argsort()[::-1][:top_n]
        return [(self.documents[i].strip(), similarities[i]) for i in ranked_indices]