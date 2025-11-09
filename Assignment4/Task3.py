def format_name(full_name: str) -> str:
    parts = full_name.strip().split()
    if not parts:
        return ""
    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{last}, {first}" if first else last

# usage examples
print(format_name("John Smith"))        # Smith, John
print(format_name("Mary Ann Evans"))    # Evans, Mary Ann
print(format_name("José del Río"))      # del Río, José