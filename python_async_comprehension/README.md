# Python - Async Comprehension

## Sommaire

1. [Generateurs asynchrones](#generateurs-asynchrones)
2. [Async comprehensions](#async-comprehensions)
3. [Typage des generateurs](#typage-des-generateurs)
4. [asyncio.gather et parallelisme](#asynciogather-et-parallelisme)

---

## Generateurs asynchrones

### Qu'est-ce qu'un generateur classique ?

Un generateur est une fonction qui utilise `yield` au lieu de `return`. Au lieu de renvoyer une seule valeur, il **produit** une sequence de valeurs une par une, de maniere paresseuse (lazy).

```python
def compteur():
    for i in range(5):
        yield i

for val in compteur():
    print(val)  # 0, 1, 2, 3, 4
```

### Passer a l'asynchrone : `async def` + `yield`

Un **generateur asynchrone** combine `async def` avec `yield`. Il permet de produire des valeurs tout en effectuant des operations asynchrones (attente reseau, temporisation, etc.).

```python
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)   # attente non bloquante
        yield random.uniform(0, 10)
```

Points cles :

- `async def` declare une coroutine.
- `await` suspend l'execution sans bloquer la boucle evenementielle.
- `yield` produit une valeur a chaque iteration.
- On itere dessus avec `async for`, pas `for`.

```python
async def main():
    async for value in async_generator():
        print(value)
```

### Difference entre `yield` et `return`

| `return` | `yield` |
|----------|---------|
| Termine la fonction | Suspend la fonction |
| Renvoie une seule valeur | Produit plusieurs valeurs |
| La memoire stocke tout | Les valeurs sont generees a la demande |

---

## Async comprehensions

### Comprehension classique (rappel)

```python
# List comprehension classique
carres = [x ** 2 for x in range(10)]
```

### Async comprehension

Meme syntaxe, mais avec `async for` pour consommer un generateur asynchrone :

```python
async def async_comprehension():
    return [i async for i in async_generator()]
```

Cela equivaut a :

```python
async def async_comprehension():
    result = []
    async for i in async_generator():
        result.append(i)
    return result
```

L'async comprehension est plus concise et idiomatique. Elle fonctionne aussi pour les sets et les dicts :

```python
# Async set comprehension
unique = {i async for i in async_generator()}

# Async dict comprehension
indexed = {idx: i async for idx, i in aenumerate(async_generator())}
```

---

## Typage des generateurs

Python permet d'annoter les types de retour des generateurs avec le module `typing`.

### Generator classique

```python
from typing import Generator

def compteur() -> Generator[int, None, None]:
    for i in range(5):
        yield i
```

`Generator[YieldType, SendType, ReturnType]` :

| Parametre | Description |
|-----------|-------------|
| `YieldType` | Type des valeurs produites par `yield` |
| `SendType` | Type des valeurs envoyees via `.send()` (`None` si pas utilise) |
| `ReturnType` | Type de la valeur de `return` (`None` si pas utilise) |

### AsyncGenerator

Pour les generateurs asynchrones, on utilise `AsyncGenerator` :

```python
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

`AsyncGenerator[YieldType, SendType]` ne prend que deux parametres (pas de `ReturnType`).

---

## asyncio.gather et parallelisme

### Le probleme : executer des taches en parallele

Si on execute 4 coroutines sequentiellement, chacune prenant 10 secondes, le total est de 40 secondes :

```python
# Sequentiel : ~40 secondes
await async_comprehension()
await async_comprehension()
await async_comprehension()
await async_comprehension()
```

### La solution : `asyncio.gather`

`asyncio.gather` lance plusieurs coroutines **en parallele** (concurrence) sur la boucle evenementielle :

```python
# Parallele : ~10 secondes
await asyncio.gather(
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
)
```

### Pourquoi ~10 secondes et pas ~40 ?

```
Temps -->  0s -------- 5s -------- 10s
Tache 1:  |=========================|
Tache 2:  |=========================|
Tache 3:  |=========================|
Tache 4:  |=========================|
```

Chaque tache fait 10 iterations de `await asyncio.sleep(1)`. Pendant qu'une tache attend (`await`), les autres peuvent s'executer. Toutes les taches **partagent la meme boucle evenementielle** et progressent simultanement.

Le temps total est donc celui de la tache la plus longue (~10s), pas la somme de toutes les taches.

### Mesurer le temps d'execution

```python
import time

async def measure_runtime() -> float:
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
```

`time.perf_counter()` est prefere a `time.time()` car il offre une meilleure precision pour mesurer des intervalles.

### gather vs autres approches

| Methode | Usage |
|---------|-------|
| `asyncio.gather` | Lancer plusieurs coroutines et attendre toutes les reponses |
| `asyncio.create_task` | Lancer une tache en arriere-plan |
| `asyncio.wait` | Attendre avec plus de controle (premier termine, timeout, etc.) |

---

## Resume des concepts

| Concept | Syntaxe | Exemple |
|---------|---------|---------|
| Generateur async | `async def` + `yield` | `yield random.uniform(0, 10)` |
| Async comprehension | `[x async for x in ...]` | `[i async for i in async_generator()]` |
| Type annotation | `Generator[Y, S, R]` | `-> Generator[float, None, None]` |
| Parallelisme | `asyncio.gather(*coroutines)` | `await asyncio.gather(c1(), c2())` |
