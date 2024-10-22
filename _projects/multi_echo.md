---
title: "Multi-Echo fMRI"
project_id: multi_echo
short_summary: "Multi-echo fMRI acquires data at multiple echo times following each radio-frequency excitation pulse.
Measurements of how signals change across echoes can be used to better isolate the Blood Oxygen Level Dependent (BOLD) signal that is relevant to most fMRI studies.
We develop, validate, and distribute methods to better isolate BOLD signal with the goal of improving fMRI data quality."
summary: "<p>For MRI, there is a radio-frequency excitation pulse and then a period where signal is read.
The duration between the excitation pulse and the center of the readout period is the echo time (TE).
In many MRI studies, there is a single TE.
This TE is set by the experimenter to to weight various factors of interest,
which can be maximizing the contrast between gray and matter for structural imaging,
or maximizing the Blood Oxygen Level Dependent (BOLD) contrast that is often used in fMRI.
For BOLD fMRI, we typically set TE to be as close as possible to the T2* decay value for gray matter.
For example a typical fMRI study on a 3T scanner, might acquire a single volume every 2 seconds with TE=28ms.
A weakness of this approach is that other factors can affect the optimal TE for BOLD and undesired signals are also included for any given TR.</p>

<p>With multi-echo fMRI, for every excitation pulse, the same readout period is repeated as many times as possible before the next excitation pulse.
That means, for each 2 seconds of acqusition, one could acquire three volumes with TE=(14ms, 28ms, and 42ms).
By collecting multiple echoes, one can estimate the optimal TE for each voxel and use examine who signal changes across echoes to better isolate signal that is likely to be BOLD weighted.</p>

<h2>1. Methods development</h2>

<p>Prior to SFIMs work with multi-echo fMRI (<a href='https://doi.org/10.1002/(SICI)1522-2594(199907)42:1<87::AID-MRM13>3.0.CO;2-O'>[Posse et al. 1999]</a>
and <a href='https://doi.org/10.1002/mrm.20900'>[Poser et al. 2006]</a>) developed methods to take the weighed average of all echoes to benefit from a
better estimate of T2* and improve data quality.
This approach, sometimes called 'Optimal Combination,' produces a decrease in signal dropout and increase in the contrast-to-noise ratio (CNR).
In SFIM, Prantik Kundu led work to develop a method that separates data into ICA components and the fits each component to models of T2* and S0 signals.
Components that fit S0 signals, but not T2* signals were more likely to be artifacts, from the scanner or from head motion, which would be regressed from the data.
This approach takes advantage of the physics underlying signal changes across echoes to identify noise.
(<a href='/publications/kundu_et_al_2012_0.md'>[Kundu et al. 2012]</a> and 
<a href='/publications/kundu_et_al_2013_0.md'>[Kundu et al. 2013]</a>).</p>

<p>The following image is from a review paper (<a href='/publications/kundu_et_al_2017_0.md'>[Kundu et al. 2017]</a>)
that shows example ICA components that fit well to a T2* (kappa) model (top row) and S0 (rho) model (bottom row).
For this example, the lower row component would be regressed from the data as noise.
<img src='/assets/images/Kundu2017_Fig8.jpg', alt='Example ICA components for T2* kappa weighting and S0 rho weighting. Figure 8 from Kundu 2017'></p>


<p>Continued work in SFIM has evaluated and expanded this ICA-based denoising approach.
<a href='/publications/evans_et_al_2015_0.md'>[Evans et al. 2015]</a> shows that multi-echo denoising has the potential to separate slow neural changes from other slow changes, like scanner signal drift.
In single-echo fMRI, it is common to remove all slow drifts, which are assumed to be noise, which makes it difficult to study slow changes such as in studies of learning or studies that use pharmaceutical drugs.
<a href='/publications/gonzalez-castillo_et_al_2016_0.md'>[Gonzalez-Castillo et al. 2016]</a> evaluates multi-echo denoise across multiple task designs to show that it is an effective tool for improving signal in small regions with high suseptability to cardiac pulsations, like the inferior colliculus.
Cardiac gating us common for other MRI scans that benefit from synchronizing MRI acqusition with specific phases of the cardiac cycle, but it is rare with fMRI because variable spacing between volume aqusitions creates large artifacts. The above study shows that multi-echo denoising can remove these artifacts so that gated methods are possible with fMRI.</p>

<p>In addition to the ICA-based methods, we have collaborated with César Caballero-Gaudes' group to use multi-echo information to identify sparse peaks in fMRI series that are more likely to be neural in origin (<a href='/publications/caballero-gaudes_et_al_2019_0.md'>[Caballero-Gaudes et al. 2019]</a> and <a href='/publications/urunuela_et_al_2024.md'>[Uruñuela  et al. 2024]</a>).
These methods can be used to identify timings of neural events, like cognitive state changes with no additional assumptions or measures of participant behavior.</p>

<p>Ongoing work includes efforts to combine multi-echo ICA denoising methods with other ICA denoising methods that fit data to signals such as head motion, cardiac or respiratory fluctuations, or CSF signals. We are evaluating these methods both for event-related task designs (<a href='/presentations/Multiecho_fMRI_denoising_with_physiological_and_motion_information_1.md'>[Holness et al. 2022]</a>) and naturalistic movie viewing (<a href='/presentations/Multiecho_fMRI_removes_physiological_noise_during_naturalistic_viewing_1.md'>[Holness et al. 2023]</a>).
We are also testing ways to alter ICA component estimation so that each component more purely contains BOLD or non-BOLD signals (<a href='/presentations/Moving_away_from_ICA_in_multiecho_fMRI_denoising_1.md'>[Handwerker et al. 2018]</a>).</p>


<h2>2. Software and Education</h2>

<p>As we develop methods, we are also helping to distribute robust software and educational materials so these methods are widely available to the research community.
This work centers on contributing to <a href='/_publications/dupre_et_al_2021_0'>tedana</a> which is both software and
<a href='https://tedana.readthedocs.io/en/stable/multi-echo.html'>educational resources</a> to help people better understand multi-echo fMRI and methods.
Recent enhancements to the tedana software includes better recording of how the algorithm processes each dataset and a way for anyone to modify
the ICA component selection process to fit specific needs or improve the overall method (<a href='/presentations/tedana_A_growing_multiecho_fMRI_ecosystem_1.md'>[tedana team 2023]</a>)
and new ways to fit external time series to the components so that head motion and cardiac or respiratory fluctuations can be fully integrated into the component selection process
(<a href='/presentations/tedana_Multiecho_fMRI_noise_removal_software_and_resources_1.md'>[tedana team 2024]</a>).</p>"
status: current
layout: project
---
