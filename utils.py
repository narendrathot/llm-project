import pandas as pd

def save_to_csv(data: List[Dict], filename: str):
    """Save the fetched papers to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)