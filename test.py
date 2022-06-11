from juego import anillo
import csv

if __name__ == '__main__':

    intervalo = 0.003
    mu = []
    b = 10
    for k in range(5):
        fo = open(f"resultados_{k+1}.csv", "w", encoding = "utf-8", newline="")
        header = ['intentos', 'probabilidad']
        writer = csv.DictWriter(fo, fieldnames=header)
        writer.writeheader()
        intentos = []
        probabilidades = []
        j = 2
        while True:
            j += 1
            match = 0
            for i in range(b**j):
                if(anillo()):
                    match += 1
            probabilidades.append(round((match/(b**j)*100),2))
            intentos.append(b**j)
            print(match, "/", b**j)
            writer.writerow({"intentos":intentos[-1], "probabilidad":probabilidades[-1]})
            if len(probabilidades) > 1:
                if 1-intervalo < probabilidades[-1] / probabilidades[-2] < 1+intervalo:
                    mu.append(probabilidades[-1])
                    fo.close()
                    break
    mur = sum(mu)/len(mu)
    print("probabilidad de ganar el juego es", mur, "+-", round(mur-(mur*(1-intervalo)),4))