---
marp: true
---

# CoasterDex
## by David Pažout and Dagur Elinór Kristinnson 

---

<!-- - Evolution of your project idea and where you are with respect to your goals.
- Results so far:
    - Elaboration of background material that you have discovered, including previous work (papers, existing systems), useful software, and data sets.
    - Methods tested and selected.  Explain the methods that you selected and how you adapted them to meet the needs of your application.
    - Numerical results of your performance measures, and how they evolved over the project.  What changes made the most improvement?  Compare your results to background work.
    - Live demonstration of the capabilities of your system. Show and discuss both success and failure.
- Work involved:
    - Division of labor - who did what. 
    - What has taken up the most time?
    - Particular challenges.
- Conclusions
    - What worked well first-time and what would you do differently, if doing the project over again?
    - Ideas for future work on the project or spin-offs.

--- -->

# Achievements 
## from first presentation
- success
    - determining if a coaster in present in a dataset and retrieve the match, otherwise add the coaster to the collection
    - matching a coaster from a complex scene (varied lighting and angles)
    - coaster recognition in a scene
    - custom dataset
- somewhat
    - transforming the marched coaster to a frontal view
    - retrieval from video at framerate
- failed
    - extract additional data

---

# Achievements 
## from last week presentation
- success
    - combine modules for full functionality
    - different search for faster coaster addition
- somewhat
    - async call implementation
- failed
    - *Color dependant features/recognition*

---

# Instance recognition - methods
- instance recognition overviews [1], [2]
- used methods: 
    - Contrast Limited Adaptive Histogram Equalization (CLAHE)
    - RootSIFT features, VLAD encoding, BallTree NN search
- other steps
    - key-point matching filter
    - dynamic database
    - bbox rescaling

---

# Instance recognition - results

![width:600px](pictures/matcher-table1.jpg)

---

![width:500px](pictures/matcher-ex2.jpg) ___ ![width:500px](pictures/matcher-ex1.jpg)

---

# Augmentation
## Roboflow provided automatic augmentation
Flip, 90°Rotate, Crop, Shear, Grayscale, Hue, Brightness, Exposure, Blur,
Bounding Box: Rotation, Bounding Box: Shear, Bounding Box: Brightness,
Bounding Box: Noise
190 images -> 498 images

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

# Coaster detection
44 images with 50 coasters not present in training set
# Synthetic version:
    Recall = 0.96, Precision = 0.83
    Average confidence of correct detections = 0.74
# Augmented version:
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
- Training dataset needs more environment objects, specifically beer for better recall
- Augmentation can be experimented with to be utilized more effectively to improve generalization
- Augmented model might prove superior since both train and test datasets are most likely to specific

--- 
<!-- 
- Work involved:
    - Division of labor - who did what. 
    - What has taken up the most time?
    - Particular challenges. 
-->

# Work involved
- Feature matching for instance level recognition
    - Parallelization
    - Integration of existing code
- Model training for coaster detection
    - Custom dataset creation
    - Model training environment errors took time to resolve
- Integration across systems 

---

<!-- 
- Conclusions
    - What worked well first-time and what would you do differently, if doing the project over again?
    - Ideas for future work on the project or spin-offs. 
-->

# Conclusion

- would would we do differently, if are doing the project over again?
    - better research methodology
    - better recording of the process
- future improvements
    - full parallelism
    - extension to a full application
    - proper database
    - more advanced testing

---

# Thank you for your attention

---

# Questions?

---

# Sources
[1] https://ieeexplore.ieee.org/document/7935507
[2] https://arxiv.org/pdf/2101.11282.pdf
[GitHub] https://github.com/pazoudav/CoasterDex/tree/main