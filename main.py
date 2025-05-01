import arxiv
import datetime
from models import ArxivArticle, Author

def search_arxiv_articles(query, max_results=10):
    """
    Search for articles on arXiv based on the given query.
    
    Args:
        query (str): The search query
        max_results (int): Maximum number of results to return
    
    Returns:
        list[Article]: List of Article objects
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    articles = []
    for result in search.results():
        article = ArxivArticle(
            title=result.title,
            authors=[Author(name=author.name) for author in result.authors],
            published=result.published,
            summary=result.summary,
            entry_id=result.entry_id,
            pdf_url=result.pdf_url,
            primary_category=result.primary_category,
            categories=result.categories,
            doi=result.doi
        )
        articles.append(article)
    
    return articles

def main():
    print("Searching for articles about multi-agent systems...")
    
    # Search for articles
    articles = search_arxiv_articles("multi-agent systems", max_results=5)
    
    # Print results
    print(f"\nFound {len(articles)} articles:\n")
    for i, article in enumerate(articles, 1):
        print(f"Article {i}:")
        print(article)
        print("-" * 80)

if __name__ == "__main__":
    main()
