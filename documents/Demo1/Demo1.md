---
marp: true
---

# CoasterDex
## by David Pažout and Dagur Elinór Kristinnson 

---

# Points

- project Evaluation
- Project status with respect to min and max goals.
- Elaboration of background materials: papers/existing systems, software, and data sets.
---

# Instance recognition 
- instance recognition overviews [1], [2]
- tested and used methods: 
    - Contrast Limited Adaptive Histogram Equalization (**CLAHE**)
    - SIFT, **RootSIFT**, ORB and MAC features
    - **coco** and coco/coaster codebooks
    - **basic** and RANSAC-geometric key-point matching
    - updating database
- performance measures ???

---

# Work involved
- individual coaster **instance** recognition and coaster **class** classification
- dataset creation, integrating existing code

---

# Moving forwards
- integration between our systems
- different search for faster coaster addition
- async call implementation 

---

# Thank you for your attention

---

# Questions?

---

# Sources
[1] https://ieeexplore.ieee.org/document/7935507
[2] https://arxiv.org/pdf/2101.11282.pdf
<!-- 
[1] https://blog.research.google/2020/09/advancing-instance-level-recognition.html
[2] https://paperswithcode.com/task/image-retrieval
[3] https://www.beer-coasters.eu/cz/pivni-tacky.html
[4] https://www.beer-coasters.eu/coasters/branik-10.jpg
[5] https://g.denik.cz/54/45/20151127-pivo-tacek-osek_denik-galerie-800@2x.jpg
[6] https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7935507
[7] https://www.diva-portal.org/smash/get/diva2:422669/FULLTEXT01.pdf
[8] https://github.com/tensorflow/models/tree/master/research/delf
[9] https://ieeexplore.ieee.org/abstract/document/6475023
[10] https://dl.acm.org/doi/pdf/10.1145/3240508.3240522 -->