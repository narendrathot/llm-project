# llm-project
# PubMed Paper Fetcher

This Python project fetches research papers from PubMed based on a user-specified query. It identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

---

## Features

- Fetches papers using the **PubMed API**.
- Filters papers with authors affiliated with pharmaceutical or biotech companies.
- Saves the results in a CSV file with the following columns:
  - **PubmedID**: Unique identifier for the paper.
  - **Title**: Title of the paper.
  - **Publication Date**: Date the paper was published.
  - **Non-academic Author(s)**: Names of authors affiliated with non-academic institutions.
  - **Company Affiliation(s)**: Names of pharmaceutical/biotech companies.
  - **Corresponding Author Email**: Email address of the corresponding author.
- Command-line interface with options for query, output file, and debug mode.

---

## Installation

### Prerequisites

- Python 3.8 or higher.
- Git (optional, for version control).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pubmed-paper-fetcher.git
   cd pubmed-paper-fetcher
