"""Опыт 1б: точный подсчёт токенов Claude через API (endpoint count_tokens).

Нужен ключ: export ANTHROPIC_API_KEY=...   и   pip install anthropic
Запуск:     .venv/bin/python exp1b_claude_count.py [model ...]
Тексты берутся из results/exp1_texts.json (их создаёт exp1_tokenizer.py).
Результат:  results/exp1b_claude.md

count_tokens возвращает токены всего запроса, включая служебные. Чтобы получить токены самого
текста, из каждого результата вычитается результат для минимального сообщения "."
"""
import json
import sys
from pathlib import Path

import anthropic

MODELS = ["claude-sonnet-5-5", "claude-opus-5-5", "claude-haiku-5-5"]
LANGS = ["en", "ru", "ru-lat", "kk", "kk-lat"]


def count(client, model, text):
    r = client.messages.count_tokens(model=model, messages=[{"role": "user", "content": text}])
    return r.input_tokens


def main():
    models = sys.argv[1:] or MODELS
    corpus = json.loads(Path("results/exp1_texts.json").read_text(encoding="utf-8"))
    client = anthropic.Anthropic()
    lines = ["# Опыт 1б: токены Claude (count_tokens)", "", f"Текстов: {len(corpus)}", ""]
    lines += ["| модель | " + " | ".join(LANGS) + " |", "|---|" + "---|" * len(LANGS)]
    ratios = []
    for model in models:
        base = count(client, model, ".")
        tot = {l: sum(count(client, model, c[l]) - base for c in corpus) for l in LANGS}
        lines.append(f"| {model} | " + " | ".join(str(tot[l]) for l in LANGS) + " |")
        ratios.append((model, tot))
    lines += ["", "Во сколько раз больше, чем у английского:", "",
              "| модель | " + " | ".join(LANGS) + " |", "|---|" + "---|" * len(LANGS)]
    for model, tot in ratios:
        lines.append(f"| {model} | " + " | ".join(f"{tot[l] / tot['en']:.2f}x" for l in LANGS) + " |")
    out = "\n".join(lines) + "\n"
    Path("results/exp1b_claude.md").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
