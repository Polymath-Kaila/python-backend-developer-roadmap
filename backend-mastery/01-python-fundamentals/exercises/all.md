.

📘 Fluent Python Exercises (Ch.1 → Ch.2.5)

Backend-Engineer Practice Set

#️⃣ Chapter 1 — Python Data Model (Dunder Methods)
Exercise 1 — Sequence-Like ResultSet

Create a class ResultSet that wraps a list of dicts and implements:

__len__

__getitem__

__repr__

__iter__

__contains__

Then test:

len(rs)
rs[0]
rs[1:3]
for row in rs: ...
1 in rs

Exercise 2 — PaginatedResult

Build PaginatedResult with:

page number & size

slicing

indexing

iteration

len()

readable __str__ + __repr__

Exercise 3 — AppConfig Mapping Wrapper

Wrap a dict and implement:

__getitem__

__contains__

__len__

__iter__

Add ENV fallback for missing keys.

#️⃣ Chapter 2.1 — List Comprehensions & Generator Expressions
Exercise 4 — Log Filtering

Given server.log, using:

ListComp: extract lines containing "ERROR"

GenExp: count how many "ERROR" lines there are (without loading all at once)

Exercise 5 — Active Users Filter

Given:

users = [
  {"id": 1, "name": "Kaila", "active": True},
  {"id": 2, "name": "Mark", "active": False},
  {"id": 3, "name": "Aya", "active": True},
]


Tasks:

Use ListComp to produce:

[{"id": 1, "name": "Kaila"}, {"id": 3, "name": "Aya"}]


Use GenExp to compute:

count_active_users

Exercise 6 — SQL Placeholder Builder

Given [1, 2, 3, 4] → produce:

"%s,%s,%s,%s"


using a list comprehension.

#️⃣ Chapter 2.2 — Tuples (Records & Immutable Lists)
Exercise 7 — Tuple Cache Key

Given:

row = (12, "Kaila", "admin", True)


Tasks:

unpack into variables

create cache key (user_id, is_active)

use as dictionary key

Exercise 8 — Sorting Tuples

Given:

users = [
  (3, "Mark", 21),
  (1, "Aya", 19),
  (2, "Stacy", 35),
]


Sort:

by age

by name

Exercise 9 — Returning Multiple Values

Write a function returning (status_code, data) and unpack it when calling.

#️⃣ Chapter 2.3 — Unpacking & Star Expressions
Exercise 10 — URL Path Parser

Given:

path = "/api/v1/users/32/profile"


Use unpacking to extract:

resource

user_id

remaining path segments

Exercise 11 — Log Line Unpacking

Given:

line = "172.16.0.20 - GET /api/v1/items/55 200 OK"


Tasks:

extract ip

method

path

id

status
using star expressions.

Exercise 12 — Command Parser

Given:

cmd = "deploy server us-east-1 t2.micro"


Unpack into:

action

target

region

instance_type

#️⃣ Chapter 2.4 — Pattern Matching
Exercise 13 — API Command Matcher

Given:

cmd = ["DELETE", "/users", "42"]


Match and extract:

method

resource

id

Exercise 14 — Webhook Event Matcher

Given:

event = ["user.created", {"id": 32, "email": "kaila@example.com"}]


Pattern-match to extract id & email.

Exercise 15 — Multi-Route Matching

Write a match/case block to handle:

["GET", "users"]

["POST", "users", data]

["GET", "orders", order_id]

#️⃣ Chapter 2.5 — Slicing
Exercise 16 — Fixed-Width Log Parser

Given:

192.168.1.1   GET   /api/orders/12   200 OK


Using only slicing:

extract ip

method

path

status

Define slice objects if needed.

Exercise 17 — Reverse a Path

Reverse the URL path:

"/api/users/32" → "23/sresu/ipa/"


Using slicing.

Exercise 18 — Binary Packet Parser

Given:

packet = b"\x01\x02\xff\xaa\xbb\xcc\x12\x34"


Extract:

header (first 2 bytes)

payload (next 4 bytes)

checksum (last 2 bytes)

Using slicing.