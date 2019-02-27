"""Uses SHA-1 to hash a string given"""


import argparse


def sha1(text:str):
    """Converts text string to SHA-1 hashed

    Args:
        text: a string that will hashed by the SHA-1 algo

    Returns:
        A string representing the hashed version of text

    """

    txt_list = list(text)
    ascii_list = [ord(w) for w in txt_list]
    bin_list = [format(w, '08b') for w in ascii_list]
    joined = ''.join(bin_list) + '1'

    while(len(joined) % 512 != 448):
        joined += '0'

    suffix = format(len(joined), '08b')

    while(len(suffix) % 64 != 0):
        suffix = '0' + suffix

    joined += suffix

    # break into 512 bit chunks
    chunks = [joined[512*i:512*(i+1)] for i in range(0, int(len(joined)/512))]

    # break each chunk to 32 bit subarrays
    new_chunks = []
    for c in chunks:
        new_chunks.append([c[32*i:32*(i+1)] for i in range(0, 16)])

    return(new_chunks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--string', help='String to hash')
    args = parser.parse_args()

    text_to_hash = args.string

    hashed = sha1(text_to_hash)
    print(hashed)


if __name__ == "__main__":
    main()