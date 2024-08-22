# Hash tables

Key value relationships

Some good points to note:
- Hash tables use mathematical mappings to compress the key space
  - A _hash function_ is used to map the raw key into the location in the table (aka _hash value_)
    - This allows us to map the key into an specific index in the internal array of values
- A good hashing function will reduce the amount of collisions

## Good for
- Pure storage cases
- Retrieve and store information quickly
- Particularly useful when used in Depth-First and Breadth-First Searches
  - Have a hashing function that maps the elements in a specific range of bins

## Complexity
| Big O notation | Scenario |
| -------------- | -------- |
|      O(1)      | Good hash table |
|      O(N)      | Terrible hash table, lots of collisions |

## Collisions
When two values share the same hashed value (of the key)

### Chaining
Chaining in an approach for handling collisions by employing linked lists on each value location.

This means that we can store multiple values with the same hash value

### Linear probing
Linear probing do not require linked lists but requires an extra data structure to store keys and values.

It basically looks for the next available space in the array of key/values starting from the index that got calculated by the _hash value_.
  - When reaching the end of the array, we need to start looking from the begining.

We might end up looking for values that are not restricted to ones with matching keys.

## Hashing function
A bad hashing function will cause the searches to be done in few overloaded keys (or bins), resulting in linear searches on these linked lists.

Your goal is to have a function that effectively maps keys uniformly throughout the space of bins.

### Considerations for your hashing function
- __Be deterministic__: Map the same key to the same bin **all the time**
- __Have a predefined range for a given size__: The hash function needs to map any key into a limited range, corresponding to the number of hash buckets
