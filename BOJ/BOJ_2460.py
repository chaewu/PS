sonnom = 0
max_sonnom = 0

for _ in range(10):
    out_gicha, in_gicha  = map(int, input().split()) 
    sonnom += in_gicha - out_gicha 
    max_sonnom = max(sonnom, max_sonnom) 
    
print(max_sonnom)