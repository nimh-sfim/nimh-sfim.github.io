---
title: "Layer Specific fMRI"
project_id: layer_fmri
short_summary: "We are working to improve the spatial resolution and specificity of fMRI so that it is possible to distinguish neural activity changes across cortical layers."
summary: "<p>We are working to improve the spatial resolution and specificity of fMRI so that it is possible to distinguish neural activity changes across cortical layers and better understand the mechanisms of mesoscale activity.</p>
 
<h2>1. Patch Analysis</h2>
<p>Cerebral blood volume (CBV) weighted fMRI with sub millimeter resolution has been shown to resolve layer specific brain activity. Most of the layer studies are focused on reporting depth dependent activity patterns so called layer profiles. However, those profiles are very dynamic in time and averaging them across time may mislead the interpretation of feedback and feedforward activity patterns. Here we propose a patch analysis, which focuses both depth and time information of a given cortical patch. This not only helps direct viewing of profile changes in time, but it also allows several different analysis approaches like ranking feedback and feed forwardness, capturing time instances of a specific layer in time in each cortical patch.</p>

<img src='assets/images/layerfMRI_1.jpg', alt='Layer fMRI, Figure 1'>
<p>Figure 1). Sample patch analysis of an index finger area to a tactile stimulation.
A) Instantaneous CBV patterns of right index finger area, B) Patch representation of the depth dependent activity C) three main Centroids of the K-Means clustering. D) Cluster indices of every instantaneous layer profile, yellow for upper, blue for middle, red for deeper. Also, blue arrows indicating the time of tactile stimuli introduced to the index finger</p>

<h2>2. Layer Regional Homogeneity (ReHo)</h2>
<p>Cerebral blood volume (CBV) weighted fMRI with sub millimeter resolution has been shown to resolve layer specific brain activity. However rigorous processing pipelines are needed to localize the depth dependent activity. Here we propose a simple tool to characterize mesoscale structure by using local connectivity patterns. It is model free and fast tool for exploring any layer data given only the depth of the voxels, also the regions Layer ReHo highlights are in line with the task dependent activity.</p>

<img src='assets/images/layerfMRI_2.jpg', alt='Layer fMRI, Figure 2'>

<p>Figure 2; An example of Layer dependent ReHo (Regional Homogeneity) calculation. Time courses are extracted from the same laminar bin and correlation coefficients across all pairs are calculated. A square matrix with a size of the number of voxels is averaged for each column. This gives a coefficient or in other words weight of that voxel to the laminar bin which is given to the voxel as a ReHo value.</p>

<img src='assets/images/layerfMRI_3.jpg', alt='Layer fMRI, Figure 3'>
<p>Figure 2; Comparison of Layer ReHo maps with average CBV changes to tactile stimuli
A) Regional homogeneity of four different finger areas higher values showing more homogeneous pattern B) average CBV change in finger areas are shown in percent signal change</p>"
status: current
layout: project
---
