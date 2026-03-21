import streamlit as st
from recommender import get_recommendations, movies

st.title("🎬 Movie Recommender")

st.write("Content-based recommendation system")

option = st.radio("Choose input method", ["Type", "Select"])

if option == "Type":
    query = st.text_input("Enter movie name")
else:
    query = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):

    if not query or query.strip() == "":
        st.warning("Please enter a movie name")
    else:
        with st.spinner("Finding recommendations..."):
            results, matched_title = get_recommendations(query)

        if results is not None:
            st.subheader(f"Top recommendations for: {matched_title}")

            for _, row in results.iterrows():
                year = int(row['year']) if str(row['year']).isdigit() else "—"
                rating = round(row['vote_average'], 1)

                st.write(f"🎬 {row['title']} ({year}) ⭐ {rating}")
        else:
            st.error("Movie not found")