import os
from typing import Iterator

import requests


def access(dois: Iterator[str]) -> Iterator[str]:
    """Excludes dois that are not open access and returns the remaining list."""
    return (doi for doi in dois if open_access(doi))


def open_access(doi: str) -> bool:
    """Checks whether doi is open access."""
    email = os.environ["UNPAYWALL_EMAIL"]
    uri = f"https://api.unpaywall.org/v2/{doi}?email={email}"
    return requests.get(uri).json()["is_oa"]
