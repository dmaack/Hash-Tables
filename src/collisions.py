import random

def how_many_before_collision(buckets, loops=1):
    """

    Roll random hashes indexes into buckets and print how many rolls beofre collision

    Run loops times
    """

    for i in range(loops):
        tries = 0 
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets

            if hash_index not in tried:
                tried.add(hash_index) # would it work to use a python list instead of a set? 
                tries += 1
            else:
                # We have found the collision
                break
        print(f'{buckets} buckets, {tries} hashes before collisions. ({tries/buckets * 100:.1f}%)') # 1 decimal float percision

how_many_before_collision(10, 1)
how_many_before_collision(100, 1)
how_many_before_collision(1000, 1)
how_many_before_collision(10000, 1)
how_many_before_collision(100000, 1) # HACKERRANK TIP: a possibility of failing one of the tests (time out), you might have used the list/array and should have used something else
how_many_before_collision(10, 10)