# Mini-project report 
Members: Ebbe Karlstad and Firas Moussa\
Program: Software Technology and Network Security\
Course: 1DV501\
Date of submission: 2023-11-02

## Introduction  
This project in Introduction to Programming (1DV501) contains three different "sub-projects". These are Part 1: Count unique words, Part 2: Implementing data structures, and Part 3: Count unique words 2. In part 1, we were supposed to use Python's built-in sets and dictionaries to count the number of unique words and produce a top ten list of the ten most frequently used words for two files we used in a previous assignment, one of which is a snippet from Monty Python's "Life of Brian", and the other which is a report from the Swedish news.

In part 2, we were supposed to implement a hash-based set, and a map based on a binary search tree. For the hash-based set, we received two files, ``HashSet.py`` and ``hash_main.py``. Both of these files contained pre-made functions, in which we were supposed to implement the functions but not modify the existing ones. This was done to make them work when running the hash_main file, which calls all the functions and uses them in various ways. This file also contains examples of how the program should work, essentially, we wrote the HashSet program using the instructions from the hash_main file. Likewise, for the BST (Binary Search Tree) implementation, we got two files, ``BstMap.py`` and ``bst_main.py``. The BstMap, similarly to the HashSet file, came with pre-defined functions, without any code in them. Our task was to write these functions for the bst_main file to work.

In part 3, we were supposed to use our hash set and our bst map implementation to, like in part 1, count the numbers of unique words in the files, only this time using our own hash set, and present a list of the top-10 most frequently used words in both of the files, using our BST. We were also supposed to calculate the bucket list size (number of buckets in the hash set), the max bucket size (max amount of key-value pairs a single bucket can hold), and the zero-bucket-ratio (the proportion of buckets in the hash set that are empty) for both files. We also used our BST map implementation to calculate the number of tree nodes (all nodes in our BST), the max depth (how far we can reach down the tree until we reach a leaf node), and the internal node count (nodes that have at least one child.)

## Part 1: Count unique words 1
The total amount of words in the initial life_of_brian was; ``13431``, and the total amount in swedish_news_2020 was; ``15096801``.

The Top-10 part was implemented using a sorted dictionary. Since we were allowed to use dictionaries (which have an order) in this part of the project, the implementation of this was rather simple. We simply saved all the words into a dictionary and sorted them using:
```
def sort_by_value(item):
    return item[1]
```
And returning the 10 first words of the sorted dictionary  with:
```
def get_top10(input_dict):
    sorted_dict = sorted(input_dict.items(), key=sort_by_value, reverse=True)
    return sorted_dict[:10]
```
Lastly, we printed out the results using the get_top_10() function:
```
word_dict = task1.frequency_calculator(path)

print("Top 10 most frequent words used:")
sorted_dict = task1.get_top10(word_dict)

for word, frequency in sorted_dict:
    print(f"{word}: {frequency}")
```

The results of the unique words and the Top-10 lists are as follows:

```
The total amount of words in life_of_brian: 2112
The Total amount of words in swedish_news_2020: 411162

Top 10 most frequent words used:
-----------------------------
brian: 366
crowd: 161
centurion: 121
mother: 103
right: 99
crucifixion: 78
pilate: 68
pontius: 64
rogers: 52
there: 44

Top 10 most frequent words used:
-----------------------------
under: 54023
säger: 47539
efter: 44059
kommer: 42845
eller: 32066
också: 30473
sedan: 30375
andra: 28062
finns: 27576
många: 26811
```

## Part 2: Implementing data structures
Our task was to implement two data structures:

A set based on hashing, suitable for storing words.
A map based on binary search trees (BST).

Detailed Requirements:
1. BST-based Map:
    * Implementation: It should be a linked implementation.
    * Node Structure: Each node in the BST should have the fields; key, value, left child, and right child.
2. Hash-based Set:
    * Implementation: Use a Python list to store the buckets.
    * Bucket Structure: Each bucket within the "list of a list".
    * Initial Size: The start size of the bucket list should be 8.
    * Rehashing: When the number of elements in the set equals the number of buckets, we should double the size of the bucket list.
3. Additional:
    * Code skeletons are provided which outline the expected functions for both data structures. These skeletons also contain demo programs
    that show how we're supposed to use the various methods.
    * We can't change any of the already written functions.
---
### Method explanations:

