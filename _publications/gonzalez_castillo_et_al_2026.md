---
title: "A new fMRI quality metric using multi-echo information: Theory, validation and implications"
date: 2026-03-23
authors_string: Javier Gonzalez-Castillo, César Caballero-Gaudes , Daniel Handwerker, Peter Bandettini
authors:
   - Javier Gonzalez-Castillo
   - César Caballero-Gaudes 
   - Daniel Handwerker
   - Peter Bandettini
author_ids:
   - javier_gonzalez-castillo
   - daniel_handwerker
   - peter_bandettini
journal: 'BioRxiv'
volume: 
issue:
pages: 
book_title: ''
publisher: ''
abstract: "Consistent, high-quality data is key to the success of fMRI studies given the many confounding factors and undesired signals that contaminate these data. Several quality assurance (QA) metrics exist for fMRI (e.g., temporal signal-to-noise ratio (TSNR), percent ghosting, motion estimates), but none of them leverage relationships between echoes that are part of multi-echo (ME) fMRI acquisitions. Here, we fill this gap by proposing a new QA metric for for ME-fMRI that quantifies the likelihood a given ME scan is dominated by BOLD (Blood Oxygenation Level-Dependent) fluctuations. We refer to this metric as pBOLD; the probability of the signal change being primarily BOLD contrast-dominated. Having an estimate of overall BOLD weighting – both before and after preprocessing - is meaningful because BOLD is the intrinsic contrast mechanism used in fMRI to infer neural activity. We introduce pBOLD to the neuroimaging community by first describing the theoretical principles supporting the metric. Next, we validate pBOLD efficacy using a small dataset (N=7 scans) of constant- and cardiac-gated scans that have distinct levels of contributing BOLD fluctuations. Third, we apply pBOLD to a larger publicly available ME dataset (N=439 scans), to evaluate six different pre-processing pipelines, and show how pBOLD provides complementary information to TSNR. Our results show that ME-based denoising increases both pBOLD and TSNR relative to basic denoising; however, including the global signal (GS) as a regressor only improves TSNR, but worsens pBOLD. Further analyses looking at the BOLD-like characteristics of the GS and its relationship to cardiac and respiratory traces suggest that the observed decrease in pBOLD is likely due to a decrease in BOLD fluctuations of neural origin contributing to the GS, and not due to contributions from other physiological BOLD fluctuations (i.e., respiratory and cardiac function). Finally, we also demonstrate how pBOLD can be applied as a data quality metric, by showing how higher pBOLD results in better ability to predict phenotypes based on whole-brain functional connectivity matrices."
project_id: multi_echo
paper_url: https://www.biorxiv.org/content/10.64898/2026.03.19.712948v1
doi: https://doi.org/10.64898/2026.03.19.712948
data_loc: ''
code_loc: 'https://github.com/nimh-sfim/me_staticfc'
file: '/assets/publications/'
file_name: ''
type: journal_article
pub_str: ' (2026) BioRxiv'
layout: publication 
---