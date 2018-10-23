import sys


if __name__ == "__main__":
    filename = sys.argv[1]
    savedir = sys.argv[2]
    print('reading: {}'.format(filename))

    with open(filename) as f:
        for line in f:
            url = line.strip()
            if url:
                print(url)
