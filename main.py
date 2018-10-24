import logging
from urllib.parse import urlparse
from pathlib import Path

import click
import requests


def url_to_path(url):
    parsed = urlparse(url)
    return '{}_{}{}'.format(parsed.scheme, parsed.netloc, parsed.path)


def fetch_url(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        logging.warning('connection error: %s', url)
        return None
    return r.content


def save_to_file(data, file_path):
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
