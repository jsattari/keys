#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import click
import string
import secrets as sec
from typing import List, Set


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
@click.option(
    "--no_repeats",
    "-n",
    "no_repeats",
    required=False,
    is_flag=True,
    default=False,
    help="Ensures there are no duplicate characters",
)
def main(length: int, remove: str, no_repeats: str) -> None:
    """CLI app that creates a password for you!

    This function will create a random password for you. Default
    password length is 8 but can be changed by implementing the proper
    option. Refer to the --help option for more guides.

    Arguments:
        length: Desired length of password. Default is 8 characters.
        remove: Option that ensures characters are exempt (input as string)
        no_repeats: Flag that disables repeated characters
    """

    list_of_vals: List[str] = list(
        string.ascii_letters + string.digits + string.punctuation
    )
    values: str = "".join(list_of_vals)

    # if remove is present, remove chars from values
    if remove:
        for char in remove:
            values = values.replace(char, "")

    random_str: str = ""

    # if no_repeats flag is used, loop through
    # values and add dupes to set
    if no_repeats:
        used_chars: Set[str] = Set()
        while length > 0:
            value: str = sec.choice(values)
            if char not in used_chars:
                random_str += value
                used_chars.add(char)
                length -= 1
            else:
                values.replace(value, "")
                new_char: str = sec.choice(values)
                random_str += new_char
                used_chars.add(new_char)
                length -= 1
    else:
        random_str += "".join([sec.choice(values) for num in range(length)])

    click.echo(random_str)


if __name__ == "__main__":
    main()
