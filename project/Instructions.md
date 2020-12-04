# Project Instructions

The course project is your opportunitiy to independently demonstrate your mastery of the course materials on an NLP problem that you find interesting. Your project will culminate in a Final Report that should be about 2,000 words in length, and be structured simmilarly to an academic paper. Ideally, you should be able to submit your project as a paper by the end of semester, or sometime shortly thereafter. [Here are some example projects.](ExampleProjects.md)



## Part 1:  Data Collection, Write Introduction
In the first part of the project, you will develop an NLP related research question you would like to answer, and collect a natural langugage dataset of some kind that will help you answer that question. By the end of part 1, you should have:

1. A well articulated research problem
2. A dataset you will use to answer the problem
3. A Python notebook with a preliminary exploration of the data, and its characteristics
4. A draft of your final paper's Introduction section

##### When writing your draft of the introduction, be sure to answer the following questions:

1. Motivate the reader for why they should care about the specific problem you will go on to solve: Does the problem cost a lot of money? Do people lose their lives? Does solving the problem provide an amazing opportunity to make money, change an industry?
2. Speak about the general class of problems that your specific problem belongs to (e.g. match-making is a recommendation problem). 
3. What are the latest and greatest approaches to solve the specific problem? How about the general problem? Summarize a few papers (1-2 sentences each) describing their approach to these problems.
4. What is the shortcoming of the existing solutions to the problem? How can these shortcoming be addressed? Where are there opportunities for improving how the problem is currently solved?
5. Introduce your solution(s). Say specifically how it advances, solves the problems of, or has advantages over, the current approaches. Convince them this what they're about to read is a good idea.

## Part 2: Model Development, Write Methods
In the second part of the project, you will apply a method to answer the research question you posed in the first part of the project. By the end of part 2, you should have:

1. A data pre-processing pipeline
2. A trained model
3. A Python notebook you used to pre-process, train, and assess your model 
4. A draft of your final paper's Methods section. 

##### When writing your draft of the method's section, be sure to answer the following questions:

1. Data collection approach: How was the data collected? Where was it collected from? What kind of information was collected, be specific? What components of the data that you've collected are the "outputs" you're going to predict, and what are the "input" you're going to use to predict the "outputs"? Who generated those outputs?
2. Data pre-processing approach: Describe the approach you used to transform the raw data you collected into a clean detest that could be used for analysis later. Describe your inclusion or exclusion criteria; when did you throw data out versus choose to keep it?  Do you provide a copy of the pre-processed data to people; if so, how do people access it?
3. Feature Extraction: Describe any features you extracted from the data, or transformation you performed on the data. For instance, did you dummy code your categorical variables? Did you z-score the continuous measures?  
4. Modeling Approach: Describe the modeling approach you're using to predict the "outputs" using the "inputs". Describe how your method works (in math, psudocode, or English, whichever is most appropriate). Call out links to external source code. If you're using a DNN approach, or any model with hyper-parameters, describe and justify how you selected the settings of the hyper-parameters. 
5. Baselines: Describe each of the baselines that you will be comparing your approach against. How exactly will you be comparing your performance against the baselines (AUC, Accuracy, fscore, etc., calibration)? Why is your performance metric the correct metric?  
6. Describe your validation approach: How big was your training/dev/test set? Did you do cross validation; how many folds? 

## Part 3: Comparing against baselines, Write Results
In the third part of the project, you will compare your method against an alternative approach and discuss the pros and cons of your approach compared to the baseline. By the end of part 3, you should have:

1. One or more figures/tables that illustrate your method's results on an experiment.
2. A Python notebook with the baseline method implemented and compared against your approach
3. A draft of your final paper's Results section. 

##### When writing your draft of the result's section, be sure to answer the following questions:

1. Describe the characteristics of the data you collected. How many unique rows? How many unique columns? What are the characteristics of the outcome? Do you notice any interesting simple relationships in the data. Provide any plots or tables that will help people understand the characteristics of the data you collected, at a glance. 
2. Compare the performance of your proposed methods against the baselines according to the performance metrics you choose in the methods section. Present these results in a table or a figure. Discuss the table/figure, and verbally highlight important results, or comparisons between results presented in the table/figure. 
3. Interpret your model: If your model is interpretable, interpret it. Discuss which "input" features had the strongest and/or weakest impact on the "output".
4. Illustrative example: Show your model working on a flattering example from the data, or doing something cool to show off your work. 

## Part 4: Combine, Polish and Write Discussion
In the fourth part of the project, you  generate visualizations that illustrate the pros and cons of your approach, and discuss future directions of your work. By the end of part 4, you should have:

1. A completed draft of your final report, including a discussion section
2. A well organized code repository that allows one to regenerate all results described in your report

##### When writing your draft of the discussion section, be sure to answer the following questions:

1. Summarize the problem you were trying to solve, and how your main results prove you solved that problem. Theorize about why you think your method did better than the baselines.
2. Talk about if/how your findings in this work might generalize to the general problem domain, or another problem domain.
3. Talk about anything that the reviewer might see as a weaknesses or limitation of your work and defend your work against those limitations.
4. Describe the appropriate next steps for the work. Extensions, possibilities, etc.
 Conclude by summarizing what you were trying to accomplish with the paper, and what you did in fact accomplish at the end.

## CODE AND DATA REPOSITORY REQUIREMENTS
Your work should contain an accompanying code and data repository that may be used by others to easily reporduce your work. That is, people should be able to run your software, and re-generate all the code, data and analysis you presented in the final report.
