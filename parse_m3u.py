def parse_m3u(file_path):
    channels = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                channels.append(line)
    return channels

if __name__ == "__main__":
    urls = parse_m3u("playlist.m3u")
    print(f"Found {len(urls)} streams!")
