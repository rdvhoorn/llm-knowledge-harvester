from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
from typing import List, Optional

class Author(BaseModel):
    name: str

class ArxivArticle(BaseModel):
    """Model representing an arXiv article."""
    
    title: str = Field(..., description="Title of the article")
    id: str = Field(..., description="arXiv ID of the article")
    abstract: str = Field(..., description="Abstract of the article")
    categories: str = Field(..., description="Space-separated list of arXiv categories")
    doi: str = Field(default="", description="Digital Object Identifier")
    created: datetime = Field(..., description="Date when the article was first created")
    updated: datetime = Field(..., description="Date when the article was last updated")
    authors: List[str] = Field(..., description="List of author names")
    affiliation: List[str] = Field(default_factory=list, description="List of author affiliations")
    url: HttpUrl = Field(..., description="URL to the article on arXiv")
    
    @property
    def pdf_url(self) -> str:
        """Get the PDF URL for the article."""
        return f"https://arxiv.org/pdf/{self.id}.pdf"
    
    @property
    def category_list(self) -> List[str]:
        """Get the list of categories."""
        return self.categories.split()
    
    def __str__(self) -> str:
        """Simple string representation showing just the title."""
        return self.title
    
    def __repr__(self) -> str:
        """Detailed string representation of the article."""
        return (
            f"Title: {self.title}\n"
            f"Authors: {', '.join(self.authors)}\n"
            f"Published: {self.created.strftime('%Y-%m-%d')}\n" 
            f"Updated: {self.updated.strftime('%Y-%m-%d')}\n"
            f"Abstract: {self.abstract}\n"
            f"URL: {self.url}\n"
            f"PDF: {self.pdf_url}\n"
            f"Categories: {self.categories}\n"
            f"DOI: {self.doi if self.doi else 'Not available'}"
        )