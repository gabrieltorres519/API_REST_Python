from cupshelpers import Printer


numTabla = int(input("Ingrese el número para ver su tabla de multiplicar: "));
hastaDonde = int(input(f"Hasta dónde desea calcular la tabla del {numTabla}?: "));

numMult = 1;

print("Con for: \n");
for i in range(hastaDonde):
    print(f"{numTabla} x {numMult+i} = {numTabla*(i+1)}");


print("\n Con While: \n");
counter = 0;
while counter < hastaDonde:
    counter+=1;
    print(f"{numTabla} x {counter} = {numTabla*counter}");


