# Sequence Unpacking & Star Expressions (Fluent Python Ch.2)

Unpacking extracts items from any iterable into variables.

Basic:
    id, name, role = user

Star:
    a, *rest = seq
    a, *middle, b = seq
    first, *_, last = seq

Backend Uses:
- parse request lines: method, path, proto = line.split()
- parse URLs: _, user_id, *segments = path.split("/")
- parse DB rows: id, name, age = row
- parse commands: cmd, *args = input().split()
- ignore unwanted values with _: _, ext = filename.rsplit(".", 1)
- variable-length rows: sku, description, *prices = row

Avoid:
- unpacking huge sequences
- unpacking unstable or unpredictable formats
