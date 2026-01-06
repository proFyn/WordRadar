import click
import requests
import re
from bs4 import BeautifulSoup

def get_words_of(url):
    resp = requests.get(url)
    try:
    	resp = requests.get(url, timeout=10)
    	resp.raise_for_status()
    except requests.RequestException as e:
    	print(f"Error fetching page: {e}")
    	exit(1)

    soup = BeautifulSoup(resp.content.decode(), 'lxml')
    raw_text = soup.get_text()
    return re.findall(r'\w+', raw_text)

def get_top_words(words, length):
    word_count = {}

    for word in words:
        if len(word) < length:
            continue
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)

@click.command()
@click.option('-u', '--url', prompt='Enter the page url', help='URL page to extract from')
@click.option('-l', '--length', default=0, help='Minimum word length (default: 0, no limit)')
@click.option('-t', '--top', default=5, help='Top word occurrences (default: 5)')
@click.option('-o', '--output', help='File to copy result to')
def main(url, length, top, output):
    PAGE_URL = url
    words = get_words_of(PAGE_URL)
    top_words = get_top_words(words,length)
  

    for i in range(top):
        print(f"{i+1}. {top_words[i][0]} : {top_words[i][1]}")

    if output:
        try:
            with open(output, 'x', encoding='utf-8') as f:
                for i in range(top):
                    f.write(f"{i+1}. {top_words[i][0]} : {top_words[i][1]}\n")
            print(f"Results saved to {output}")
        except FileExistsError:
            print("The file already exists.")

if __name__ == '__main__':
    main()
