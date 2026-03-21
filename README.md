# 🎬 Movie Recommender System

A hybrid movie recommendation system built using Python and Streamlit.
It suggests movies based on content similarity and weighted rating system.

---

## 🚀 Features

* 🔍 Content-based recommendations using TF-IDF
* ⭐ IMDB-style weighted rating system
* 🎯 Hybrid recommendation (similarity + weighted rating system)
* 🌐 Interactive UI with Streamlit
* ⚡ Fast similarity search using cosine similarity

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

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Pickle (for model storage)
* uv (environment & dependency management)
* google collab

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
