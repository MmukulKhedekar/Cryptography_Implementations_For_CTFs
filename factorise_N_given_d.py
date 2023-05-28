from Cryptodome.Util.number import long_to_bytes, bytes_to_long
import math
n=0xa66791dc6988168de7ab77419bb7fb0c001c62710270075142942e19a8d8c51d053b3e3782a1de5dc5af4ebe99468170114a1dfe67cdc9a9af55d655620bbab
e=10001
d=0x123c5b61ba36edb1d3679904199a89ea80c09b9122e1400c09adcf7784676d01d23356a7d44d6bd8bd50e94bfc723fa87d8862b75177691c11d757692df8881
k=e*int(str(d),16)-1
print(k)
n=int(str(n),16)
g=2
while (k>1):
    x=pow(g,k,n)
    if math.gcd(x-1,n)>1:
        print(math.gcd(x-1,n))
        print(n/math.gcd(x-1,n))
        break
    k=k//2