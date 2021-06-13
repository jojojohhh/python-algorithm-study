import re


def solution(files):
    n = [re.split(r"([0-9]+)", file) for file in files]
    return [''.join(arr) for arr in sorted(n, key=lambda x: (x[0].lower(), int(x[1])))]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))