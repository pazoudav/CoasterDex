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

**image level retrieval** finding images similar to a provided query from a large database [2]

---

# requirements: from basic to nice to have

- determining if a coaster in present in a database and retrieve the match
- matching a coaster from a complex scene
- coaster recognition in a scene
- transforming the 'segmented' coaster to correct plane
- generalize to other object domains
- retrieval from video at framerate

---

# differences
- single domain/class with high variability
- only one instance of each item present



---

# dataset

website of a personal beer coaster collection: https://www.beer-coasters.eu/cz/pivni-tacky.html
![width:200px](https://www.beer-coasters.eu/coasters/branik-10.jpg)

collecting photo in real environment:
![width:200px](https://g.denik.cz/54/45/20151127-pivo-tacek-osek_denik-galerie-800@2x.jpg)

manufactured dataset from printed paper coasters

---

# methods



---

# performance measures



---

# sources

[1] https://blog.research.google/2020/09/advancing-instance-level-recognition.html
[2] https://paperswithcode.com/task/image-retrieval

