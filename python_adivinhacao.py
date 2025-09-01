while True:
    if opcao == '4':
        break
        while True:
    tentativa = input(f"Tentativa {tentativa_atual}/{max_tentativas}: ")
    
    if tentativa.strip() == "":
        print("❌ Valor vazio. Digite um número!")
        continue
    
    if not tentativa.isdigit():
        print("❌ Valor inválido. Digite apenas números!")
        continue
        
        if palpite == numero_secreto:
    print(f"🎉 Parabéns! Você acertou em {tentativa_atual} tentativas!")
    break

elif palpite < numero_secreto:
    print("🔍 Dica: Tente um número MAIOR!")
else:
    print("🔍 Dica: Tente um número MENOR!")
    
    if palpite < 1 or palpite > 100:
    print("❌ O número deve estar entre 1 e 100!")
    continue