HashSet:

The add() method in our word set based on hashes inserts a word into the hash set if it doesn't already exist. For this function, we first started by checking the conditions for the rehash() function if the size of the set is equal to the length of the buckets, i.e. if the set is full.
```
if self.size == len(self.buckets):
    self.rehash()
```
After this we calculate the bucket index for the word by calling the get_hash() function, we do this by calculating the index of the bucket where the word should be placed using the modulo operation to make sure it is in the right bounds.
```
hash_value = self.get_hash(word)
bucket_index = hash_value % len(self.buckets)
```
We then check if the word is found in the given bucket index, if it is found, the function will return and do nothing
```
if word in self.buckets[bucket_index]:
    return
```
If the word is not found inside of the given bucket index, we initialize a probe count variable to use for linear collision resolution, this was added when we were trying to lower the max bucket size for the hashset. Alongside a secondary hash function that takes the old hash value and increments it with 1 each time until we manage to find an empty bucket.

```
# Linear probing for collision resolution
    probe_count = 0  # Keep track of how many times we've probed
    while len(self.buckets[bucket_index]) != 0:

        # Check if the word already exists in the new bucket
        if word in self.buckets[bucket_index]:
            return  # Do nothing if the word is already in the bucket

        # Find a new bucket index
        new_hash = self.secondary_hash(hash_value + probe_count)
        bucket_index = new_hash % len(self.buckets)
        probe_count += 1

```

---
The get_hash() method computes a hash value for a given word. We simply do this by iterating over each character and the index of the character using the enumerate method and multiplying the ASCII value of the character by a prime number to the power of the index of the character. By using this modified hash function of the ASCII code, we are making sure that the hash value gets more randomized and also gives us the potential to have a lot larger hash values.
```
hash_value = 0
    for i, char in enumerate(word):
        hash_value += ord(char) * (31 ** i)
    return hash_value
```
The secondary_hash() method takes the old hash value and increments it with 1.
```
def secondary_hash(self, old_hash):
        return (old_hash + 1)
```
---
The rehash() method doubles the size of the bucket list when the hash set reaches its maximum size. We start by creating a variable new_bucket_size and setting it to twice the size of the current one, as well as creating a new set of buckets.
```
new_bucket_size = len(self.buckets) * 2
    new_buckets = [[] for i in range(new_bucket_size)]
```
It then goes through all the words in the old bucket and appends them to the new bucket based on their hash values. We again use the modulo operation the make sure we're in the right bounds.
```
for bucket in self.buckets:
    for word in bucket:
        new_bucket_index = self.get_hash(word) % new_bucket_size
        new_buckets[new_bucket_index].append(word)
```

Finally, we replace the old bucket list with the new one.

```
    self.buckets = new_buckets
```
---
### Differences from the given results in HashSet:
The outputs we got that differed from the output that was provided in the hash_main file were the max bucket size and the order of the names when we called the to_string() function to get a string representation of the hash set. This is simply because of the way hashing and rehashing works. When we add elements to our HashSet, it starts with 8 buckets, and after adding 8 unique elements, it rehashes and creates 16 new buckets. The way we hash and rehash can change both the order of the elements and the size of the bucket with the most elements (max bucket size), which is the reason for the two differences in our output compared to the provided output.

---
BstMap:

The put() method in our BST-based map is designed to insert a key-value pair into the binary search tree. We do this by first checking the left side of the tree, and if the current node doesn't have a left child, we insert a new node with the given key and value. If, however, the current node already has a left child, the method recursively calls put() on the left child. This continues until an empty node is found on the left side of the tree to insert a new node.
```
if self.key > key:
    if self.left is None:
        self.left = Node(key, value)
    else:
        self.left.put(key, value)
```
We then do the same thing, but for the right side of the tree:
```
elif self.key < key:
    if self.right is None:
        self.right = Node(key, value)
    else:
        self.right.put(key, value)
```
The last lines of this function handle cases where the node already has a key, which then updates it with a new value, in the case of task 3, the value would be the frequency of the word.
```
else:
    self.value = value
```
---
The max_depth() function in the program is designed to return the maximum depth of the binary tree. The depth here is the number of nodes along the longest path from the root node down to the leaf node farthest down. The left_depth variable is used to calculate the maximum depth of the left subtree. We use a ternary conditional to check if there's a left child (self.left) and calculate its depth. If there's no left child, left_depth is set to 0.
Similarly, the right_depth variable calculates the maximum depth of the right subtree using a similar ternary conditional.
Finally, we return the maximum depth of either the left or right subtree, whichever is greater, and add 1 for the current node. This accounts for the depth of the current level of the tree.
```
# Calculate the maximum depth of the left subtree
left_depth = self.left.max_depth() if self.left else 0

# Calculate the maximum depth of the right subtree
right_depth = self.right.max_depth() if self.right else 0

# Return the maximum depth of either subtree
# plus 1 for the current node
return max(left_depth, right_depth) + 1
```

