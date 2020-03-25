import random

def expand(text):
    for c, _ in enumerate(text, 1):
        yield (' '*c).join(list(text))
    yield (' '*(len(text)+1)).join(list(text))
    for c, _ in reversed(list(enumerate(text, 1))):
        yield (' '*c).join(list(text))