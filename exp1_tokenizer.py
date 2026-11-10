"""Опыт 1: одна и та же фраза на русском и английском через токенайзер.

Токенайзеры (tiktoken, OpenAI): cl100k_base (GPT-4) и o200k_base (GPT-4o).
Результат печатается в консоль и сохраняется в results/exp1_tokenizer.md
"""
from pathlib import Path

import tiktoken

PHRASES = {
    "en": "Artificial intelligence is changing the way people work and learn.",
    "ru": "Искусственный интеллект меняет то, как люди работают и учатся.",
}
ENCODINGS = ["cl100k_base", "o200k_base"]


def pieces(enc, text):
    ids = enc.encode(text)
    return ids, [enc.decode_single_token_bytes(i).decode("utf-8", errors="replace") for i in ids]


def main():
    lines = ["# Опыт 1: токенизация одной фразы на EN и RU", ""]
    summary = []
    for enc_name in ENCODINGS:
        enc = tiktoken.get_encoding(enc_name)
        lines += [f"## {enc_name}", ""]
        for lang, text in PHRASES.items():
            ids, toks = pieces(enc, text)
            chars = len(text)
            n_bytes = len(text.encode("utf-8"))
            lines += [
                f"**{lang}**: `{text}`",
                "",
                f"- символов: {chars}, байт UTF-8: {n_bytes}, токенов: **{len(ids)}**",
                f"- символов на токен: {chars / len(ids):.2f}",
                f"- токены: " + " ".join(f"[{t}]" for t in toks),
                f"- id: {ids}",
                "",
            ]
            summary.append((enc_name, lang, chars, len(ids)))

    lines += ["## Сводка", "", "| токенайзер | язык | символов | токенов | симв./токен |", "|---|---|---|---|---|"]
    for enc_name, lang, chars, n in summary:
        lines.append(f"| {enc_name} | {lang} | {chars} | {n} | {chars / n:.2f} |")
    lines.append("")
    for enc_name in ENCODINGS:
        en = next(n for e, l, c, n in summary if e == enc_name and l == "en")
        ru = next(n for e, l, c, n in summary if e == enc_name and l == "ru")
        lines.append(f"- {enc_name}: RU / EN = {ru / en:.2f}x токенов")
    lines.append("")

    out = "\n".join(lines)
    print(out)
    Path("results").mkdir(exist_ok=True)
    Path("results/exp1_tokenizer.md").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()
