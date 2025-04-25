def normaltext(s: str):
    _res = s.strip().split()
    res = " ".join(_res)
    return res


def main():
    import sys
    text = sys.stdin.read()  # đọc toàn bộ input tới EOF
    text = text.strip()

    start = 0
    for idx, char in enumerate(text):
        if char in ['.', '?', '!']:
            raw = text[start:idx]
            cleaned = normaltext(raw)
            if cleaned:
                cleaned = cleaned.lower()
                cleaned = cleaned[0].upper() + cleaned[1:]
                print(cleaned)
            start = idx + 1  # bỏ qua dấu kết thúc câu


if __name__ == "__main__":
    main()
