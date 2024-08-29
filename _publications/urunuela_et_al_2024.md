---
title: "Whole-brain multivariate hemodynamic deconvolution for multi-echo fMRI with stability selection"

date: 1/1/24
authors_string: Eneko Uruñuela, Javier Gonzalez-Castillo, Charles Zheng, Peter Bandettini, Cesar Caballero-Gaudes
authors:
   - Eneko Uruñuela
   - Javier Gonzalez-Castillo
   - Charles Zheng
   - Peter Bandettini
   - Cesar Caballero-Gaudes
author_ids:
   -  javier_gonzalezcastillo
   - peter_bandettini
journal: 'Medical Image Analysis'
volume: 92.0
issue: 
pages: 
book_title: ''
publisher: ''
isbn: 
abstract: 'Conventionally, analysis of functional MRI (fMRI) data relies on available information about the experimental paradigm to establish hypothesized models of brain activity. However, this information can be inaccurate, incomplete or unavailable in multiple scenarios such as resting-state, naturalistic paradigms or clinical conditions. In these cases, blind estimates of neuronal-related activity can be obtained with paradigm-free analysis methods such as hemodynamic deconvolution. Yet, current formulations of the hemodynamic deconvolution problem have three important limitations: 1) their efficacy strongly depends on the appropriate selection of regularization parameters, 2) being univariate, they do not take advantage of the information present across the brain, and 3) they do not provide any measure of statistical certainty associated with each detected event. Here we propose a novel approach that addresses all these limitations. Specifically, we introduce MvME-SPFM (multivariate multi-echo sparse paradigm free mapping), a novel hemodynamic deconvolution algorithm that operates at the whole brain level and adds spatial information via a mixed-norm regularization term over all voxels. Additionally, MvME-SPFM employs a stability selection procedure that removes the need to select regularization parameters and also lets us obtain an estimate of the true probability of having a neuronal-related BOLD event at each voxel and time-point based on the area under the curve (AUC) of the stability paths. Besides, the formulation is tailored for multi-echo fMRI acquisitions, which allows us to better isolate fluctuations of BOLD origin on the basis of their linear dependence with Echo Time (TE) and to assign physiologically interpretable units (i.e., changes in the apparent transverse relaxation ) to the resulting deconvolved events. We demonstrate that this algorithm outperforms existing state-of-the-art deconvolution approaches, and shows higher spatial and temporal agreement with the activation maps and BOLD signals obtained with a standard model-based linear regression approach, even at the level of individual neuronal events. Consequently, the proposed algorithm provides more reliable estimates of neuronal-related activity, here in terms of , for the study of the dynamics of brain activity when no information about the timings of the BOLD events is available. This algorithm will be made publicly available as part of the splora Python package.'
project_id: 
paper_url: https://www.sciencedirect.com/science/article/pii/S1361841523002700
doi: 10.1016/j.media.2023.103010
data_loc: ''
code_loc: ''
file: '/assets/publications/'
file_name: ''
type: journal_article
pub_str: 'Medical Image Analysis (1/1/) 92'
layout: publication 
---