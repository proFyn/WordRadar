# WordRadar 📊
A lightweight Python CLI tool that scrapes a webpage, extracts text, and calculates the frequency of the most common words.

Built with Python using:  
- [Click](https://click.palletsprojects.com/) for command-line interface  
- [Requests](https://docs.python-requests.org/) for fetching web pages  
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing  

---

## ✨ Features

- **Scrape Any URL:** Extracts text content cleanly from HTML.
- **Word Filtering:** Filter out short words (noise) by specifying a minimum length.
- **Custom Ranking:** Choose how many top words to display.
- **File Export:** Save the analysis results to a text file automatically.
  
---

## 🚀 Installation

#### 1. **Clone the repository:**
```bash
   git clone [https://github.com/proFyn/WordRadar.git](https://github.com/proFyn/WordRadar.git)
   cd WordRadar
```
#### 2. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

## 💻 Usage

#### Basic Usage
The tool will prompt you for the URL if not provided.

```bash
python3 WordRadar.py
```
#### Advanced Usage with Arguments
```bash
python3 WordRadar.py -u [https://example.com](https://example.com) -l 4 -t 10 -o results.txt
```

#### Command Options

Option,Shorthand,Description,Default
--url,-u,The target URL to scrape.,(Prompt)
--length,-l,Minimum character length for words to be counted.,0
--top,-t,Number of top frequent words to display.,5
--output,-o,"File path to save the output (e.g., data.txt).",None

#### 📂 Example Output

```bash
python WordRadar.py -u [https://example.com](https://example.com) -l 5 -t 3
```
####### Terminal Output:

1. example : 12
2. domain : 8
3. established : 4
