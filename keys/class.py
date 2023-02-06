#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List
import secrets as sec


class CmdLine:
    def __init__(self, chars: List[str], length: int) -> None:
        self.chars: List[str] = chars
        self.length: int = length
        self.password: str = "".join(
            [sec.choice(self.chars) for num in range(self.length)]
        )

    def remove_chars(self, removals: str) -> None:
        for char in removals:
            if char in self.password:
                self.chars.remove(char)
                new_char = sec.choice(self.chars)
                self.password = self.password.replace(char, new_char)

    def remove_repeats(self) -> None:
        pass

    def get_password(self) -> str:
        return self.password
