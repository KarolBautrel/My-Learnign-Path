import time
source = "reportLine += 1 "

reportLine = 0

start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start

start = time.time()
# compile(co kompilujemy, plik z ktorego tekst jest preczytany, tryb(exec,eval,simple=pojedyncza instrukca))
sourceCompiled = compile(source, "internal variable source", 'exec')
for i in range(100000):
    exec(sourceCompiled)
stop = time.time()
time_compiled = stop - start

print(time_not_compiled)
print(time_compiled)  # Compile jest duzo szybszy

print(reportLine)  # teraz wartosc bedzie dwa, poniewaz dwa razy wykonalismy funkcje exec na zmiennej. Raz normalnie, a drugi raz za pomoca compile
