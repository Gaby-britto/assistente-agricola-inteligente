import csv
import random

with open("dados_agricolas.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["umidade", "pH", "temperatura", "irrigacao", "fertilizante", "produtividade"])
    
    for _ in range(100):
        umidade = random.randint(20, 60)
        ph = round(random.uniform(5.5, 7.5), 2)
        temperatura = random.randint(20, 35)
        irrigacao = random.randint(5, 20)
        fertilizante = random.randint(2, 10)
        
        produtividade = (umidade * 0.5 + irrigacao * 2 + fertilizante * 1.5) - abs(ph - 6.5) * 5
        
        writer.writerow([umidade, ph, temperatura, irrigacao, fertilizante, round(produtividade, 2)])
