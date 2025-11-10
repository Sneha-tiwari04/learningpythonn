import keyword

all_key=keyword.kwlist
print(all_key)
print(len(all_key))

soft_key=keyword.softkwlist
print(soft_key)
print(len(soft_key))

total_key=keyword.kwlist+keyword.softkwlist
print(total_key)
print(len(total_key))
