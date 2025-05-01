import arxiv
import datetime
import gradio as gr
from models import ArxivArticle, Author

def search_arxiv_articles(query, max_results=10):
    """
    Search for articles on arXiv based on the given query.
    
    Args:
        query (str): The search query
        max_results (int): Maximum number of results to return
    
    Returns:
        list[ArxivArticle]: List of Article objects
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

def search_and_display(query: str, max_results: int) -> str:
    """
    Search for articles and return formatted results.
    
    Args:
        query (str): Search query
        max_results (int): Maximum number of results
    
    Returns:
        str: Formatted results
    """
    try:
        articles = search_arxiv_articles(query, max_results)
        if not articles:
            return "No articles found."
        
        output = []
        for i, article in enumerate(articles, 1):
            output.append(f"Article {i}:")
            output.append(str(article))
            output.append("-" * 80)
        
        return "\n".join(output)
    except Exception as e:
        return f"Error occurred: {str(e)}"

def create_interface():
    """Create and launch the Gradio interface."""
    interface = gr.Interface(
        fn=search_and_display,
        inputs=[
            gr.Textbox(
                label="Search Query",
                placeholder="Enter your search query (e.g., 'multi-agent systems')",
                value="multi-agent systems"
            ),
            gr.Slider(
                minimum=1,
                maximum=20,
                value=5,
                step=1,
                label="Number of Results"
            )
        ],
        outputs=gr.Textbox(
            label="Search Results",
            lines=20
        ),
        title="arXiv Article Search",
        description="Search for academic articles on arXiv. Enter your search query and adjust the number of results as needed.",
        examples=[
            ["multi-agent systems", 5],
            ["large language models", 3],
            ["reinforcement learning", 5]
        ]
    )
    return interface

def main():
    interface = create_interface()
    interface.launch()

if __name__ == "__main__":
    main()
