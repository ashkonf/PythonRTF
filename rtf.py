#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
import os
import time

class RTF():

    # fileName must refer to an RTF file.
    # Input is not validated.
    @staticmethod
    def rtfToPlainText(fileName):
        file = open(fileName)

        text = ""
        ignoringHeader = True
        lastCharWasNewline = False
        ignoringEscapedCharacters = False
        escapedCharacters = None

        while True:
            char = file.read(1)
            if not char:
                break

            if char == "\\":
                ignoringEscapedCharacters = True

            if not ignoringHeader:
                if ignoringEscapedCharacters:
                    if char == "\\":
                        escapedCharacters = ""
                    elif char == " ":
                        ignoringEscapedCharacters = False
                    elif char == "\n":
                        ignoringEscapedCharacters = False
                        text += "\n"
                    else:
                        escapedCharacters += char
                else:
                    text += char

            if char == "\n":
                if lastCharWasNewline:
                    ignoringHeader = False
                lastCharWasNewline = True
            else:
                lastCharWasNewline = False

        file.close()
    
        return text

    def __init__(self, fileName):
        self.fileName = fileName
        self.__cachedPlainText = None
        self.__lastCacheUpdateTime = None

    def plainText(self):
        lastUpdateTime = self.lastUpdateTime()
        if self.__lastCacheUpdateTime == None or self.__lastCacheUpdateTime != lastUpdateTime:
            self.__cachedPlainText = rtfToPlainText(self.fileName)
            self.__lastCacheUpdateTime = lastUpdateTime
        return self.__cachedPlainText

    def lastUpdateTime(self):
        return time.ctime(os.path.getmtime(self.fileName))

    def toTXT(self, fileName):
        try:
            file = open(fileName, "w+")
            file.write(self.plainText())
            file.close()
            return True
        except:
            return False

def main():
    if len(sys.argv) == 2:
        print RTF(sys.argv[1]).plainText()
    elif len(sys.argv) == 3:
        RTF(sys.argv[1]).toTXT(sys.argv[2])

if __name__ == '__main__':
    main()
