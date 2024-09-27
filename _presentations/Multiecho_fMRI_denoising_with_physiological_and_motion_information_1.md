---
title: "Multi-echo fMRI denoising with physiological and motion information"
project_id: multi_echo
date: 2022-06-01
conference_id: "OHBM_2022"
presenters:
   - micah_holness
   - daniel_handwerker
   - joshua_teves
   - tyler_morgan
   - javier_gonzalez-castillo
   - peter_bandettini
summary: "<p>Multi-echo denoising removes non-T2* and therefore non-BOLD time series fluctuations. This includes scanner artifacts and head motion. However, breathing related BOLD changes are not removed.</p>

<p>We use the multi-echo ICA denoising method implemented in tedana and additionally removed ICA components that are correlated with head motion, cardiac, and respiratory fluctuations. Our hypothesis was that this additional ICA removal process would help eliminate artifactual BOLD and maintain higher statistical degrees of freedom.</p>"
file: /assets/presentations/Holness_OHBM_final.pdf
filename: Holness_OHBM_final.pdf
layout: presentation
---