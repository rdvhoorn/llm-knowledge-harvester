from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List

class Author(BaseModel):
    name: str

class ArxivArticle(BaseModel):
    # The title of the article
    title: str

    # List of authors who wrote the article
    authors: List[Author]

    # When the article was published on arXiv
    published: datetime

    # Abstract/summary of the article's content
    summary: str

    # The unique arXiv URL identifier for this article
    entry_id: HttpUrl

    # Direct link to PDF version, if available
    pdf_url: HttpUrl | None = None

    # Main research category (e.g. cs.AI, physics.comp-ph)
    primary_category: str | None = None

    # All research categories this article belongs to
    categories: List[str] | None = None
    
    # Digital Object Identifier, if assigned
    doi: str | None = None 

    def __str__(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Authors: {', '.join(author.name for author in self.authors)}\n"
            f"Published: {self.published}\n"
            f"Summary: {self.summary}\n"
            f"Entry ID: {self.entry_id}\n"
            f"PDF URL: {self.pdf_url}\n"
            f"Primary Category: {self.primary_category}\n"
            f"Categories: {', '.join(self.categories) if self.categories else 'None'}\n"
            f"DOI: {self.doi}"
        )