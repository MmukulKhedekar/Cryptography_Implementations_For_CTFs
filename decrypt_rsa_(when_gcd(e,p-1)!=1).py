from Cryptodome.Util.number import *

p = 147271787827929374875021125075644322658199797362157810465584602627709052665153637157027284239972360505065250939071494710661089022260751215312981674288246413821920620065721158367282080824823494257083257784305248518512283466952090977840589689160607681176791401729705268519662036067738830529129470059752131312559
c = 117161008971867369525278118431420359590253064575766275058434686951139287312472337733007748860692306037011621762414693540474268832444018133392145498303438944989809563579460392165032736630619930502524106312155019251740588974743475569686312108671045987239439227420716606411244839847197214002961245189316124796380

e = pow(3,pow(2,100),(p-1))
print(e)
k = pow(p,-1,e)
print(k-1)
c = pow(c,(k*p-1)//e,p)
for i in range(682):
    l = pow(p,-1,(k-1))
    print(l-1)
    c = pow(c,(l*p-1)//(k-1),p)
    k=l
c = pow(c,(p+1)//4,p)
print(long_to_bytes(c))

# b'grey{CubeIsSquarerThanSquare_FjUFynTNUdTyJu5x}'