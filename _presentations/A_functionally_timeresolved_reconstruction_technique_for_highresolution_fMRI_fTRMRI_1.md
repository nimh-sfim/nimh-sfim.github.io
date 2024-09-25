---
title: "A functionally time-resolved reconstruction technique for high-resolution fMRI (fTR-MRI)"
project_id: 
date: 2023-11-01
conference_id: "SFN_2023"
presenters:
   - tyler_morgan
   - isabel_gephart
   - daniel_handwerker
   - javier_gonzalez-castillo
   - peter_bandettini
summary: "<p>Functional MRI (fMRI) with sub-millimeter spatial resolution is a promising technique to probe the human brain’s mesoscopic scale [1,2]. However, typical spatial resolutions remain too coarse to sample individual human columnar and laminar structures. Moreover, high-resolution fMRI measurements using echo-planar trajectories (EPI) and blood oxygen-dependent (BOLD) contrast suffer from spatial distortions and T2* blurring due to long readout trains. Recently, time-resolved reconstruction methods have alleviated some of these issues by keeping track of the timing of data acquisition in reference to signal properties [3] or physiological cycles [4]. We utilize this conceptual framework to time resolve data with respect to events in a neuroscience experiment. The current work, which we call functionally time-resolved MRI (fTR-MRI), has high spatial resolution (0.5 mm) and is not affected by phase-encoding distortions yet reconstructs brain responses with reasonable temporal resolution (400 ms).<br />
We acquired data from 3 participants (2 male) on a Siemens MAGNETOM 7T+ with a Nova 32-channel head coil. We collected a multi-echo 2D-GRE sequence (TR=31 ms, TEs=[4.22, 8.38, 12.54, 16.7, 20.86, 25.02] ms, slice thickness=0.8 mm, matrix=360x270, no acceleration or Partial Fourier). Acquisition times were tracked for each k-space line by sending an external trigger to a stimulation computer. The experimental paradigm consisted of a 10 Hz flashing radial checkerboard presented for 2 s (15 s ISI). We reconstructed data via low-rank tensor completion [5] with modes for k-space, receivers, echoes, and experimental response time. The resulting reconstruction depicts brain responses from -2 to 32 seconds after stimulus presentation with 6 echoes.<br />
Primary visual cortex displayed a prominent dip in T2* decay times in middle layers, allowing us to identify infra- and supra-granular layers. Functional responses peaked between 2.5 and 3 s after the short stimulus presentation and superficial layers showed larger peak response and post-stimulus undershoot amplitudes, as reported in rodent studies [6].<br />
The fTR-MRI reconstruction method incorporates experimental designs into the image reconstruction process to capture high spatial and temporal resolution brain responses. These features expand the arsenal of tools available to non-invasively examine mesoscopic responses in the human brain.<br />
[1] M. Moerel, et al., J. Neurosci. 2018<br />
[2] E. Finn, et al., Prog Neurobiol. 2021<br />
[3] F. Wang et al., Magn. Reson. Med. 2019<br />
[4] A.G. Christodoulou et al., Nat. Biomed. Eng. 2018<br />
[5] M.A.O. Vasilescu, University of Toronto Thesis. 2009<br />
[6] P. Tian et al., Proc. Natl. Acad. Sci. 2010</p>
"
file: /assets/presentations/Morgan_SFN2023.pdf
filename: Morgan_SFN2023.pdf
layout: presentation
---