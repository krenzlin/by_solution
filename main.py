import click


@click.command()
@click.argument('filename')
@click.argument('savedir')
def main(filename, savedir):
    print('reading: {}'.format(filename))

    with open(filename) as f:
        for line in f:
            url = line.strip()
            if url:
                print(url)


if __name__ == "__main__":
    main()
