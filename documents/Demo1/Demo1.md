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
- performance measures: 

---

# Status 

- Working detection model but code is broken'
- Mostly accurate feature matching, needs bounding box implementation
- Homogenous transformation of detected coaster for angle correction most likely unnecessary

---

# Work involved

- Feature matching for instance level recognition
- Handled by David
- Model training for coaster detection
- Handled by Dagur Elinór Kristinsson
- Custom dataset creation
- Model training environment errors took time to resolve
- Integration of existing code
<!-- - individual coaster **instance** recognition and coaster **class** classification -->

---

# Model training for coaster detection
## Dataset
- 179 Photos of 120 coasters, 5 empty photos
![image](./pictures/Dataset/website.png) | ![image](./pictures/Dataset/dataset2.png)
![image](./pictures/Dataset/dataset3.png)
---

# Training results
![image](./pictures/Training_graph.png)

------

# Model inference test
![image](./pictures/Infertest/images1.jpg) ![image](./pictures/Infertest/images2.jpg)![image](./pictures/Infertest/images3.jpg)![image](./pictures/Infertest/images4.jpg) ![image](./pictures/Infertest/testimg1.jpg) ![image](./pictures/nfertest/testimg2.jpg)![image](./pictures/Infertest/testimg3.jpg)![image](./pictures/Infertest/testimg4.jpg)![image](./ictures/Infertest/testimg5.jpg)![image](./pictures/Infertest/testimg6.jpg)![image](./pictures/Infertest/testimg7.jpg)![image](./pictures/Infertest/testimg8.jpg)![image](./pictures/Infertest/testimg9.jpg)

---

# Inference test results
![image](./pictures/TestDetections/images1.jpg) ![image](./pictures/TestDetections/images2.jpg) ![image](./pictures/TestDetections/images3.jpg) ![image](./pictures/TestDetections/images4.jpg) ![image](./pictures/TestDetections/testimg1.jpg) ![image](./pictures/TestDetections/testimg2.jpg) ![image](./pictures/TestDetections/testimg3.jpg) ![image](./pictures/TestDetections/testimg4.jpg) ![image](./pictures/TestDetections/testimg5.jpg) ![image](./pictures/TestDetections/testimg6.jpg) ![image](./pictures/TestDetections/testimg7.jpg) ![image](./pictures/TestDetections/testimg8.jpg) ![image](./pictures/TestDetections/testimg9.jpg) 


---

# Moving forwards
- Combine modules for full functionality
- Speed optimizations

- Final goal is quick and accurate matching from various coaster types

- integration between our systems
- color dependant features/recognition
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