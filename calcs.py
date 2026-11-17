from triggers import *

LISTONA = SIX_SEVEN_TRIGGERS + RESENHA_TRIGGERS + CEMPILA_TRIGGERS + DEVAGAR_TRIGGERS + JE_TRIGGERS + LARP_TRIGGERS + ENTROSA_TRIGGERS

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