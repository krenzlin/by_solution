from urllib.parse import urlparse

import click
import requests


def url_to_path(url):
    parsed = urlparse(url)
    return '{}_{}{}'.format(parsed.scheme, parsed.netloc, parsed.path)


def download(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)


@click.command()
@click.argument('inputfile', type=click.File())
@click.argument('savedir')
def main(inputfile, savedir):
    for line in inputfile:
        url = line.strip()
        if url:
            print(url)


if __name__ == "__main__":
    main()
