---
title: "Manifold Learning for fMRI time-varying FC"
date: 2023-07-10
authors_string: Javier Gonzalez-Castillo, Isabel Fernandez, Ka Lam, Daniel Handwerker, Francisco Pereira, Peter Bandettini
authors:
   - Javier Gonzalez-Castillo
   - Isabel Fernandez
   - Ka Lam
   - Daniel Handwerker
   - Francisco Pereira
   - Peter Bandettini
author_ids:
   - javier_gonzalez-castillo
   - isabel_fernandez
   - daniel_handwerker
   - peter_bandettini
journal: 'Frontiers in Human Neuroscience'
volume: 17
issue: 
pages: 
book_title: ''
publisher: ''
abstract: "Whole-brain functional connectivity (FC) measured with functional MRI (fMRI) evolves over time in meaningful ways at temporal scales going from years (e.g., development) to seconds [e.g., within-scan time-varying FC (tvFC)]. Yet, our ability to explore tvFC is severely constrained by its large dimensionality (several thousands). To overcome this difficulty, researchers often seek to generate low dimensional representations (e.g., 2D and 3D scatter plots) hoping those will retain important aspects of the data (e.g., relationships to behavior and disease progression). Limited prior empirical work suggests that manifold learning techniques (MLTs) - namely those seeking to infer a low dimensional non-linear surface (i.e., the manifold) where most of the data lies - are good candidates for accomplishing this task. Here we explore this possibility in detail. First, we discuss why one should expect tvFC data to lie on a low dimensional manifold. Second, we estimate what is the intrinsic dimension (ID; i.e., minimum number of latent dimensions) of tvFC data manifolds. Third, we describe the inner workings of three state-of-the-art MLTs: Laplacian Eigenmaps (LEs), T-distributed Stochastic Neighbor Embedding (T-SNE), and Uniform Manifold Approximation and Projection (UMAP). For each method, we empirically evaluate its ability to generate neuro-biologically meaningful representations of tvFC data, as well as their robustness against hyper-parameter selection. Our results show that tvFC data has an ID that ranges between 4 and 26, and that ID varies significantly between rest and task states. We also show how all three methods can effectively capture subject identity and task being performed: UMAP and T-SNE can capture these two levels of detail concurrently, but LE could only capture one at a time. We observed substantial variability in embedding quality across MLTs, and within-MLT as a function of hyper-parameter selection. To help alleviate this issue, we provide heuristics that can inform future studies. Finally, we also demonstrate the importance of feature normalization when combining data across subjects and the role that temporal autocorrelation plays in the application of MLTs to tvFC data. Overall, we conclude that while MLTs can be useful to generate summary views of labeled tvFC data, their application to unlabeled data such as resting-state remains challenging."
project_id: bold_connectivity_dynamics
paper_url: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2023.1134012/full
doi: 10.3389/fnhum.2023.1134012
data_loc: ''
code_loc: 'https://github.com/nimh-sfim/manifold_learning_fmri'
file: '/assets/publications/'
file_name: ''
type: journal_article
pub_str: ' (2023) Frontiers in Human Neuroscience 17'
layout: publication 
---