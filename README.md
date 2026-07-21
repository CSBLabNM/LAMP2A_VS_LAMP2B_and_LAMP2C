# LAMP2A_VS_LAMP2B_and_LAMP2C
# **Isoform-specific stabilization of LAMP2A oligomers provides a structural basis for chaperone-mediated autophagy**
# Overview
This repository contains molecular dynamics (MD) simulation datasets for both monomeric and homotrimeric assemblies of the human Lysosome-Associated Membrane Protein 2A (LAMP2A). The simulations encompass wild-type (WT) systems in which histidine residues at positions 402–404 were modeled in either their neutral (0) or protonated (+1) states, yielding five distinct protonation combinations: 1000, 1100, 1010, 1001, and 1111. In addition, an inactive mutant variant of LAMP2A was simulated within a biologically relevant lysosomal membrane environment.
Each system was subjected to microsecond-scale MD simulations: three replicas for the trimeric assemblies and two replicas for the monomeric systems, with trajectories extending to 1000 ns per replica. All simulations were performed using GROMACS, enabling detailed investigation of the structural and dynamical consequences of the protonation states and the mutation on LAMP2A stability and function.

# **Repository Contents**

# File Description
- **initial.pdb** (The initial structure of protein embedded in a lipid bilayer, used for simulation.)
- **final.pdb** (The final structure of the system after 1000 ns MD simulation.)
- **trj.xtc** (Compressed trajectory file containing the simulation trajectory.)