## Part 3: Count unique words 2
For the Top-10 part of the problem, we did a similar solution to what we did in part 1. We created a function called get_top_10(), in which we used the as_list() method to get the list of all words, in which we used Python's built-in "sort" function and used key=lambda to sort it based on the value (frequency), and reversed it to get the most used words on top, instead of on the bottom. In the end, we returned the list with the ten most frequently used words.

```
lst.sort(key=lambda x: x[1], reverse=True)
    return lst[:10]
```
---
The results of the unique words, the Top-10 lists, the bucket list sizes, the max bucket sizes, the zero-bucket-ratios, the total node counts, the max depth, and the internal node counts for both of the files are as follows:

```
HashSet Results for brian_13431_words.txt:
--------------------------------------------------
Total unique words:      2112
Bucket List Size:        4096
Max Bucket Size:         4
Zero Bucket Ratio:       0.112

HashSet Results for news_15096801_words.txt:
--------------------------------------------------
Total unique words:      411162
Bucket List Size:        524288
Max Bucket Size:         6
Zero Bucket Ratio:       0.107

BST Results for brian_13431_words.txt:
--------------------------------------------------
Tree Nodes:              1457
Max Depth:               25
Internal Node Count:     984

BST Results for news_15096801_words.txt:
--------------------------------------------------
Tree Nodes:              395109
Max Depth:               112
Internal Node Count:     264547

Top 10 Words from Brian's BST:
--------------------------------------------------
Word: 'brian', Frequency: 366
Word: 'crowd', Frequency: 161
Word: 'centurion', Frequency: 121
Word: 'mother', Frequency: 103
Word: 'right', Frequency: 99
Word: 'crucifixion', Frequency: 78
Word: 'pilate', Frequency: 68
Word: 'pontius', Frequency: 64
Word: 'rogers', Frequency: 52
Word: 'there', Frequency: 44

Top 10 Words from Swedish News BST:
--------------------------------------------------
Word: 'under', Frequency: 54023
Word: 'säger', Frequency: 47539
Word: 'efter', Frequency: 44059
Word: 'kommer', Frequency: 42845
Word: 'eller', Frequency: 32066
Word: 'också', Frequency: 30473
Word: 'sedan', Frequency: 30375
Word: 'andra', Frequency: 28062
Word: 'finns', Frequency: 27576
Word: 'många', Frequency: 26811

Runtime: 63.79 seconds to run.
```
---
* The max bucket size can be a good indicator of how good the hash function is. When the max bucket size is low, it tells us that items are getting more evenly distributed across the buckets, which is a good indication since the amount of collision is decently low which also would lower the retrieval time. We can compare the max bucket size to the average size of each bucket (Total amount of elements / Total amount of buckets) to also get a good understanding of how well the hash function is.
An optimal average size of each bucket would be around 1, same for the max bucket size, since then we would be distributing all elements evenly throughout the buckets.
In this case, we have an average of ``0.51 & 0.71`` elements inside of each bucket and ``4 & 6`` as max bucket size, which tells us that we have room for improvement since the buckets are not being used to their full potential and are resulting in more empty buckets, for this, we would say that they are between reasonable to poor values.
Ideally, the max bucket size would be as close to the average bucket size as possible, and the average bucket size would be as close to ``1`` as possible.

- The zero bucket ratio tells us how many buckets are not being used, the most optimal in this case would be as close to 0 as possible. A reasonable value would be around 50% (0.5) and anything above that would be poor. In our case ``0.112 & 0.107`` are very optimal values. We can see that the zero bucket ratio is also getting lower for the Swedish news file which means the ratio is getting exponentially better. 

