def test_download(tmpdir):
    from main import download

    url = 'https://www.python.org/static/img/python-logo.png'
    tmp_file = tmpdir / 'python-logo.png'

    assert tmp_file.isfile() is False

    download(url, str(tmp_file))

    assert tmp_file.isfile() is True
