import random
from js import document, localStorage
import js

words = ['bloop','blop','BLOOP','bleep','blep','boop', 'blooop','bop']
n = 0
try:
    n = int(localStorage.getItem('catso_n') or 0)
except:
  n=0

def bloop(*a):
    global n
    n = n+1
    try: localStorage.setItem('catso_n', str(n))
    except: pass
    w = random.choice(words)
    if n % 100 == 0 :
        w = str(n) + '!!!'
    if random.random()<0.02: w = 'meow'
    return w

def count(): return n

def pitch():
    return 0.8 + random.random()*0.6

def say(t):
  document.getElementById('t').innerText = t

#def bloop_old():
#    return 'bloop'

js.window.py_bloop = bloop
js.window.py_count = count
js.window.py_pitch = pitch
say('click the cat (python on)')
document.getElementById('n').innerText = 'bloops: ' + str(n)
