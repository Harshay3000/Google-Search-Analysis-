# Google-Search-Analysis-

This project performs an end-to-end analysis of **Google search results** using web scraping, natural language processing (NLP), sentiment analysis, topic clustering, and visual insights generation. Developed in Jupyter Notebook and deployed using Streamlit.

---

## 📌 Project Workflow

### ✅ Phase 1: Web Scraping
- Uses `Selenium` and `BeautifulSoup` to scrape top Google search results.
- Extracted: `Title`, `URL`, `Snippet`, and `Main Text`.

### ✅ Phase 2: Data Enrichment
- Cleaned text data and added a `source` (website domain) column.
- Fetched and stored main content from each search result.

### ✅ Phase 3: NLP Analysis
- **Keyword Extraction**: Extracted key phrases using RAKE.
- **Sentiment Analysis**: Used `TextBlob` to label results as Positive, Negative, or Neutral.
- **Topic Clustering**: Grouped articles using `TF-IDF` and `KMeans`.

### ✅ Phase 4: Insight Generation
- Visualized:
  - Sentiment distribution
  - Keyword frequency
  - Source website contributions
  - Topic clusters using `Plotly`, `Matplotlib`, and `Seaborn`.

### ✅ Phase 5: Streamlit Deployment
- Developed `app.py` to host the project as an interactive web app.
- Included light/dark theme toggle and simplified dashboard.

---

## 🛠️ Tech Stack

| Tool          | Purpose                        |
|---------------|--------------------------------|
| `Jupyter`     | Development & data analysis    |
| `Pandas`      | Data manipulation              |
| `Selenium`    | Web scraping automation        |
| `BeautifulSoup` | HTML parsing               |
| `TextBlob`    | Sentiment analysis             |
| `RAKE`        | Keyword extraction             |
| `Scikit-learn`| Clustering                     |
| `Plotly`, `Seaborn`, `Matplotlib` | Visualization |
| `Streamlit`   | Web app deployment             |

---

## 🚀 How to Run the Project

### 🔧 1. Clone the repository

```bash
git clone https://github.com/your-username/google-search-analysis.git
cd google-search-analysis

###  📦 2. Install dependencies
pip install -r requirements.txt

###  💡 3. Run the Streamlit App
streamlit run app.py
