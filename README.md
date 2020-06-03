PythonRTF
=========

A concise module for converting simple RTF documents to plain text.

The "to_plain_text" function takes in the file name of an RTF document, and returns the plain text equivalent of the file's contents. It handles only simple RTF documents, ignoring tables, bulleted lists, etc. It does not validate input. Sample usage:

    from rtf import *
    
    print RTF.to_plain_text("filename.rtf")

The "RTF" class is built around this function, providing additional functionality. It's primary value add is intelligent caching; an "RTF" instance will store the plain text interpretation of its underlying RTF file and only parse it again once it has been marked as having been edited since the instance last parsed it. Sample usage:

    from rtf import *
    
    r = RTF("input_filename.rtf")
    print r.plain_text()
    r.dump("output_filename.txt")
