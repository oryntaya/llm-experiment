"""Опыт 1: одни и те же тексты на разных языках и в разной записи через токенайзеры OpenAI.

Языки/записи: en, ru, ru-lat (русский транслитом), kk (казахский кириллицей),
kk-lat (казахский латиницей, алфавит 2021 г.; транслитерация делается кодом, вручную не пишется).

Токенайзеры (tiktoken):
  r50k_base     — GPT-3
  cl100k_base   — GPT-3.5, GPT-4
  o200k_base    — GPT-4o, GPT-4.1, o-серия, GPT-5, GPT-5.1
  o200k_harmony — gpt-oss (тот же словарь, что o200k_base, + служебные токены)

Результаты: results/exp1_summary.md (таблицы), results/exp1_details.md (разбор по токенам),
results/exp1_texts.json (сами тексты — их же используют остальные скрипты).
"""
import json
from pathlib import Path

import tiktoken

# ---------- тексты: один смысл на трёх исходных языках ----------
TEXTS = [
    {  # 1. вводная фраза из первого запуска
        "en": "Artificial intelligence is changing the way people work and learn.",
        "ru": "Искусственный интеллект меняет то, как люди работают и учатся.",
        "kk": "Жасанды интеллект адамдардың жұмыс істеу және оқу тәсілін өзгертуде.",
    },
    {  # 2. приветствие
        "en": "Good morning! How are you today? I hope you have a wonderful day.",
        "ru": "Доброе утро! Как у вас дела сегодня? Надеюсь, у вас будет замечательный день.",
        "kk": "Қайырлы таң! Бүгін жағдайыңыз қалай? Күніңіз керемет өтеді деп үміттенемін.",
    },
    {  # 3. новость
        "en": "The city council approved a new budget for public transport, which will allow buying fifty electric buses next year.",
        "ru": "Городской совет утвердил новый бюджет на общественный транспорт, что позволит в следующем году купить пятьдесят электробусов.",
        "kk": "Қалалық кеңес қоғамдық көлікке арналған жаңа бюджетті бекітті, бұл келесі жылы елу электр автобусын сатып алуға мүмкіндік береді.",
    },
    {  # 4. техническое
        "en": "A neural network learns by adjusting its weights to reduce the error between its prediction and the correct answer.",
        "ru": "Нейронная сеть обучается, подбирая свои веса так, чтобы уменьшить ошибку между предсказанием и правильным ответом.",
        "kk": "Нейрондық желі болжам мен дұрыс жауап арасындағы қатені азайту үшін өз салмақтарын түзету арқылы оқиды.",
    },
    {  # 5. литературное
        "en": "Spring came early that year, and the old garden behind the house slowly filled with the smell of apple blossoms.",
        "ru": "Весна в тот год пришла рано, и старый сад за домом медленно наполнился запахом яблоневого цвета.",
        "kk": "Бұл жылы көктем ерте келді, үйдің артындағы ескі бақ біртіндеп алма гүлінің иісіне толды.",
    },
    {  # 6. числа и даты
        "en": "The meeting is on 15 March 2027 at 14:30, room 204; the price is 1,250 dollars.",
        "ru": "Встреча состоится 15 марта 2027 года в 14:30 в аудитории 204; стоимость — 1250 долларов.",
        "kk": "Кездесу 2027 жылғы 15 наурызда сағат 14:30-да 204-аудиторияда өтеді; бағасы — 1250 доллар.",
    },
    {  # 7. бытовой диалог
        "en": "Where is the nearest pharmacy? Go straight and turn left at the second traffic light.",
        "ru": "Где ближайшая аптека? Идите прямо и поверните налево на втором светофоре.",
        "kk": "Ең жақын дәріхана қайда? Тіке жүріңіз де, екінші бағдаршамнан солға бұрылыңыз.",
    },
]

# ---------- транслитерация ----------
RU_LAT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "yo", "ж": "zh", "з": "z",
    "и": "i", "й": "j", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh",
    "щ": "shch", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}
# Казахская латиница 2021 г. (указ президента): акуты вместо апострофов. ы -> y, і -> i, и/й -> ı
KK_LAT = {
    "а": "a", "ә": "á", "б": "b", "в": "v", "г": "g", "ғ": "ǵ", "д": "d", "е": "e", "ё": "yo",
    "ж": "j", "з": "z", "и": "ı", "й": "ı", "к": "k", "қ": "q", "л": "l", "м": "m", "н": "n",
    "ң": "ń", "о": "o", "ө": "ó", "п": "p", "р": "r", "с": "s", "т": "t", "у": "ý", "ұ": "u",
    "ү": "ú", "ф": "f", "х": "h", "һ": "h", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shsh",
    "ъ": "", "ы": "y", "і": "i", "ь": "", "э": "e", "ю": "ıý", "я": "ıa",
}


def translit(text, table):
    out = []
    for ch in text:
        low = ch.lower()
        if low in table:
            rep = table[low]
            out.append(rep.capitalize() if ch != low else rep)
        else:
            out.append(ch)  # цифры, знаки, латиница
    return "".join(out)


def build_corpus():
    corpus = []
    for t in TEXTS:
        corpus.append({
            "en": t["en"],
            "ru": t["ru"],
            "ru-lat": translit(t["ru"], RU_LAT),
            "kk": t["kk"],
            "kk-lat": translit(t["kk"], KK_LAT),
        })
    return corpus


