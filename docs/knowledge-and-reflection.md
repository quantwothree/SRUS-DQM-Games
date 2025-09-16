# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> All of the functions above are hash functions because they all share these common properties:
- They all take an input and give an output 
- If the same input is given then the output would also be the same. This kind of determinism is achieved by the mathematics inside each hash function. 
- The output stays within a defined range, from 0 to size -1. Except for the ssh hash, which always return a 1. Other than the ssh hash, other hash functions above all calculate the output by using modulo on its size (% size). 
- They all have the tendency to have collisions at some point, the lower the size the greater the chance. 
- They are designed, direclty or indirectly to use in a hashmap, to distribute key-value pairs accross a table, which is the main purpose of hashing 

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> SSH: 
    This hash function has the worst uniformity because it ignores the input and always return a 1. If the hashmap has 10 slots, only slot 1 will be used (not distributing hash values evenly across). 

    SSH has good determinism meaning the same input should give the same output everytime. In this case the output is always 1 regardless anyways. 

    For efficiency, this hash function should be really fast since it doesn't compute anything internally.

    Its collision resistance is none. Because it returns 1 always, a collision happens every time it takes an input.

    Same thing here for sensitivity to input changes, it is not sensitive at all. 

    It is totally insecure because of its output predictability and probably vulnerable to DoS attac because all values end up in the same index, look up time becomes slow and might crash the system 


ASCII Hash function:
    This hash function has a poor to fair uniformity rating. Because it is based only on the sum of ASCII values, regardless of the order of the characters. Meaning 'abc' 'acb' 'bca' 'bac' 'cab 'cba' all give 294 as the sum, which mnean they would all do in the same index - the opposite of what we want in uniformity. 

    However it is deterministic. Since calculated based on ASCII, the same input would always generate the same output. 

    It is also relatively fast, not a lot of operations internally. 

    It is not resistant to collisions because of the poor uniformity, many combinations of characters will be allocated to the same index causing collisions. 

    It is not so sensitive to input changes because a smallest change of 1 single letter in the combination would only add or minus the ASCII value of that single character, all other ASCII values remain the same, meaning the sum will not change drastically. 

    Since it is based on ASCII values, it is not very secure because someone can easily do the math operations in reverse to find out the input.


Pearson Hash function:
    Peason hash function has moderate uniformity given if the Pearson table is well randomized. When the table is well randomized, over many inputs the final hash will be evenly spread accross the output range. 

    It is deterministic if the pearson table stays the same. So for each different randomized pearson table, we have a fixed input-output pair. 

    It is considered to be fast because of its lightweight design with no complex math or recursion. 

    The output is from 0 to 255, this means that at some point we will have a collision. So collision resistance is not very good here. 

    It is somewhat sensitive to input changes since every character in the combination will effect the next character's hash value and so on. 

    It is also not secure due to the fact that it has small output range, not resistant to collisions, and probably could be brute-forced easily. Also consider the fact that it's secret here is the randomized Pearson table, if someone have the table they can reverse the process ti find the input. 


Built-in Hash function:
    This function has moderate uniformity especially with larger hashmap size, but for smaller size, the modulo would probably distribute the hash values unevenly. 

    Because the built in hash() is random between different sessions, given that the hashing is in the same Python session, it is deterministic, hash() would give the same output for every same input. 

    It is very fast since all it does is passing kthe key into a built in hash(), nothing extra. 

    Even though the output range of hash() is large, but it is narrowed down by the modulo and size, The Birthday Paradox applies here and we will encounter collisions more often than we think. 

    It is sensitive to input changes since Python hash() produces drastically different hash for very small changes in the inputs. 

    It is considered to be not very secure and that is exactly why Python has to randomize its interal opertations for every Python sesssion.

SHA256 Hash function:
    SHA-256 has good uniformity, it is designed to evenly and randomly spreads outputs accross the table. 

    It is fully deterministic, the same input will always generate the same output regardless of sessions, computers, systems, etc 

    However, due to the complexity and security features, it lacks efficiency, it is slower than many simple hash functions. 

    Its resistance to collisions is excellent because of its cryptographic design. THe output hash is 256-bit, which gives SHA-256 a very large number of possible output hashes (115792089237316195423570985008687907853269984665640564039457584007913129639936) making it extremely unlikely for a collision to ever occur.

    It is also designed to be very sensitive to input changes with an avalanche effect, which means even a tiny change produces a very different has outcome. 

    It is very secure but maybe overkill for simple hash for general uses. 




