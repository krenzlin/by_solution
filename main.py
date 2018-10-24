import click


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