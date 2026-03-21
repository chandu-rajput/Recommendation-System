import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# Load data once
movies = pickle.load(open('models/movie_list.pkl', 'rb'))
tfidf_matrix = pickle.load(open('models/similarity_vectors.pkl', 'rb'))
indices = pickle.load(open('models/indices_map.pkl', 'rb'))

# Weighted rating
C = movies['vote_average'].mean()
m = movies['vote_count'].quantile(0.60)

def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m)) * R + (m / (m + v)) * C


def get_recommendations(title, top_n=5):
    key = title.lower().strip()

    if key not in indices:
        matches = [k for k in indices.keys() if key in k]
        if not matches:
            return None, None
        key = matches[0]

    idx = indices[key]
    matched_title = movies.iloc[idx]['title']

    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix)[0]
    sim_indices = sim_scores.argsort()[::-1][1:101]

    rec = movies.iloc[sim_indices].copy()
    rec['sim_score'] = sim_scores[sim_indices]
    rec = rec.drop_duplicates(subset='title')

    rec['weighted_rating'] = rec.apply(weighted_rating, axis=1)

    scaler = MinMaxScaler()
    rec[['norm_sim', 'norm_rating']] = scaler.fit_transform(
        rec[['sim_score', 'weighted_rating']]
    )

    rec['hybrid_score'] = 0.6 * rec['norm_sim'] + 0.4 * rec['norm_rating']

    return rec.sort_values('hybrid_score', ascending=False).head(top_n), matched_title