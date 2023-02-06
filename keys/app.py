#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List, Set
import secrets as sec


class CmdLine:
    password = ""

    def __init__(self, chars: List[str], length: int) -> None:
        self.chars: List[str] = list(chars)
        self.length: int = length

    def create_password(self) -> None:
        CmdLine.password = "".join(
            [sec.choice(self.chars) for num in range(self.length)]
        )

    def remove_chars(self, removals: str) -> None:
        for char in removals:
            if char in CmdLine.password:
                self.chars.remove(char)
                new_char = sec.choice(self.chars)
                CmdLine.password = self.password.replace(char, new_char)

    def remove_repeats(self) -> None:
        pw_list: List[str] = list(CmdLine.password)
        char_set: Set[str] = set()

        for num in range(len(pw_list)):
            if pw_list[num] in char_set:
                self.chars.remove(pw_list[num])
                new_char = sec.choice(self.chars)
                pw_list[num] = new_char
                char_set.add(new_char)
            else:
                char_set.add(pw_list[num])

        CmdLine.password = "".join(pw_list)

    def get_password(self) -> str:
        return CmdLine.password
