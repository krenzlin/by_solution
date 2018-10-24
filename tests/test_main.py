def test_download(tmpdir):
    from main import download

    url = 'https://www.python.org/static/img/python-logo.png'

    filename = tmpdir / 'python-logo.png'

    assert filename.exits() is False

    download(url, filename)

    assert filename.exits() is True
