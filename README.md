# Laboratorio 9
Gli obiettivi principali di questo laboratorio sono:
- *args e **kwargs
- classi astratte (ABC)
- second order functions e decorators

Gli ultimi esercizi riguardano la ricorsione e la rappresentazione di grafi.

## Esercizio 1
Sviluppare la classe astratta *Shape* che eredita da *ABC*, rappresentante una figura geometrica.
Il costruttore accetta come unico parametro il nome che si vuole associare alla figura.
(ad es., "figura1", "la mia forma", etc...)
Il nome deve essere ottenibile tramite opportuno getter.
La classe possiede due metodi astratti che restituiscono, rispettivamente, il perimetro e l'area della figura.

La classe *Triangle*, rappresentante un triangolo, eredita da *Shape*.
Il suo costruttore, oltre al nome del triangolo,
accetta la lunghezza della base e un numero variabile di lunghezze degli altri lati.
Se viene fornita solo la lunghezza della base il triangolo è equilatero,
se viene fornita la lunghezza di un altro lato il triangolo è isoscele, altrimenti è scaleno.

Implementare i metodi astratti che della classe padre che restituiscono area e il perimetro.
Per il calcolo dell'area in modo generico si può utilizzare la
[formula di Erone](https://it.wikipedia.org/wiki/Formula_di_Erone).

La classe *Square* eredita da *Shape* e rappresenta un quadrato.
Il suo costruttore, oltre a nome del quadrato, accetta la lunghezza del lato.
Implementare i metodi astratti della classe padre che restituiscono l'area e il perimetro.


## Esercizio 2
Scrivere due decoratori per funzioni con argomenti sconosciuti (*args, **kwargs).
Il primo decoratore, ```repeat_ten_times(f)```, fa in modo che la funzione decorata sia invocata 10 volte.
Il secondo decoratore, ```time_execution(f)```,
stampa il tempo di esecuzione della funzione decorata, espresso in nanosecondi, dopo averla invocata.

Sviluppare la classe *Greet*, il cui costruttore accetti come parametro il nome della persona da salutare.
Il metodo ```say_hello(self) -> None``` stampa a schermo la scritta *"Hello"* seguita dal nome della persona
(ad es., *"Hello Pietro"*)

Il metodo ```say_good(self, time_of_day: str) -> None``` 
accetta come parametro un stringa contente il periodo della giornata (ad es., *"morning"*, *"afternoon"*, ecc...),
e stampa a schermo la scritta *"Good"* seguita dal periodo della giornata e il nome della persona
(ad es., *"Good evening Pietro"*).

Decoratore i due metodi con entrambi i decoratori, usandoli in ordine opposto.
Scrivere un main che testi i due metodi e notare le differenze dovute all'ordine dei decoratori.

**SUGGERIMENTO**: per calcolare il tempo di esecuzione di una funzione, importare *time*
e chiamare ```time.perf_counter_ns()``` prima e dopo averla invocata.
La differenza dei valori restituiti da ```time.perf_counter_ns()``` è il tempo di esecuzione in nanosecondi.

## Esercizio 3
Scrivere un programma in grado di trovare il percorso per attraversare un labirinto.
I labirinti sono rappresentati su file come una matrice di caratteri.
Il carattere ```W``` rappresenta un muro, il carattere ```E``` rappresenta una cella vuota e quindi percorribile,
mentre il carattere ```P``` rappresenta celle del percorso per attraversarlo.
Gli unici caratteri ```P``` forniti indicano l'entrata e l'uscita del labirinto.


```
# labirinto
WWWWWWWWWWWWWWWWWWWWWW      
WEWEWEEEEWWEWEEEEWEEWW
PEEEEEWWEEEEEEWWEEWEEW
WEWEWEEWEWWEWEWEWWWEWW
WWEEEWWEEEEWEEEEEEEEEW
WEEWEWEWWEWWWEWEWEWWEW
WEWWEWEEWWEWWWEEWEEEWW
WWEEWEWEEEEEWWEWWEWEEW
WEEWWEEEWEWEEEWEEWWEWW
WEWWEWEWEWWEWWEWEEEEEW
WEEEEEEEEWEEEEEEEWWEWW
WWPWWWWWWWWWWWWWWWWWWW
```
Trovare il percorso che collega l'entrata e l'uscita e cambiare il contenuto delle celle a ```P```:

```
# soluzione
WWWWWWWWWWWWWWWWWWWWWW
WEWEWPPPPWWEWEEEEWEEWW
PPPPPPWWPPPPPPWWEEWEEW
WEWEWEEWEWWEWPWEWWWEWW
WWEEEWWEEEEWEPPPPPEEEW
WEEWEWEWWEWWWEWEWPWWEW
WEWWEWEEWWEWWWEEWPPPWW
WWEEWEWPPPPPWWEWWEWPEW
WEEWWEPPWEWPEEWEEWWPWW
WEWWEWPWEWWPWWEWPPPPEW
WEPPPPPEEWEPPPPPPWWEWW
WWPWWWWWWWWWWWWWWWWWWW
```

Rappresentati graficamente:

<img src="img/lab1.png" width="300" />

<img src="img/lab1_sol.png" width="300" />


La cartella ```data``` contiene tre labirinti di diverse dimensioni.
```es3_template.ipynb```, da aprire in *jupyter notebook*, contiene del codice utile per importare e disegnare il labirinti.

**IMPORTANTE**: presa un strada nel labirinto,
essa può condurre a un vicolo cieco, ma non tornare a un punto già percorso.
Il labirinto pertanto può essere visto come un albero
in cui i nodi sono le celle del labirinto e i rami le deviazioni che è possibile prendere (su, giù, destra, sinistra).
L'esplorazione di un labirinto per trovare l'uscita è pertanto equivalente alla ricerca in profondità di un albero
per trovare le foglie (vicoli cechi o uscita).

## Esercizio 4
Partendo dallo scheletro della classe *SocialNetwork*, fornito nel file *es4_template.py*,
scrivere una classe che permetta di rappresentare le relazioni tra utenti in un social network.
Ogni utente può essere un follower del profilo di altri utenti del social network.

Pertanto il social network può essere rappresentato come un grafo
**DIRETTO** (chi è seguito può anche non seguire la persona che lo segue) e **NON PESATO**,
in cui gli utenti sono i nodi e i rami le relazioni di "follow".
Per l'implementazione del grafo utilizzare il metodo della **LISTA DI ADIACENZE**.

La classe deve permettere:
- di aggiungere un nuovo utente tramite il metodo ```create_account(self, username: str) -> None```, che accetta i nome del profilo.
- di controllare se un nome di profilo è presente sul social network tramite il metodo ```has_account(self, username: str) -> bool```.
- a un utente di seguirne un altro tramite il metodo ```follow(self, follower: str, followed: str) -> None```, che accetta il nome dei due profili.
- di ottenere una collezione contente il nome di profilo di tutti i followers di un dato profilo, tramite il metodo ```get_followers(self, username) -> Container[str]```.
- di ottenere una collezione contenente il nome di tutti i profili seguiti da un dato profilo ```get_followed(self, username) -> Container[str]```
- di ottenere una collezione di nomi profilo di tutti gli utenti del social network tramite il metodo ```get_users(self) -> Container[str]```
- di ottenere il numero di utenti del social network tramite il metodo ```__len__(self) -> int```

Scrivere un mail che testi l'implementazione caricando le relazioni di "follow" dal file *data/social_graph.txt*,
che contiene, per ogni riga, il nome di due profili utente, indicando che il primo segue il secondo.
