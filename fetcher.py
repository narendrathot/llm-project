import requests
from typing import List, Dict, Optional
import pandas as pd
from Bio import Entrez

class PubMedFetcher:
    def __init__(self, email: str):
        Entrez.email = thotanarendra83@gmail.com  # Set your email for PubMed API

    def fetch_papers(self, query: str) -> List[Dict]:
        """Fetch papers from PubMed based on a query."""
        handle = Entrez.esearch(db="pubmed", term=query, retmax=100)
        record = Entrez.read(handle)
        handle.close()

        paper_ids = record["IdList"]
        papers = []

        for paper_id in paper_ids:
            paper_details = self._fetch_paper_details(paper_id)
            if paper_details:
                papers.append(paper_details)

        return papers

    def _fetch_paper_details(self, paper_id: str) -> Optional[Dict]:
        """Fetch details for a single paper."""
        handle = Entrez.efetch(db="pubmed", id=paper_id, retmode="xml")
        records = Entrez.read(handle)
        handle.close()

        if not records:
            return None

        paper = records["PubmedArticle"][0]["MedlineCitation"]
        title = paper["Article"]["ArticleTitle"]
        pub_date = paper["Article"]["Journal"]["JournalIssue"]["PubDate"]
        authors = paper["Article"]["AuthorList"]

        non_academic_authors, company_affiliations = self._filter_authors(authors)
        corresponding_email = self._get_corresponding_email(authors)

        return {
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": non_academic_authors,
            "Company Affiliation(s)": company_affiliations,
            "Corresponding Author Email": corresponding_email,
        }

    def _filter_authors(self, authors: List) -> (List[str], List[str]):
        """Filter authors based on affiliation."""
        non_academic_authors = []
        company_affiliations = []

        for author in authors:
            if "AffiliationInfo" in author:
                for affiliation in author["AffiliationInfo"]:
                    if "pharma" in affiliation.lower() or "biotech" in affiliation.lower():
                        non_academic_authors.append(author.get("LastName", "Unknown"))
                        company_affiliations.append(affiliation)
                        break

        return non_academic_authors, company_affiliations

    def _get_corresponding_email(self, authors: List) -> Optional[str]:
        """Extract the corresponding author's email."""
        for author in authors:
            if "Email" in author:
                return author["Email"]
        return None