---
title: "Evaluating the predictive power of dynamic fMRI connectivity summary statistics"
project_id: bold_connectivity_dynamics
date: 2023-11-01
conference_id: "SFN_2023"
presenters:
   - megan_spurney
   - josh_faskowitz
   - javier_gonzalez-castillo
   - daniel_handwerker
   - peter_bandettini
summary: "<p>Brain-behavior models often use resting-state fMRI data in the form of functional connectivity (FC) matrices, where each entry corresponds to the correlation between time series for a pair of regions (or nodes). This useful approach is limited in that a typical FC matrix is unable to capture the changes of connectivity that the brain experiences during a typical time series duration. To access precise dynamic connectivity information, we generated a time series for each node pair (or edge) that captured how the two nodes co-fluctuate from moment to moment (i.e., edge time series) (Zamani Esfahlani, 2020). Here, we explore multiple approaches to summarizing fMRI connectivity dynamics using resting-state fMRI scans from the NKI-Rockland sample (N=971, 59.4% Female, ages 6-85). In addition to the mean of the edge time series, which is equivalent to the more standard FC, we also computed the standard deviation, entropy, and several other time-dependent measures, to form new matrices for each subject. We then evaluated the predictive ability of these alternative brain representations using Connectome-Based Predictive Modeling. We produced significant predictions for measures of attention and intelligence, respectively, through a general linear model, using the edge time series mean (r=0.26, p&lt;0.001; r=0.35, p&lt;0.001), standard deviation (r=0.15, p&lt;0.01; r=0.11, p&lt;0.01), and entropy (r=0.22, p&lt;0.001; r=0.29, p&lt;0.001). Next, we predicted attention and intelligence using a ridge regression model that included these three representations of the data. This model performed better than our individual models for attention (r=0.31, p&lt;0.0001) and intelligence (r=0.43, p&lt;0.0001). We found that, across fitting iterations, the model framework repeatedly selected the mean of the edge time series in building these predictions, suggesting that the mean (or the FC) is relatively most predictive. Finally, we computed several other temporally sensitive summary metrics, including autocorrelation and dynamic entropy. Their predictive value proved to be not as significant as that of the mean of edge time series. In sum, our results demonstrated that mean co-fluctuation, i.e., functional connectivity, showed significant predictive power that was unmatched compared to a variety of other summary statistics, suggesting perhaps, that what the brain is doing over 10 minute periods is more predictive of traits than the specific dynamics of how it changes from moment to moment. Future work will focus on exploring spatial and temporal aspects of these edge time series that may either be more predictive of traits or more informative of the functional organization of the brain.</p>
"
file: /assets/presentations/Spurney_SFNPoster23_FINAL_sm.pdf
filename: Spurney_SFNPoster23_FINAL_sm.pdf
layout: presentation
---