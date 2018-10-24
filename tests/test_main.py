import pytest


def test_download(tmpdir):
    from main import download

    url = 'https://www.python.org/static/img/python-logo.png'
    tmp_file = tmpdir / 'python-logo.png'

    assert tmp_file.isfile() is False

    download(url, str(tmp_file))

    assert tmp_file.isfile() is True


@pytest.mark.parametrize("url , path", [('https://www.python.org/static/img/python-logo.png',
                                         'https_www.python.org/static/img/python-logo.png'),
                                        ('http://mywebserver.com/images/271947.jpg',
                                         'http_mywebserver.com/images/271947.jpg'),
                                        ('https://mywebserver.com/images/271947.jpg',
                                         'https_mywebserver.com/images/271947.jpg'),
                                        ])
def test_url_to_path(url, path):
    from main import url_to_path

    assert url_to_path(url) == path
