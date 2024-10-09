import random



res1 = random.choice([0, 1, 2, 3, 4])
rand_choice = random.choice(['apple', 'banana', 'orange', 'pear'])
print(res1) 
print(rand_choice) 



rand_float = random.random()
print(rand_float) 




# une chiffre float aléatoire entre A et B
rand_float = random.uniform(2.5, 5.5)
print(rand_float) 



rand_int = random.randint(1, 10)
print(rand_int) 



# choisir k éléments dans la liste
seq = ['apple', 'banana', 'orange', 'pear', 'grape']
rand_sample = random.sample(seq, 3)
print(rand_sample)



# génerer une chiffre aléa dans la range((start, stop, step))
rand_range = random.randrange(0, 10, 2)



# géneration une chiffre qui obei la gausse  gauss(mu, sigma) dont mu为均值，sigma为标准差
rand_gauss = random.gauss(0, 1)



