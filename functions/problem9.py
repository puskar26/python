# Yeild
# Generator function

def even_generator(limit):
    for i in range(2, limit+1,2):
            yield i
        
for i in even_generator(20):
      print(i)