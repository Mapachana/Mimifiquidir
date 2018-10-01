"""
@file algorithm.py
@author Jose 
@brief implementación del algoritmo del mimifiquidir, 
Mimificar una cadena de caracteres consiste en cambiar de manera conveniente las vocales y ciertas consonantes por ies, dándole un toquecillo sarcástico y desenfadado al mensaje con el fin de chincar al usuario al queu se le responde. 
con una eficiencia O(n^2).
"""
silabas_especiales =    (
                        (('que', 'qui', 'ca', 'co', 'cu'), '$1$',  'qui'),
                        (('Que', 'Qui', 'Ca', 'Co', 'Cu'), '$1^$', 'Qui'),
                        (('QUE', 'QUI', 'CA', 'CO', 'CU'), '$1^^$', 'QUI'),
                        (('qué', 'quí', 'cá', 'có', 'cú'), '$1´$', 'quí'),
                        (('Qué', 'Quí', 'Cá', 'Có', 'Cú'), '$1^´$', 'Quí'),
                        (('QUÉ', 'QUÍ', 'CÁ', 'CÓ', 'CÚ'), '$1^^´$', 'QUÍ'),
                        (('gue', 'gui', 'ga', 'go', 'gu'), '$2$', 'gui'),
                        (('Gue', 'Gui', 'Ga', 'Go', 'Gu'), '$2^$', 'Gui'),
                        (('GUE', 'GUI', 'GA', 'GO', 'GU'), '$2^^$', 'GUI'),
                        (('gué', 'guí', 'gá', 'gó', 'gú'), '$2´$', 'guí'),
                        (('Gué', 'Guí', 'Gá', 'Gó', 'Gú'), '$2^´$', 'Guí'),
                        (('GUÉ', 'GUÍ', 'GÁ', 'GÓ', 'GÚ'), '$2^^´$', 'GUÍ'),
                        (('güe', 'güi'), '$2¨$', 'güi'),
                        (('Güe', 'Güi'), '$2^¨$', 'Güi'),
                        (('GÜE', 'GÜI'), '$2^^¨$', 'GÜI'),
                        (('güé', 'güí'), '$2¨´$', 'güí'),
                        (('Güé', 'Güí'), '$2^¨´$', 'Güí'),
                        (('GÜÉ', 'GÜÍ'), '$2^^¨´$', 'GÚÍ')
                        )

vocales = (('aeou', 'i'), ('áéóú', 'í'), ('AEOU', 'I'), ('ÁÉÓÚ', 'Í'))

def mimifica(mensaje: str):
    '''Devuelve mensaje mimificado'''
    
    # Codificación de sílabas especiales:
    for grupo in silabas_especiales:
        for silaba in grupo[0]:
            mensaje = mensaje.replace(silaba, grupo[1])

    # Cambiar todas las vocales por i:
    for grupo in vocales:
        for vocal in grupo[0]:
            mensaje = mensaje.replace(vocal, grupo[1])

    # Decodificación de sílabas especiales, esta vez con la i como única vocal:
    for grupo in silabas_especiales:
        mensaje = mensaje.replace(grupo[1], grupo[2])

    return mensaje
