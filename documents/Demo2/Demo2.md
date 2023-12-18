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

# Coaster detection 

- Working detection model but code is broken'
- Mostly accurate feature matching, needs bounding box implementation
- Homogenous transformation of detected coaster for angle correction most likely unnecessary



---

# Model training for coaster detection
## Dataset
- 179 Photos of 120 coasters, 5 empty photos
![width:300px](./pictures/Dataset/website.png) ![width:150px](./pictures/Dataset/dataset2.jpg) ![width:150px](./pictures/Dataset/dataset3.jpg)
---

# Training results
![image](./pictures/Training_graph.png)

------

# Model inference test
![image](./pictures/Infertest/images1.jpg) ![image](./pictures/Infertest/images2.jpg)![image](./pictures/Infertest/images3.jpg)![image](./pictures/Infertest/images4.jpg) ![image](./pictures/Infertest/testimg1.jpg)![image](./pictures/Infertest/testimg3.jpg)![image](./pictures/Infertest/testimg4.jpg) ![image](./pictures/Infertest/testimg6.jpg)![image](./pictures/Infertest/testimg7.jpg)![image](./pictures/Infertest/testimg8.jpg)![image](./pictures/Infertest/testimg9.jpg)

---

# Inference test results
![width:200px](./pictures/TestDetections/images1.jpg) ![width:300px](./pictures/TestDetections/images2.jpg) ![image](./pictures/TestDetections/images3.jpg) ![image](./pictures/TestDetections/images4.jpg) ![width:100px](./pictures/TestDetections/testimg1.jpg) ! ![width:100px](./pictures/TestDetections/testimg3.jpg) ![width:100px](./pictures/TestDetections/testimg4.jpg) ![width:100px](./pictures/TestDetections/testimg5.jpg)  ![width:100px](./pictures/TestDetections/testimg8.jpg) ![width:100px](./pictures/TestDetections/testimg9.jpg) 
![width:400px](./pictures/TestDetections/testimg7.jpg)![width:400px](./pictures/TestDetections/testimg6.jpg) 

---

# Work involved

- Feature matching for instance level recognition
- Integration of existing code
- Model training for coaster detection
- Custom dataset creation
- Model training environment errors took time to resolve

<!-- - individual coaster **instance** recognition and coaster **class** classification -->

---

# Moving forwards
- Combine modules for full functionality
- Speed optimizations
- Final goal is quick and accurate matching from various coaster types
- Color dependant features/recognition
- Different search for faster coaster addition
- Async call implementation 

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