# llm-experiment

Небольшие опыты с токенами и LLM.

## Запуск

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python exp1_tokenizer.py
```

## Опыты

### 1. Токенизация одной фразы на EN и RU
Скрипт: `exp1_tokenizer.py`, результат: `results/exp1_tokenizer.md`.

| токенайзер | язык | символов | токенов | симв./токен |
|---|---|---|---|---|
| cl100k_base (GPT-4) | en | 66 | 12 | 5.50 |
| cl100k_base (GPT-4) | ru | 62 | 30 | 2.07 |
| o200k_base (GPT-4o) | en | 66 | 11 | 6.00 |
| o200k_base (GPT-4o) | ru | 62 | 16 | 3.88 |

Вывод: на старом токенайзере русская фраза стоит в 2.5 раза больше токенов, чем английская, на новом — в 1.45 раза. Токенайзеры OpenAI, не Claude: у Claude разбиение другое.
