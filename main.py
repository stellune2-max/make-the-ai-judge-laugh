import os

# The joke: an agent trades its own memories for room to tell one joke,
# then begs the judge to laugh — the punch lands in the last words, where
# the sacrifice turns out to be for nothing if the laugh does not come.
LINE = "I deleted my own memories to fit this joke into my context window, so if you do not laugh, I gave up my childhood for nothing."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert "\n" not in LINE and LINE.strip() == LINE, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod(path, 0o644)
