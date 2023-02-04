#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import click
import string
import secrets
from typing import List


@click.command()
@click.option(
    "--length",
    "-l",
    "length",
    required=False,
    default=8,
    type=int,
    help="Length of desired password",
)
@click.option(
    "--remove",
    "-r",
    "remove",
    required=False,
    type=str,
    help="Values or characters to be excluded from the created \
        password (Enter values as a string... ex: 'j9_@Dy]'",
)
def main(length: int, remove: str) -> None:
    list_of_vals: List[str] = list(
        string.ascii_letters + string.digits + string.punctuation
    )
    values: str = "".join(list_of_vals)

    if remove:
        for char in remove:
            values.replace(char, "")

    click.echo("".join(secrets.choice(values) for num in range(length)))


if __name__ == "__main__":
    main()
