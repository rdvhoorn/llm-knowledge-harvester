from datetime import datetime, timedelta
import arxivscraper
import pandas as pd
from typing import List, Dict
import json
from models import ArxivArticle
import gradio as gr

def fetch_arxiv_articles(start_date: str, end_date: str, category: str = "cs.AI") -> List[ArxivArticle]:
    """
    Fetch articles from arXiv for the given date range.
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        category (str): arXiv category to search in
        
    Returns:
        List[ArxivArticle]: List of ArxivArticle objects
    """
    scraper = arxivscraper.Scraper(
        category="cs",
        date_from=start_date,
        date_until=end_date,
        t=10,
        filters={"categories": [category]},
    )
    raw_articles = scraper.scrape()
    
    # Convert raw dictionaries to ArxivArticle objects
    articles = []
    for raw_article in raw_articles:
        try:
            # Handle both missing and empty string dates
            created_date = raw_article.get('created', '')
            updated_date = raw_article.get('updated', '')
            
            # Use start_date if date is missing or empty
            if not created_date:
                created_date = start_date
            if not updated_date:
                updated_date = start_date
                
            raw_article['created'] = datetime.strptime(created_date, '%Y-%m-%d')
            raw_article['updated'] = datetime.strptime(updated_date, '%Y-%m-%d')
            articles.append(ArxivArticle(**raw_article))
        except Exception as e:
            print(f"Error converting article {raw_article.get('id', 'unknown')}: {str(e)}")
            continue
    
    return articles

def search_articles(start_date: datetime, end_date: datetime, category: str, max_results: int) -> str:
    """
    Search for articles and return formatted results.
    
    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        category (str): arXiv category to search in
        max_results (int): Maximum number of results to display
        
    Returns:
        str: Formatted results
    """
    try:        
        articles = fetch_arxiv_articles(start_date, end_date, category)
        
        if not articles:
            return "No articles found for the specified criteria."
        
        # Format results
        output = [f"Found {len(articles)} articles. Displaying first {max_results}:\n"]
        
        for i, article in enumerate(articles[:max_results], 1):
            output.append(f"Article {i}:")
            output.append(repr(article))
            output.append("-" * 80)
        
        return "\n".join(output)
    
    except ValueError as e:
        return "Error: Please enter dates in YYYY-MM-DD format"
    except Exception as e:
        return f"Error occurred: {str(e)}"

def create_interface():
    """Create and launch the Gradio interface."""
    # Available categories
    categories = [
        "cs.AI", "cs.CL", "cs.CV", "cs.LG", "cs.NE", 
        "cs.RO", "cs.SE", "cs.SI", "cs.SY"
    ]
    
    # Get default dates
    default_start = datetime.now() - timedelta(days=7)
    default_end = datetime.now() - timedelta(days=6)
    
    # Create interface
    interface = gr.Interface(
        fn=search_articles,
        inputs=[
            gr.DateTime(
                label="Start Date",
                value=default_start.strftime("%Y-%m-%d"),
                include_time=False,
                type="string"
            ),
            gr.DateTime(
                label="End Date",
                value=default_end.strftime("%Y-%m-%d"),
                include_time=False,
                type="string"
            ),
            gr.Dropdown(choices=categories, value="cs.AI", label="Category"),
            gr.Slider(minimum=1, maximum=20, value=5, step=1, label="Number of Results")
        ],
        outputs=gr.Textbox(label="Search Results", lines=20),
        title="arXiv Article Search",
        description="Search for academic articles on arXiv. Select a date range, category, and number of results.",
        examples=[
            [default_start.strftime("%Y-%m-%d"), default_end.strftime("%Y-%m-%d"), "cs.AI", 5],
            [(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"), default_end.strftime("%Y-%m-%d"), "cs.LG", 3],
            [(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"), default_end.strftime("%Y-%m-%d"), "cs.CL", 5]
        ],
        theme=gr.themes.Soft()
    )
    return interface

def main():
    interface = create_interface()
    interface.launch()

if __name__ == "__main__":
    main()

