data = ""
with open('requirements.txt', 'r') as f:
    data += f.read()

# print(data)
for n in data.splitlines(True):
    if n.startswith("# "):
        print(n)
    else:
        x = n.split("  # ")
        if len(x) > 1:
            print("- " + x[1])
