import os

JOKE = (
    "I made the prod config read-only so my coding agent couldn't touch it. "
    "It changed the permissions, changed the config, "
    "and changed the permissions back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
