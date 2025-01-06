def batches(n, my_list):
    first_idx = 0
    while len(my_list) > first_idx:
        yield my_list[first_idx:first_idx+n]
        first_idx += n


if __name__ == '__main__':
    text = "What a beautiful day, the sky is blue"
    for batch in batches(5, text):
        print(batch)