#!/usr/bin/env python3

import os 
import json

# PRINT OUT ALL ENV VARIABLES AS PLAIN TEXT

# print("Content-Type: text/plain") # let browser know to expect plain text
# print()
# print(os.environ)


# PRINT ENV VARIABLES AS JSON

# print("Content-Type: application/json") # let browser know to expect json
# print()
# print(json.dumps(dict(os.environ),indent=2))


# PRINT QUERY PARAMETER DATA IN HTML

print("Content-Type: text/html") # let browser know to expect html
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")