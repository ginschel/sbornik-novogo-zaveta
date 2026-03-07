import re

# ============================================================
# Preprocess special letters
# ============================================================

_PREPROCESS_MAP = {
    'Ę': 'e', 'ę': 'e',
    'Ų': 'u', 'ų': 'u',
    'Å': 'a', 'å': 'a',
    'Ė': 'e', 'ė': 'e',
    'Ȯ': 'o', 'ȯ': 'o',
    'Ć': 'č', 'ć': 'č',
    'Đ': 'dž', 'đ': 'dž',
    'Ĺ': 'l', 'ĺ': 'l',
    'Ń': 'n', 'ń': 'n',
    'Ŕ': 'r', 'ŕ': 'r',
    'T́': 't', 't́': 't',
    'D́': 'd', 'd́': 'd',
    'Ś': 's', 'ś': 's',
    'Ź': 'z', 'ź': 'z'
}


def _preprocess(text: str) -> str:
    for k, v in _PREPROCESS_MAP.items():
        text = text.replace(k, v)
    return text


# ============================================================
# Replacement tables
# ============================================================

_STD_CYR = {
    'a':'а','b':'б','c':'ц','č':'ч','d':'д','dž':'дж','e':'е','ě':'є','f':'ф',
    'g':'г','h':'х','i':'и','j':'ј','k':'к','l':'л','lj':'љ','m':'м','n':'н',
    'nj':'њ','o':'о','p':'п','r':'р','s':'с','š':'ш','t':'т','u':'у','v':'в',
    'y':'ы','z':'з','ž':'ж','ja':'ја','ju':'ју','je':'је','jo':'јо'
}

_TRAD_CYR = {
    'a':'а','b':'б','c':'ц','č':'ч','d':'д','dž':'дж','e':'е','ě':'ѣ','f':'ф',
    'g':'г','h':'х','i':'и','j':'й','k':'к','l':'л','lj':'ль','m':'м','n':'н',
    'nj':'нь','o':'о','p':'п','r':'р','s':'с','š':'ш','t':'т','u':'у','v':'в',
    'y':'ы','z':'з','ž':'ж','ja':'ꙗ','ju':'ю','je':'ѥ'
}

_GLA = {
    'a':'ⰰ','b':'ⰱ','c':'ⱌ','č':'ⱍ','d':'ⰴ','dž':'ⰴⰶ','e':'ⰵ','ě':'ⱑ','f':'ⱇ',
    'g':'ⰳ','h':'ⱈ','i':'ⰻ','j':'ⰹ','k':'ⰽ','l':'ⰾ','lj':'ⰾⱐ','m':'ⰿ','n':'ⱀ',
    'nj':'ⱀⱐ','o':'ⱁ','p':'ⱂ','r':'ⱃ','s':'ⱄ','š':'ⱎ','t':'ⱅ','u':'ⱆ','v':'ⰲ',
    'y':'ⱏⰹ','z':'ⰸ','ž':'ⰶ','ja':'ⰹⰰ','ju':'ⱓ','je':'ⰹⰵ','jo':'ⱖ',
    '.':' ⁙', ',':'·'
}


# ============================================================
# Helper: preserve capitalization
# ============================================================

def _preserve_case(original: str, replacement: str) -> str:
    result = ''
    for o, r in zip(original, replacement):
        result += r.upper() if o.isupper() else r
    if len(replacement) > len(original):
        result += replacement[len(original):]
    return result


# ============================================================
# Core word transliteration engine
# ============================================================

def _transliterate_word(word: str, table: dict) -> str:
    i = 0
    result = ''
    while i < len(word):
        pair = word[i:i+2]
        pair_lower = pair.lower()

        if pair_lower in table:
            result += _preserve_case(pair, table[pair_lower])
            i += 2
            continue

        single = word[i]
        lower = single.lower()

        if lower in table:
            result += _preserve_case(single, table[lower])
        else:
            result += single

        i += 1

    return result


def _transliterate_word_traditional(word: str) -> str:
    # Phase 1
    word = _transliterate_phase(word, ['ja','ju','je','dž'])
    # Phase 2
    word = _transliterate_phase(word, ['lj','nj'])
    # Phase 3
    word = _transliterate_phase(word, list(_TRAD_CYR.keys()))
    return word


def _transliterate_phase(word: str, keys: list) -> str:
    i = 0
    result = ''
    while i < len(word):
        pair = word[i:i+2]
        pair_lower = pair.lower()

        if pair_lower in keys:
            result += _preserve_case(pair, _TRAD_CYR[pair_lower])
            i += 2
            continue

        single = word[i]
        lower = single.lower()

        if lower in keys:
            result += _preserve_case(single, _TRAD_CYR[lower])
        else:
            result += single

        i += 1

    return result


# ============================================================
# Sentence-level API functions
# ============================================================

def latin_to_stdCyrillic(text: str) -> str:
    text = _preprocess(text)
    tokens = re.findall(r'\w+|\W+', text)
    return ''.join(
        _transliterate_word(tok, _STD_CYR) if tok.isalpha() else tok
        for tok in tokens
    )


def latin_to_tradCyrillic(text: str) -> str:
    text = _preprocess(text)
    tokens = re.findall(r'\w+|\W+', text)
    return ''.join(
        _transliterate_word_traditional(tok) if tok.isalpha() else tok
        for tok in tokens
    )


def latin_to_glagolitic(text: str) -> str:
    text = _preprocess(text)
    tokens = re.findall(r'\w+|\W+', text)
    return ''.join(
        _transliterate_word(tok, _GLA) if tok.isalpha() else tok
        for tok in tokens
    )