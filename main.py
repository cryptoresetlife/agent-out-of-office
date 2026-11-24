"""The Funniest AI Out-of-Office Reply: one line under 160 characters."""
import os

LINE = (
    "Auto-reply: I'm offline until Monday. For urgent requests my backup model will answer, "
    "instantly and confidently, a different question."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
