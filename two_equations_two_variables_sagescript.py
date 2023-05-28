from Cryptodome.Util.number import long_to_bytes, bytes_to_long
import math 
from gmpy2 import *
gmpy2.get_context().precision=3000
c1 = 6561821624691895712873377320063570390939946639950635657527777521426768466359662578427758969698096016398495828220393137128357364447572051249538433588995498109880402036738005670285022506692856341252251274655224436746803335217986355992318039808507702082316654369455481303417210113572142828110728548334885189082445291316883426955606971188107523623884530298462454231862166009036435034774889739219596825015869438262395817426235839741851623674273735589636463917543863676226839118150365571855933
c2 = 168725889275386139859700168943249101327257707329805276301218500736697949839905039567802183739628415354469703740912207864678244970740311284556651190183619972501596417428866492657881943832362353527907371181900970981198570814739390259973631366272137756472209930619950549930165174231791691947733834860756308354192163106517240627845889335379340460495043

m1 = int(gmpy2.root(c1//5,7))
print(m1)
m2 = int(gmpy2.root((c2 - pow(m1,5))//7,3))
print(m2)
from libnum import n2s
print(n2s(m1)+n2s(m2))

# sage: F.<x,y> = ZZ[]
# sage: f = 13 * y ** 2 + x * y + 5 * x ** 7 - 6561821624691895712873377320063570390939946639950635657527777521426768466359662578427758969698096016398495828220393137128357364447572051249538433588995498109880402036738005670285022506692856341252251274655224436746803335217986355992318039808507702082316654369455481303417210113572142828110728548334885189082445291316883426955606971188107523623884530298462454231862166009036435034774889739219596825015869438262395817426235839741851623674273735589636463917543863676226839118150365571855933
# sage: g = 7 * y ** 3 + x ** 5 - 168725889275386139859700168943249101327257707329805276301218500736697949839905039567802183739628415354469703740912207864678244970740311284556651190183619972501596417428866492657881943832362353527907371181900970981198570814739390259973631366272137756472209930619950549930165174231791691947733834860756308354192163106517240627845889335379340460495043
# sage: F.<m1> = ZZ[]
# sage: F.<m2> = ZZ[]
# sage: print(f.resultant(g,y)(y=0, x=m1).roots()[0][0])
# sage: print(f.resultant(g,x)(y=m2, x=0).roots()[0][0])

print(long_to_bytes(2788921852171221111440879057471155338995686075935079372721930964530280) + long_to_bytes(672606797059492205907266474240230882559524138683883170067899497957191549))

# b'grey{solving_equation_aint_that_hard_rite_gum0pX6XzA5PJuro}'
