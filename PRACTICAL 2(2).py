nested_tuple = (
("Scala", 301),
("Java", 302),
("TOC", 303)
)
sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])
print("Sorted Subjects (by subject code):", sorted_subjects)
