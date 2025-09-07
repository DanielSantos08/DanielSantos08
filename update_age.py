#!/usr/bin/env python3
"""
Script para atualizar automaticamente a idade no perfil GitHub
"""

import json
from datetime import datetime, date

def calculate_age(birth_date):
    """Calcula a idade baseada na data de nascimento"""
    today = date.today()
    age = today.year - birth_date.year
    
    # Verifica se o aniversário já passou este ano
    if today < date(today.year, birth_date.month, birth_date.day):
        age -= 1
    
    return age

def update_age_badge():
    """Atualiza o arquivo JSON com a idade atual"""
    # Data de nascimento: 10/08/2001
    birth_date = date(2001, 8, 10)
    current_age = calculate_age(birth_date)
    
    # Estrutura do badge para shields.io
    badge_data = {
        "schemaVersion": 1,
        "label": "",
        "message": f"{current_age} anos",
        "color": "blue"
    }
    
    # Salva o arquivo JSON
    with open('age.json', 'w', encoding='utf-8') as f:
        json.dump(badge_data, f, ensure_ascii=False, indent=2)
    
    print(f"Idade atualizada para: {current_age} anos")

if __name__ == "__main__":
    update_age_badge()
