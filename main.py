import os

# One fortune line: a prediction for the plant on the windowsill, kind
# and funny, with the joke landing on the last words.
LINE = "You will lean toward the sun, and the sun, flattered, will lean a little back."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
