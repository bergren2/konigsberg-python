![Build Status](https://github.com/bergren2/konigsberg-python/workflows/build/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/776d6d4cc92c0915434c/maintainability)](https://codeclimate.com/github/bergren2/konigsberg-python/maintainability)

# [Königsberg](https://github.com/bergren2/konigsberg) - Python

Started using Python at work and chose to align this with the stack used there, which is mainly `uv`.

## Prereqs
- [uv](https://docs.astral.sh/uv/#installation)
- [ruff](https://docs.astral.sh/ruff/installation/)

## Setup

```shell
uv python install
uv sync
```

## Linting

```shell
ruff check
```

## Tests

```shell
uv run pytest
```

## Further Reading

- https://www.jetbrains.com/help/pycharm/uv.html