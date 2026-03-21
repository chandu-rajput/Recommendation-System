# 🎬 Movie Recommender System

A hybrid movie recommendation engine built with Python and Streamlit. It balances content similarity with a weighted rating system to ensure recommendations are both relevant and high-quality.

---

## 🚀 Features

* 🔍 Content-based recommendations using TF-IDF
* ⭐ IMDB-style weighted rating system
* 🎯 Hybrid recommendation (similarity + weighted rating system)
* 🌐 Interactive UI with Streamlit
* ⚡ Fast similarity search using cosine similarity

---

---

## 🧠 The Hybrid Algorithm
The system calculates a final score by combining two metrics:
1. Content-Based Filtering (60%): Uses TF-IDF Vectorization on movie overviews and genres, then calculates the Cosine Similarity between vectors.
2. Weighted Rating (40%): To avoid recommending obscure movies with a single 10-star rating, we use the IMDB Weighted Rating formula:
      $$W = \frac{v}{v+m} \cdot R + \frac{m}{v+m} \cdot C$$$
   v$: Number of votes for the movie
   $m$: Minimum votes required to be listed
   $R$: Average rating of the movie
   $C$: Mean vote across the whole report
---

## 🧠 How It Works

This system combines two approaches:

* **60% Content-Based Filtering**

  * Uses TF-IDF vectorization on movie metadata
  * Computes cosine similarity between movies

* **40% Weighted Rating (IMDB Formula)**

  * Uses a Bayesian average to rank popular movies
  * Balances vote count and vote average

---

## 🛠️ Tech Stack

* Language: Python
* Data: Pandas, NumPy, Scikit-learn
* UI: Streamlit
* Pickle (for model storage)
* Environment: uv
* Google Colab (for model building)

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── app.py
├── recommender.py
├── pyproject.toml
├── README.md
├── .gitignore
│
├── models/
│   ├── movie_list.pkl
│   ├── similarity_vectors.pkl
│   ├── indices_map.pkl
│
├── notebooks/
│   └── movie_recommendation.ipynb
```

---

## ⚙️ Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install dependencies (using uv)

```bash
uv sync
```

### 3. Run the app

```bash
uv run streamlit run app.py
```

---

## 🖼️ Screenshots

<img width="1891" height="891" alt="Screenshot 2026-03-21 222823" src="https://github.com/user-attachments/assets/897d9029-68d9-4132-8631-7eed3fa146e9" />


---

## 📊 Dataset

* Movie metadata dataset (Kaggle / TMDB)
* link : https://www.kaggle.com/datasets/abdallahwagih/movies

---

## 🔮 Future Improvements

* Add collaborative filtering
* Use deep learning (embeddings)

---

## 🙌 Acknowledgements

* Inspired by Netflix-style recommendation systems
* Dataset sourced from Kaggle

---

## 📬 Contact

If you like this project, feel free to connect!
Linkedin : https://www.linkedin.com/in/chandrapal-deora/