* The max depth of the binary search tree tells us the maximum amount of steps that we can go down the tree from the root until we reach a leaf node (node with no child nodes).
A well-balanced tree would ideally have as low of a max depth as possible. In regards to the number of nodes in the tree, the optimal max depth would be log2(N+1), where N represents the total number of nodes in the tree. Life of Brian with 1457 nodes would optimally have ``11`` as max depth, and Swedish news with 395109 nodes would optimally have ``19``. 
In our case, we have ``25`` & ``112`` which we would consider as reasonable to poor values.
This can be because the words added at the top of the tree might be too small or too high and therefore result in an unbalanced tree.
The internal node count should be as high as possible, meaning that most of the nodes have at least one child node. In our case ``984`` & ``264547`` are pretty optimal values considering the ratios to be around ``67%`` for both cases.


## Project conclusions and lessons learned

### Technical Issues

* A lot of the technical challenges were about making correct decisions to implement methods and functions that had a good balance between time efficiency and optimal results.
For example, when implementing a secondary hash function, depending on the way the hash function was implemented, it could provide better results in the zero bucket ratio and max bucket size, but at the same time, it could take longer for the program to run.

- We have learned that the efficiency of the program is not always dependent on one function, but rather the relationship between all the functions and how well they work together and also how well we use the functions to their full potential, an example of this would be when sorting the top 10 words in task 3. Instead of creating a new list with all words and reducing efficiency, we could use the function as_list() to save some time. Another example would be with the hash function when trying to reduce the zero bucket ratio and the max bucket size. Everything was not only dependent on the hash function, but rather how the items are added to the bucket and how a non-empty bucket will be handled by for example adding a secondary hash to try to reduce the max bucket size.

* More technically it took some time to reduce the zero bucket ratio and the max bucket size. But we solved this by adding a secondary hash function to try and lower the values as much as possible, which we think worked well in the end.
The results we think could be improved upon are the balance of the binary search trees. A thought we had is to manually populate the head of the tree with words that start with letters that are more in the middle of the alphabet to balance the tree accordingly.

### Project issues
- As a team we were working closely together every day, conducting meetups and brainstorming solutions. This helped us very much since we were able to look at the problems from two different perspectives and combine our coding knowledge for better and more efficient solutions.
The work was mostly split up so that we would work on implementing different methods and functions instead of working on the same things at the same time.
We found that this was time efficient and when we were finished with a function/method we would read each other's code and come up with any improvements that could be done. By planning and sitting together from the first day of the project, we managed to seamlessly create our Gitlab environments, deciding where to clone the repositories, create folders with the same names, and storing our data (.txt) files in the same places so there would not be any issues.


 ### Firas
 - Firas finished task 1 on the first day since it was pretty easy using dictionaries and sets as we have done before in the course.
 Firas likes to have aesthetic and organized code and this helped us for example in task 3 by putting everything into functions instead of having everything separated, as well as writing a lot of good comments. He is good at starting from scratch with functions and methods and coming up with ideas on how to get the program up and running for its purpose.
 Loves to write code and use creative thinking to solve problems, usually codes every evening and night at home where he can fully concentrate, and puts around 20 - 30 hours/week.

 ### Ebbe
 - Ebbe first focused mainly on the BstMap part of the project and also worked a bit on task 3 and the Hashet programs, together with Firas. He's pretty good at breaking things down and making sure everything fits together. He likes organizing projects, and their structure and keeping things neat and simple, which is why you'll see a portion of his commits are small changes to the code to make it print out more nicely, or changing the structure of the code to make it easy to read and organized. Since Firas finished task 1 on the first day, Ebbe couldn't do much on this part,
 but still learned the ins and outs of the program to make it easier to do task 3. He also stayed up for four hours one night and wrote most of the document. On average, Ebbe put in about 15-20 hours a week on the project.&nbsp;  
&nbsp;  

### Lessons & Improvements
- We got a handle on how binary search trees work by implementing various functions that change them in different ways, which made us learn about how they fit into larger systems. Hashing was another area we learned a lot about, and it was interesting to see how it changes the output using different methods. Beyond the technical aspects, one of the big takeaways was the importance of communication. We learned a lot about collaborating and sharing codes on GitLab. We did hit a few bumps along the way, with pushing our codes at the same time, and we could've had a bit better communication around task 1. If we were to do a similar project in the future, we'd focus more on improving our communication from the start.