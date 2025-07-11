from bs4 import BeautifulSoup
import requests

def scrape_website(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No title"

        # Find the first meaningful paragraph
        para = "No paragraph found"
        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if text:
                para = text
                break

        return f"Title: {title}\nParagraph: {para}"

    except Exception as e:
        return f"Error scraping website: {str(e)}"

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Black_hole"
    print(scrape_website(url))