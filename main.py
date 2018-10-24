import logging
from urllib.parse import urlparse
from pathlib import Path

import click
import requests


def url_to_path(url):
    """Convert URI to a path that can be stored on the file system.

    E.g. https://www.python.org/logo.gif -> https_www.python.org/logo.gif

    Args:
        url (str): URI

    Returns:
        str:
    """
    parsed = urlparse(url)
    return '{}_{}{}'.format(parsed.scheme, parsed.netloc, parsed.path)


def fetch_url(url):
    """Return content of url or None if connection failed.

    No check is done.

    Args:
        url (str):

    Returns:
        bytes or None:
    """
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        logging.warning('connection error: %s', url)
        return None
    except requests.exceptions.MissingSchema:
        logging.warning('invalid url: %s', url)
        return None
    return r.content


def save_to_file(data, file_path):
    """

    Args:
        data (bytes):
        file_path (str):
    """
    path = Path(file_path)

    # mkdir -p (if not exists)
    try:
        path.parent.mkdir(parents=True)
    except FileExistsError:
        pass

    # write to file
    with path.open('wb') as f:
        f.write(data)


def download(url, file_path):
    """

    Args:
        url (str):
        file_path (str):
    """
    data = fetch_url(url)
    if data:
        save_to_file(data=data, file_path=file_path)


@click.command()
@click.argument('inputfile', type=click.File())
@click.argument('savedir')
@click.option('--verbose', is_flag=True)
def main(inputfile, savedir, verbose):
    if verbose:
        logging.basicConfig(level=logging.INFO)

    for line in inputfile:
        url = line.strip()
        if url:
            path = Path(savedir) / url_to_path(url)
            logging.info('downloading: %s', url)
            download(url, str(path))


if __name__ == "__main__":
    main()
