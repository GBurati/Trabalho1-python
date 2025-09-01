# Trabalho1-python 
Este é um jogo interativo de adivinhação onde o jogador tenta descobrir um número secreto dentro de um limite de tentativas. O programa oferece três níveis de dificuldade e fornece dicas ao jogador durante as tentativas.
 Como executar
Certifique-se de ter Python instalado (versão 3.6 ou superior)

Salve o código em um arquivo com extensão .py (ex: adivinhacao.py)

Como jogar
Escolha um dos três níveis de dificuldade

Tente adivinhar o número secreto dentro do limite de tentativas

Use as dicas fornecidas pelo programa

Vença acertando o número ou tente novamente se esgotar as tentativas
Estruturas do código explicadas
1. Loop while para o menu principal
python
while True:
    # Menu de seleção de dificuldade
    # ...
    if opcao == '4':
        break  # Sai do loop e encerra o programa
Usei um loop while True para manter o programa em execução até que o usuário escolha a opção de sair. O break é utilizado para interromper o loop quando o usuário seleciona a opção de saída.

2. Validação de entrada do usuário
python
while True:
    tentativa = input(f"Tentativa {tentativa_atual}/{max_tentativas}: ")
    
    if tentativa.strip() == "":
        print("❌ Valor vazio. Digite um número!")
        continue
    
    if not tentativa.isdigit():
        print("❌ Valor inválido. Digite apenas números!")
        continue
Utilizo continue para retornar ao início do loop quando a entrada é inválida (vazia ou não numérica), solicitando novamente uma entrada válida.

3. Condicionais para controle de fluxo
python
if palpite == numero_secreto:
    print(f"🎉 Parabéns! Você acertou em {tentativa_atual} tentativas!")
    break
elif palpite < numero_secreto:
    print("🔍 Dica: Tente um número MAIOR!")
else:
    print("🔍 Dica: Tente um número MENOR!")
Uso if, elif e else para comparar o palpite do usuário com o número secreto e fornecer dicas adequadas. O break interrompe o loop quando o usuário acerta.

4. Loop for para limitar tentativas
python
for tentativa_atual in range(1, max_tentativas + 1):
    # Lógica das tentativas
Utilizo um loop for com range() para controlar o número máximo de tentativas permitidas em cada nível de dificuldade.

5. Validação de faixa de valores
python
if palpite < 1 or palpite > 100:
    print("❌ O número deve estar entre 1 e 100!")
    continue
Verifico se o palpite está dentro da faixa válida (1-100) e uso continue para solicitar uma nova tentativa caso esteja fora do intervalo.

📊 Níveis de dificuldade
Fácil: 10 tentativas, números de 1 a 50

Médio: 7 tentativas, números de 1 a 100

Difícil: 5 tentativas, números de 1 a 150

