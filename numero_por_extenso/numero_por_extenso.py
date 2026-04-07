# Projeto Número por extenso
cont = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    print('=' * 33)
    num = int(input('Digite um número entre 0 e 20: '))
    
    # 🔁 este loop só termina quando o número for válido
    while num < 0 or num > 20:
        num = int(input('Número inválido! Tente novamente: '))
    
    print(f'Você digitou {cont[num]}')
    
    resp = input('Você quer continuar [S/N]? ').upper().strip()
    if resp == 'N':
        break
print('FIM DO PROGRAMA! ')