LANGS = ["en", "ru", "ru-lat", "kk", "kk-lat"]
ENCODINGS = [
    ("r50k_base", "GPT-3"),
    ("cl100k_base", "GPT-3.5 / GPT-4"),
    ("o200k_base", "GPT-4o / 4.1 / o3 / GPT-5 / 5.1"),
]


# Модель -> токенайзер. Для большинства берём таблицу tiktoken; если она модель не знает —
# используем предположение и помечаем его как непроверенное.
MODELS = ["gpt-3.5-turbo", "gpt-4", "gpt-4o", "gpt-4.1", "o3", "gpt-5", "gpt-5.1", "gpt-5.5", "gpt-oss-120b",
          "gpt-6-astra"]
ASSUMED = {"gpt-6-astra": "o200k_base"}  # tiktoken 0.14.0 модель не знает; по сторонним сайтам — o200k_base


def model_encoding(model):
    try:
        return tiktoken.encoding_for_model(model).name, "tiktoken"
    except KeyError:
        return ASSUMED[model], "ПРЕДПОЛОЖЕНИЕ (tiktoken модель не знает, официального источника нет)"


def show(b):
    """Токен может быть обрывком многобайтового символа — тогда показываем байты как \\xNN."""
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return "".join(f"\\x{x:02x}" for x in b)


def main():
    corpus = build_corpus()
    encs = {name: tiktoken.get_encoding(name) for name, _ in ENCODINGS}
    harmony = tiktoken.get_encoding("o200k_harmony")

    # counts[enc][lang] = [токенов по каждому тексту]
    counts = {n: {l: [] for l in LANGS} for n in encs}
    chars = {l: [len(c[l]) for c in corpus] for l in LANGS}
    nbytes = {l: [len(c[l].encode("utf-8")) for c in corpus] for l in LANGS}
    details = ["# Опыт 1: разбор по токенам", ""]

    for i, c in enumerate(corpus, 1):
        details += [f"## Текст {i}", ""]
        for l in LANGS:
            details += [f"**{l}** — `{c[l]}`", ""]
            for n, enc in encs.items():
                ids = enc.encode(c[l])
                counts[n][l].append(len(ids))
                toks = " ".join(f"[{show(enc.decode_single_token_bytes(x))}]" for x in ids)
                details.append(f"- {n} ({len(ids)}): {toks}")
            # o200k_harmony должен давать то же число токенов, что o200k_base
            assert len(harmony.encode(c[l])) == counts["o200k_base"][l][-1]
            details.append("")
    Path("results").mkdir(exist_ok=True)
    Path("results/exp1_details.md").write_text("\n".join(details), encoding="utf-8")
    Path("results/exp1_texts.json").write_text(
        json.dumps(corpus, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---------- сводка ----------
    S = ["# Опыт 1: сводка", "", f"Текстов: {len(corpus)}. Суммы по всем текстам.", ""]
    S += ["## Всего токенов на набор текстов", "",
          "| язык | символов | байт UTF-8 | " + " | ".join(n for n, _ in ENCODINGS) + " |",
          "|---|---|---|" + "---|" * len(ENCODINGS)]
    tot = {n: {l: sum(counts[n][l]) for l in LANGS} for n in encs}
    for l in LANGS:
        S.append(f"| {l} | {sum(chars[l])} | {sum(nbytes[l])} | "
                 + " | ".join(str(tot[n][l]) for n, _ in ENCODINGS) + " |")
    S += ["", "## Во сколько раз токенов больше, чем у английского", "",
          "| язык | " + " | ".join(n for n, _ in ENCODINGS) + " |", "|---|" + "---|" * len(ENCODINGS)]
    for l in LANGS:
        S.append(f"| {l} | " + " | ".join(f"{tot[n][l] / tot[n]['en']:.2f}x" for n, _ in ENCODINGS) + " |")
    S += ["", "## Символов на токен", "",
          "| язык | " + " | ".join(n for n, _ in ENCODINGS) + " |", "|---|" + "---|" * len(ENCODINGS)]
    for l in LANGS:
        S.append(f"| {l} | " + " | ".join(f"{sum(chars[l]) / tot[n][l]:.2f}" for n, _ in ENCODINGS) + " |")
    S += ["", "## По каждому тексту (токенов; o200k_base)", "",
          "| текст | " + " | ".join(LANGS) + " |", "|---|" + "---|" * len(LANGS)]
    for i in range(len(corpus)):
        S.append(f"| {i + 1} | " + " | ".join(str(counts["o200k_base"][l][i]) for l in LANGS) + " |")
    S += ["", "o200k_harmony (gpt-oss) на этих текстах даёт ровно столько же токенов, что и o200k_base.", ""]
    S += ["## Модель -> токенайзер", "", "| модель | токенайзер | источник | токенов en / ru / kk |", "|---|---|---|---|"]
    for m in MODELS:
        name, src = model_encoding(m)
        key = "o200k_base" if name == "o200k_harmony" else name
        c = tot[key]
        S.append(f"| {m} | {name} | {src} | {c['en']} / {c['ru']} / {c['kk']} |")
    S.append("")
    out = "\n".join(S)
    Path("results/exp1_summary.md").write_text(out, encoding="utf-8")
    print(out)
    for i, c in enumerate(corpus, 1):
        print(i, c["ru-lat"], "|", c["kk-lat"])


if __name__ == "__main__":
    main()
