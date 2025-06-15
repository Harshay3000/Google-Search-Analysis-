import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🔍 Google Search Analysis Dashboard")
st.markdown("Analyze top Google results on sentiment, topic clustering, and trends.")

# Load the enriched CSV
df = pd.read_csv("google_search_enriched_final.csv")

# Optional cleanup (in case)
df.fillna("", inplace=True)

# Show basic table
if st.checkbox("📄 Show Raw Search Data"):
    st.dataframe(df[["search_title", "url", "source", "sentiment_label", "topic_cluster"]])

# Sentiment Distribution
st.subheader("😊 Sentiment Distribution")
sentiment_counts = df['sentiment_label'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="Set2", ax=ax)
ax.set_ylabel("Count")
st.pyplot(fig)

# Topic Clusters
st.subheader("📚 Topic Cluster Distribution")
cluster_counts = df['topic_cluster'].value_counts().sort_index()
fig2, ax2 = plt.subplots()
sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette="Pastel2", ax=ax2)
ax2.set_ylabel("Count")
st.pyplot(fig2)

# Top sources
#st.subheader("🌐 Top Sources")
#top_sources = df['source'].value_counts().head(10)
#st.bar_chart(top_sources)
# Source distribution
st.subheader("🌐 Source Website Distribution")
if "source" in df.columns:
    top_sources = df["source"].value_counts().head(10)
    fig3, ax3 = plt.subplots()
    sns.barplot(y=top_sources.index, x=top_sources.values, palette="coolwarm", ax=ax3)
    ax3.set_xlabel("Count")
    ax3.set_ylabel("Source")
    st.pyplot(fig3)


# Sentiment by Source
st.subheader("🔗 Sentiment Breakdown by Source")
sentiment_by_source = df.groupby(['source', 'sentiment_label']).size().unstack().fillna(0)
top_sentiment = sentiment_by_source.loc[top_sources.index]
st.dataframe(top_sentiment)

# Download option
st.subheader("⬇️ Download Full Enriched Data")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "google_search_analysis.csv", "text/csv")
