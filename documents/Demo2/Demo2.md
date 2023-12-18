---
marp: true
---

# CoasterDex
## by David Pažout and Dagur Elinór Kristinnson 

---


# Instance recognition 
- instance recognition overviews [1], [2]
- tested and used methods: 
    - Contrast Limited Adaptive Histogram Equalization (**CLAHE**)
    - SIFT, **RootSIFT**, ORB and MAC features
    - **coco** and coco/coaster codebooks
    - **basic** and RANSAC-geometric key-point matching
    - updating database

---

# Coaster detection model improvements
## Old Dataset
- 179 Photos of 120 coasters, 5 empty photos
## Additions
- 4 coasters with a beer glass nearby
- 2 pictures with faces
- Dataset augmentation 
![width:100px](./pictures/TrainDataExample.jpg)

---

# Augmentation
## Roboflow provided automatic augmentation
Flip, 90°Rotate, Crop, Shear, Grayscale, Hue, Brightness, Exposure, Blur,
Bounding Box: Rotation, Bounding Box: Shear, Bounding Box: Brightness,
Bounding Box: Noise
190 images -> 498 images

---

# Coaster detection model test
44 images with 50 coasters not present in training set

Synthetic version:
    Recall = 0.96, Precision = 0.83
    Average confidence of correct detections = 0.74
Augmented version:
    Recall = 0.9, Precision = 0.85
    Average confidence of correct detections = 0.78

---

# Detections example V1

![width:200px](./pictures/V1/testimg22.jpg) ![width:200px](./pictures/V1/testimg37.jpg) ![width:200px](./pictures/V1/testimg35.jpg) ![width:200px](./pictures/V1/testimg29.jpg) ![width:200px](./pictures/V2/testimg33.jpg)

---

# Detections example V2

![width:200px](./pictures/V2/testimg22.jpg) ![width:200px](./pictures/V2/testimg37.jpg) ![width:200px](./pictures/V2/testimg35.jpg) ![width:200px](./pictures/V2/testimg29.jpg) ![width:200px](./pictures/V2/testimg33.jpg) 

---

# Finalizing dataset
- Training dataset needs more environment objects and more beer for better recall
- Augmentation can be experimented with to be utilized more effectively to reduce generalization
- Augmented model might prove superior since both train and test datasets are most likely to specific

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