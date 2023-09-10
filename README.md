# [Königsberg](https://github.com/bergren2/konigsberg) - Python

For a starting project guideline, I'm going to use [City Scrapers](https://github.com/City-Bureau/city-scrapers)
because it's the one Python project I've collaborated on and I know they do good work. I'm also going to supplement with
reading from below:
- [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
    - [Repository Structure and Python](https://kennethreitz.org/essays/2013/01/27/repository-structure-and-python)

## Setup

1. `scoop install python` or `brew install python`
2. `pip install --user pipenv`

> [!NOTE]
> Depending on how you installed Python, you might need to specify Python 3 using `python3` and `pip3`.

## Tests

```shell
python -m pytest tests
```