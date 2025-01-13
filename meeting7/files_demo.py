# fd = open("data/alice_in_wonderland.txt")
# print(fd)
#
# content = fd.read()
# print(content[:1000])
#
# fd.close()

with open("data/alice_in_wonderland.txt") as fd:
    # content = fd.read(30)
    # print("content1", content)
    # content = fd.read()
    # print("content2", content)
    # print("is_closed", fd.closed)
    # counter = 0
    # text = ""
    # content = fd.read()
    # fd.seek(0)
    for line in fd:
        print("inside for", line)
        break
        # print(line)
        # counter += len(line.replace(" ",""))
        # text += line

# print("counter", counter)
# print(len(text))

# print(fd.closed)
# print("done")

with open("data/alice_in_wonderland.txt") as fd:
    content = fd.read()

with open("data/alice_in_wonderland.txt") as fd:
    for line in fd:
        print(line)

# /Users/valeria/src/jb/ai-experts/meeting7/data/alice_in_wonderland.txt