3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> In the context of a hashmap it is important to consider these atttributes:
The most important thing is the hash function itself. Because a poor-designed hash function would defeats the purpose of a hashmap. For example the first hash function mentioned above always return a 1 regardless of inputs. That hash function would put everything into index number 1, causing a collision every single time, requiring collision handling every single time, taking a lot of time and resources to resolve and "find" the item in the map. 

THe second most important thing is collision resistance, since a hashmap is use to map out key-value pair, we want to minimize the chance of a collision from happening. Because when it happens we need to handle it and it again becomes the problem we are trying to solve in the first place. 

The last one is how it will handle collisions. Collisions in hashing is unavoiable, it will happen eventually but probably takes a very long time for something highly secured like SHA 256. But when it does happen, we want it to handle collisions well enough. 


4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> For the implementation of the task, I would use the Pearson Hash function, because it is not too simple when it breaks the purpose of the task but also it is not overly complex and become overkill. 

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> 
import random 
-> import the Python random module to perform a shuffle 

random.seed(42) 
-> basically set the random 'behaviour' so that everytime it randomize something, the opertation/ procedure stays consistent
-> this line makes sure determinism for this hash function, because even with different Python sessions, random.seed(42) makes sure that the Pearson Table below will be randomized the same way, giving the same randomized table all the time. Unless you change the 42 to a different number. With the same table we can have the same output for the same input every time. 

pearson_table = list(range(256)) 
-> create a list called pearson_table that consists of numbers from 0 to 255 
-> this line and the ones below affect the uniformity of this hash function. A hash function's uniformity largely depends on it's internal mathematical operations determining how well it distributes outputs. 
-> because the 'secret' of this function is this Pearson table, therefore if someone has access to the table and its randomized state, they probably can figure out the input, making it not every secure

random.shuffle(pearson_table) 
-> shuffle that list, so that now the list still contains numbers from 0 to 255 but in random order

def pearson_hash(key: str, size: int) -> int: 
-> declare the hash function which take a key as a string and return an integer

    hash_ = 0 
    -> set the variable hash to 0 
    
    for char in key: 
    -> loop through every character in the string, for each character do the folowing:
        
        hash_ = pearson_table[hash_ ^ ord(char)] 
        -> get the ascii values of that single character then perform a bitwise comparison with the previous value of the hash_, then use the result of that as the index in the pearson table, where its associated value will be assigned to the hash_, updating it. 
        -> this line relates to the function's sensitivity to input changes, because each character in the combination will affect the next character's hash value and ultimately affecting the final outcome 
    
    return hash_ % size 
    -> after the loop, we have the final hash value, perform a modulo with the size of the hashmap to decide which index in the map the final hash goes to 


6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Create an empty hashmap with a specified size.
For each index from 0 to size-1, initialize an empty PlayerList at that index.

Inserting Players into the HashMap (inserting a player via __setitem__):
    Check if the key is a Player or str
        If it is a str, the key is the string 
        If it is a Player, the key is the uid of the player 
    Hash the key 
    Use the result of that as the index in the player list 
    Find the player with that index 
    If player already in the list
        update the name 
    If not 
        create a player 
        create a node with that player 
        insert that node into the player list 

    

## Reflection

1. What was the most challenging aspect of this task?

> The most chanllenging aspect of this task, to me, was the process of implementing what I understand into actual code. After reading the requirements of the task and after understaning how hashing and hashmap works. I have the whole concept of how this should work visualised in my head, but when it comes to actually put that into Python code and make it work, I encountered problems with working with code that I would not have thought about with only visualising the process and not actually doing it. 

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> If I didn't have to use a PlayerList, I would probably go for a dictionary. 

Meaning my HashMap would contain a list of dictionaries, each dictionaries has its index in the list, which dictionary the player would go to depends on the hash function. When collision happens, I would just append that the players in that dictionary, and also finding or getting a player is easier with dictionaries too. 


## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
