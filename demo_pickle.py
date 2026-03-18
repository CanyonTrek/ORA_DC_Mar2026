#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO PRESERVE ONE Python
# Object (Data + Structure) to a file using the pickly module.
""" 
    DocString
"""
import pickle
import pprint
import gzip # Others as bz2, tarfile, shutil
movies = { 'joe': ['underworld', 'blade', 'twilight'],
           'brianna': ['the notebook', 'inside out',  'the gentleman'],
           'dayane': ['iron man', 'transformers', 'resident evil'],
           'zac': ['the creator', 'star wars', 'black cauldron']
}

# with open(r"f:\labs\projects\ORA_DC_Mar2026\movies.p", mode="wb") as fh_out:
with gzip.open(r"f:\labs\projects\ORA_DC_Mar2026\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Pickle protocol (0=ascii, 1-5 Binary)
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Default=4
    # pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # Default=5

# with open(r"f:\labs\projects\ORA_DC_Mar2026\movies.p", mode="rb") as fh_in:
with gzip.open(r"f:\labs\projects\ORA_DC_Mar2026\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)