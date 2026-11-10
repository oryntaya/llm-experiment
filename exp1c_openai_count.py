"""Опыт 1в: тот же первый опыт (токены EN/RU/RU-lat/KK/KK-lat), но на реальной модели через API OpenAI.

По умолчанию модель gpt-6-astra. Токены берутся из usage.input_tokens ответа Responses API
(запрос с max_output_tokens=16, то есть стоит копейки). Служебные токены запроса вычитаются:
из каждого результата вычитается результат для минимального сообщения ".".
Рядом печатается счёт tiktoken o200k_base — так видно, верно ли предположение о токенайзере.

Нужен ключ: export OPENAI_API_KEY=...   и   pip install openai
Запуск:     .venv/bin/python exp1c_openai_count.py [model ...]
Тексты:     results/exp1_texts.json (создаёт exp1_tokenizer.py)
Результат:  results/exp1c_openai.md
"""
import json
import sys
from pathlib import Path

import tiktoken
from openai import OpenAI

MODELS = ["gpt-6-astra"]
LANGS = ["en", "ru", "ru-lat", "kk", "kk-lat"]


def count(client, model, text):
    r = client.responses.create(model=model, input=text, max_output_tokens=16)
    return r.usage.input_tokens


def main():
    models = sys.argv[1:] or MODELS
    corpus = json.loads(Path("results/exp1_texts.json").read_text(encoding="utf-8"))
    client = OpenAI()
    enc = tiktoken.get_encoding("o200k_base")
    ref = {l: sum(len(enc.encode(c[l])) for c in corpus) for l in LANGS}

    lines = ["# Опыт 1в: токены через API OpenAI", "", f"Текстов: {len(corpus)}. Суммы по всем текстам.", "",
             "| модель | " + " | ".join(LANGS) + " |", "|---|" + "---|" * len(LANGS)]
    rows = []
    for model in models:
        base = count(client, model, ".")
        tot = {l: sum(count(client, model, c[l]) - base for c in corpus) for l in LANGS}
        rows.append((model, tot))
        lines.append(f"| {model} | " + " | ".join(str(tot[l]) for l in LANGS) + " |")
    lines.append("| tiktoken o200k_base | " + " | ".join(str(ref[l]) for l in LANGS) + " |")
    lines += ["", "Во сколько раз больше, чем у английского:", "",
              "| модель | " + " | ".join(LANGS) + " |", "|---|" + "---|" * len(LANGS)]
    for model, tot in rows:
        lines.append(f"| {model} | " + " | ".join(f"{tot[l] / tot['en']:.2f}x" for l in LANGS) + " |")
    lines.append("| tiktoken o200k_base | " + " | ".join(f"{ref[l] / ref['en']:.2f}x" for l in LANGS) + " |")
    lines += ["", "Если строки модели и o200k_base совпадают (с точностью до пары токенов), "
              "предположение о токенайзере верно."]
    out = "\n".join(lines) + "\n"
    Path("results/exp1c_openai.md").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
