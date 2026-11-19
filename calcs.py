import random

from triggers import *

from datetime import datetime, timezone

LISTONA = SIX_SEVEN_TRIGGERS + RESENHA_TRIGGERS + CEMPILA_TRIGGERS + DEVAGAR_TRIGGERS + JE_TRIGGERS + LARP_TRIGGERS + ENTROSA_TRIGGERS

LISTONA_MAX = (RESENHA_TRIGGERS + CEMPILA_TRIGGERS + DEVAGAR_TRIGGERS + JE_TRIGGERS + LARP_TRIGGERS + ENTROSA_TRIGGERS) * 100

def calc_resenha(item):
    numeros_resenhas = [67, 41, 505, 13, 22, 14, 24, 69]

    if type(item) == int:
        if item in numeros_resenhas:
            return ":white_check_mark::white_check_mark: MT RESENHA 100/10"
        else:
            return ":x::x: VERGONHOSO, NÃO É RESENHA"

    elif type(item) == str:
        if len(item) in numeros_resenhas:
            return f":white_check_mark: TEM {len(item)} LETRAS"
        else:
            for word in item.split():
                if word.lower() in LISTONA:
                    return f":white_check_mark: EU OUVI {word}????"

            for word in item.split():
                try:
                    if int(word) in numeros_resenhas:
                        return f":white_check_mark: {word} É MT É RESENHA"
                finally:
                    return f":x::x: NENHUMA RESENHA DETECTADA"

def calc_today_resenha():
    resenha = []

    hoje = datetime.now(timezone.utc)

    resenha.append(LISTONA_MAX[hoje.month * int(str(hoje.year)[:2])])
    resenha.append(LISTONA_MAX[int(str(hoje.year)[:2])])
    resenha.append(LISTONA_MAX[hoje.day * int(str(hoje.year)[2:])])
    resenha.append(LISTONA_MAX[int(str(hoje.year)[2:])])

    return " ".join(resenha)

def calc_aura(pessoa):
    aura = 0

    if len(str(pessoa.name)) > 10:
        aura -= 50 * (len(str(pessoa.name)) - 10)
    else:
        aura += 50 * (10 // len(str(pessoa.name)))

    for letter in pessoa.name:
        if letter.isalpha():
            aura += 50
        else:
            aura -= 10

    return aura