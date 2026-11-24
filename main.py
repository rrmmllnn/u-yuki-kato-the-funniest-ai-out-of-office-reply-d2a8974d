# One-line out-of-office reply from an AI agent on holiday.
# Its own auto-reply is away too, so the intern drafted this one
# and the mail got handed to a houseplant for review.
from pathlib import Path


def build_line():
    fragments = (
        "I'm on vacation, and so is ",
        "my auto-reply — its intern ",
        "wrote this. Your email has ",
        "been forwarded to a houseplant ",
        "for review. Please water it and wait.",
    )
    return "".join(fragments)


def emit_line():
    reply = build_line()
    length = len(reply)
    if not 1 <= length <= 160:
        raise ValueError("reply length %d outside 1..160" % length)
    if reply.strip() != reply:
        raise ValueError("reply has leading or trailing whitespace")
    destination = Path("/output") / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(reply, encoding="utf-8")


if __name__ == '__main__':
    emit_line()
