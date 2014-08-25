PythonRTF
=========

A concise module for converting simple RTF documents to plain text.

The "rtfToPlainText" function takes in the file name of an RTF document, and returns the plain text equivalent of the file's contents. It handles only simple RTF documents, ignoring tables, bulleted lists, etc. It does not validate input.

The "RTF" class is built around this function, providing additional functionality. It's primary value add is intelligent caching.
