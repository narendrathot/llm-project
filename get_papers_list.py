import argparse
from pubmed_fetcher.fetcher import PubMedFetcher
from pubmed_fetcher.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="PubMed query to search for papers.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save the results.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information.")
    args = parser.parse_args()

    fetcher = PubMedFetcher(email="thotanarendra83@gmail.com")
    papers = fetcher.fetch_papers(args.query)

    if args.file:
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()