---
marp: true
---

# CoasterDex
## by David Pažout and Dagur Elinór Kristinnson 

---

# motivation

My friend has a large collection of beer coasters (+200).
When I'm in a pub and see a coaster, I don't know if they already have it or not. I could ask them but sometime they don't know either. I don't want to bring them duplicate coaster or bother them all the time (and its nice to surprise them with a new coasters).
![alt text](https://i.pinimg.com/564x/d1/cb/27/d1cb27e1a5dd3983174b1e70c4a17a7d.jpg)

---

# problem statement

**instance level recognition**: computer vision task of recognizing a specific instance of an object, rather than simply the category to which it belongs [1]
- recognition
- retrieval

---

# minimum requirements

![height: 20px](https://www.beer-coasters.eu/coasters/branik-10.jpg)

---

# Methods 

Some level of machine learning would be required to locate the object. We would like to avoid having it do the comparison due to the inherent need for dynamic collection management.
This makes it stand out 

---

# performance

We would like to minimize the time it takes for the person photographing the object to recieve a result. Object tracking time and image comparison time.

---

# dataset

website of beer coaster collection https://www.beer-coasters.eu/cz/pivni-tacky.html
collecting photo in real environment


---

# sources

[1] https://blog.research.google/2020/09/advancing-instance-level-recognition.html


