---
title: "NORDIC denoising on VASO data"
date: 2025-01-05
authors_string: Lasse Knudsen, Luca Vizioli, Federico De Martino, Lonike K. Faes, Daniel Handwerker, Steen Moeller, Peter Bandettini, Laurentius Huber
authors:
   - Lasse Knudsen
   - Luca Vizioli
   - Federico De Martino
   - Lonike K. Faes
   - Daniel Handwerker
   - Steen Moeller
   - Peter Bandettini 
   - Laurentius Huber
author_ids:
   - daniel_handwerker
   - peter_bandettini
   - laurentius_huber
journal: 'Frontiers in Neuroscience'
volume: 18
issue: 
pages: 1499762
book_title: ''
publisher: ''
abstract: "<p>The use of submillimeter resolution functional magnetic resonance imaging (fMRI) is increasing in popularity due to the prospect of studying human brain activation non-invasively at the scale of cortical layers and columns. This method, known as laminar fMRI, is inherently signal-to-noise ratio (SNR)-limited, especially at lower field strengths, with the dominant noise source being of thermal origin. Furthermore, laminar fMRI is challenged with signal displacements due to draining vein effects in conventional gradient-echo blood oxygen level-dependent (BOLD) imaging contrasts. fMRI contrasts such as cerebral blood volume (CBV)-sensitive vascular space occupancy (VASO) sequences have the potential to mitigate draining vein effects. However, VASO comes along with another reduction in detection sensitivity. NOise Reduction with DIstribution Corrected (NORDIC) PCA (principal component analysis) is a denoising technique specifically aimed at suppressing thermal noise, which has proven useful for increasing the SNR of high-resolution functional data. While NORDIC has been examined for BOLD acquisitions, its application to VASO data has been limited, which was the focus of the present study. We present a preliminary analysis to evaluate NORDIC’s capability to suppress thermal noise while preserving the VASO signal across a wide parameter space at 3T. For the data presented here, with a proper set of parameters, NORDIC reduced thermal noise with minimal bias on the underlying signal and preserved spatial resolution. Denoising performance was found to vary with different implementation strategies and parameter choices, for which we provide recommendations. We conclude that when applied properly, NORDIC has the potential to overcome the sensitivity limitations of laminar-specific VASO fMRI. Since very few groups currently have 3T VASO data, by sharing our analysis and code, we can compile and compare the effects of NORDIC across a broader range of acquisition parameters and study designs. Such a communal effort will help develop robust recommendations that will increase the utility of laminar fMRI at lower field strengths.</p>"
project_id: layer_fmri
paper_url: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1499762/full
doi: 10.3389/fnins.2024.1499762
data_loc: 'https://layerfmri.page.link/ME_VASO3T'
code_loc: 'https://github.com/LasseKnudsen1/NORDIC-VASO'
file: '/assets/publications//assets/publications/'
file_name: '/assets/publications/'
type: journal_article
pub_str: ' (2025) Frontiers in Neuroscience 18:1499762'
layout: publication 
---