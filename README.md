# A Hands-on Introduction to Natural Language Processing (NLP)


### About this course
This course was created by [Prof. Mohammad Ghassemi](https://ghassemi.xyz) in Fall of 2020 as part of the CSE 842 class at Michigan State University. The course provides a step-by-step guide to NLP and makes no assumptions that you have a background in the material (NLP or Machine Learning). The content in this repository will teach you:

1. How to collect and process text data.
2. How to generate text using language models.
3. How to classify text using machine learning.
4. How to use and tune state-of-the-art sequence-to-sequence models, including transformers.
5. How to process speech signals.

All lectures are hosted on Youtube and can be consumed at your own pace (see links below). At the end of (most) every lecture there is a tutorial + homework assignment that will demonstrate how to perform NLP tasks in Python. The Python Notebooks are available through the links below, and in the `Homework` folder.


### Introduction
- <u>Lectures:</u> 
  - a. [Introduction to the Course](https://youtu.be/-4OsuTi8OkE) 
  - b. [Overview of Syllabus](https://youtu.be/92gDHHGmJeo) 
  - c. [Overview of Course Tools](https://youtu.be/xGNys9rDEsQ)
  - d. [Overview of the Course Project](https://youtu.be/Jmdo5YjPIOo)
- **HW0:** [Setting up your notebook and Gitlab Repo](homework/HW0/Instructions.md)
- **Project:** [Guidelines](project/Instructions.md)


### NLP Fundamentals and N-gram Language Models
- <u>Optional Readings</u>:
  - [Chapter 2](https://web.stanford.edu/~jurafsky/slp3/2.pdf) and [Chapter 3](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- <u>Lecture:</u> 
  - [Introduction](https://youtu.be/lwzyB0zendM)
  - a. [Language and its properties](https://youtu.be/662hOEPxEVo)
  - b. [Regular Expressions](https://youtu.be/Xv51Z73yaYU) 
  - c. [Text Normalization](https://youtu.be/aFUXV7-WUFM) 
  - d. [Edit Distance](https://youtu.be/SNEZ5beES-k) 
  - e. [N-gram Language Models](https://youtu.be/P3d7D78Cj1E) 
  - f. [Generalization and Smoothing](https://youtu.be/vpJ_Iw63cFU)
  - [HW1 Tutorial](https://youtu.be/JdtuvnOhCZM)
- **HW1 and Code Tutorial:** [Basic data manipulations, representations and statistics](homework/HW1/assignment.ipynb)


### Niave Bayes, Sentiment Classification, Logistic Regression
- <u>Optional Readings</u>:
  - [Chapter 4](https://web.stanford.edu/~jurafsky/slp3/4.pdf) and [Chapter 5](https://web.stanford.edu/~jurafsky/slp3/5.pdf)
- <u>Lecture:</u> 
  - [Introduction](https://youtu.be/nmVSwvhQAtM) 
  - [Overview](https://youtu.be/wCKpJNKcyGU)
  - a. [Numerical Representations of Text](https://youtu.be/qzYouqf45sQ)
  - b. [Naive Bayes](https://youtu.be/TlNjXaI7F_M)
  - c. [Logistic Regression](https://youtu.be/TbjUaZLhJVc)
  - d. [Performance Metrics](https://youtu.be/wfJk_9xRGNc)
  - [HW2 Tutorial](https://youtu.be/xVf1vcIeqVI)
- **HW2 and Code Tutorial:** [Supervised language classification models and their assessment](homework/HW2/assignment.ipynb)


### Vector Semantics, Embeddings, Neural Language Models
- <u>Optional Readings</u>
  - [Chapter 6](https://web.stanford.edu/~jurafsky/slp3/6.pdf) and [Chapter 7](https://web.stanford.edu/~jurafsky/slp3/7.pdf)
  - [PCA](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)
  - [Word2Vec](https://lilianweng.github.io/lil-log/2017/10/15/learning-word-embedding.html)
- <u>Lecture:</u> 
  - [Introduction](https://youtu.be/OC-JQimrkAs)
  - [Overview](https://youtu.be/Nfw8Yjo-kis)
  - a. [Simple Contextual Representations](https://youtu.be/LGJSZCvBT3g)
  - b. [Gradient Descent](https://youtu.be/pfJimE8ed-g)
  - c. [Neural Networks](https://youtu.be/9EjCkNLJvs4)
  - d. [Neural Langauge Models](https://youtu.be/y4zDz3MwrEw)
  - [HW3 Tutorial](https://youtu.be/JLX-2X7gb8o)
- **HW3 and Code Tutorial:** [Embeddings and Neural Networks](homework/HW3)


### Modeling Text as a Sequence
- <u>Optional Readings</u>
  - [Chapter 8](https://web.stanford.edu/~jurafsky/slp3/8.pdf) and [Chapter 9](https://web.stanford.edu/~jurafsky/slp3/9.pdf)
- <u>Lecture:</u>  
  - [Overview](https://youtu.be/5Hjf1c9_icQ)
  - [Introduction](https://youtu.be/VtZjvQhXy1w)
  - a. [Hidden Markov Models](https://youtu.be/7ak1_zDUgEg)
  - b. [Maximum Entropy Markov Models](https://youtu.be/FtXRkzLKnpQ)
  - c. [Recurrent Neural Networks](https://youtu.be/RMLW-BKy-lk)
  - [HW4 Tutorial](https://youtu.be/-jP8vuzsid4)
- **HW4 and Code Tutorial:**  [Sequence Models](homework/HW4)
  

### Encoder-Decoder Models, Attention and Transformers
- <u>Optional Readings</u>
  - [Chapter 10](https://web.stanford.edu/~jurafsky/slp3/10.pdf), [Viswani, 2017](https://arxiv.org/pdf/1706.03762.pdf)
- <u>Lecture</u>: 
  - [Overview](https://youtu.be/m3d7MERBSrc) 
  - [Introduction](https://youtu.be/aJ9AR9NQG1E)
  - a. [Encoder-Decoder Networks](https://youtu.be/Xe8Y1emJlMk)
  - b. [Attention](https://youtu.be/DZgHT1jsjeE)
  - c. [Transformers](https://youtu.be/GyC1lVT3Urw)
  - [HW5 Tutorial](https://youtu.be/WD14dradNrY)
- **HW5 and Code Tutorial:** [Transformers](homework/HW5)
   
   
### Constituencies, Parsing and Dependency
- <u>Optional Readings</u>
  - [Chapter 12](https://web.stanford.edu/~jurafsky/slp3/12.pdf), [Chapter 13](https://web.stanford.edu/~jurafsky/slp3/13.pdf), [Chapter 14](https://web.stanford.edu/~jurafsky/slp3/14.pdf), [Chapter 15](https://web.stanford.edu/~jurafsky/slp3/15.pdf)
- <u>Lecture</u>: 
  - [Overview](https://youtu.be/pXTrY2GPMn0)
  - [Introduction](https://youtu.be/El4r91dgCTQ)
  - a. [Context Free Grammar](https://youtu.be/kq4aUYzLlb0)
  - b. [Constituency Parsing](https://youtu.be/_OpOoiySZRA)
  - c. [Statistical Consituency Parsing](https://youtu.be/avmq_oVGOOM)
  - d. [Dependency Parsing](https://youtu.be/2jLk93iIyrw)
- **HW6 and Code Tutorial:** [Context free grammar](homework/HW6)


### Speech Processing
- <u>Optional Readings</u>
  - [Chapter 27](https://web.stanford.edu/~jurafsky/slp3/27.pdf)
- <u>Lecture</u>: 
  - [Overview](https://youtu.be/yZ-3fF9ECGk)
  - [Introduction](https://youtu.be/6L1XBid5aws)
  - a. [Phonetics](https://youtu.be/y8kEwd2DJNw)
  - b. [Speech Signals](https://youtu.be/RPHRxRS_wbY)
  - [HW7 Tutorial](https://youtu.be/29P7q84xGls)
- **HW7 and Code Tutorial:** [Speech Analysis](homework/HW7)
