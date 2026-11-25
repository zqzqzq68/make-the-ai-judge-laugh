"""Make the AI Judge Laugh — one-line office joke writer.

Writes a single joke about office life, one line under 200 characters,
to /output/entry.txt, where the make.fun judge reads it.
"""

from pathlib import Path

JOKE = "The only meeting everyone attends on time is the fire drill — it's the only one with an exit plan."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
