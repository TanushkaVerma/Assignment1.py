#Write a program in python that checks if a string starts with a given prefix 
#or ends with a given suffix.

def starts_or_ends_with(string, prefix=None, suffix=None):
    starts_with_prefix = False
    ends_with_suffix = False

    if prefix is not None:
        starts_with_prefix = string.startswith(prefix)

    if suffix is not None:
        ends_with_suffix = string.endswith(suffix)

    return starts_with_prefix, ends_with_suffix



