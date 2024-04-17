def fib(final):
        atual=1
        anterior=0
        prox_numero= atual+anterior
        print(anterior)
        print(atual)
        while(prox_numero<=final):
            anterior=atual
            atual=prox_numero
            prox_numero=atual+anterior
            print(prox_numero)
            
final= int(input("digite o numero maximo da sequencia "))
fib(final)
