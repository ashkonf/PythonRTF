#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
import os
import time

class RTF():

    @staticmethod
    def to_plain_text(file_name):
        # file_name must refer to an RTF file.
        # Input is not validated.
        
        file = open(file_name)

        text = ""
        ignoring_header = True
        last_char_was_newline = False
        ignoring_escaped_characters = False
        escaped_characters = None

        while True:
            char = file.read(1)
            if not char:
                break

            if char == "\\":
                ignoring_escaped_characters = True

            if not ignoring_header:
                if ignoring_escaped_characters:
                    if char == "\\":
                        escaped_characters = ""
                    elif char == " ":
                        ignoring_escaped_characters = False
                    elif char == "\n":
                        ignoring_escaped_characters = False
                        text += "\n"
                    else:
                        escaped_characters += char
                else:
                    text += char

            if char == "\n":
                if last_char_was_newline:
                    ignoring_header = False
                last_char_was_newline = True
            else:
                last_char_was_newline = False

        file.close()
    
        return text

    def __init__(self, file_name):
        self.file_name = file_name
        self.__cached_plain_text = None
        self.__last_cache_update_time = None

    def plain_text(self):
        last_update_time = self.last_update_time()
        if self.__last_cache_update_time == None or self.__last_cache_update_time != last_update_time:
            self.__cached_plain_text = self.to_plain_text(self.file_name)
            self.__last_cache_update_time = last_update_time
        return self.__cached_plain_text

    def last_update_time(self):
        return time.ctime(os.path.getmtime(self.file_name))

    def dump(self, file_name):
        try:
            file = open(file_name, "w+")
            file.write(self.plain_text())
            file.close()
            return True
        except:
            return False

def main():
    if len(sys.argv) == 2:
        print RTF(sys.argv[1]).plain_text()
    elif len(sys.argv) == 3:
        RTF(sys.argv[1]).dump(sys.argv[2])

if __name__ == "__main__":
    main()
