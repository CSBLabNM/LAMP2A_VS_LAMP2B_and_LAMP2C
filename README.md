# LAMP2A_VS_LAMP2B_and_LAMP2C
# **Isoform-specific stabilization of LAMP2A oligomers provides a structural basis for chaperone-mediated autophagy**
# Overview
This repository contains molecular dynamics (MD) simulation datasets for three isoforms of Lysosome-Associated Membrane Protein, **LAMP2A**, **LAMP2B**, and **LAMP2C**, in both their monomeric and trimeric forms. For each system, simulations were performed for the monomer as well as the trimeric wild-type (WT) and mutant (Mut) variants within a biologically relevant lysosomal membrane environment. Independent replicas were generated for every simulation to ensure reproducibility and robust statistical sampling with trajectories extending to 1000 ns per replica. Each replica contains the initial structure (.pdb), the final structure (.pdb) and the corresponding production trajectory (.xtc). All simulations were performed using GROMACS under identical simulation protocols, providing a consistent framework for comparing the structural and dynamical behavior of the three systems across different monomeric and trimeric states and variants. This repository is organized to facilitate reproducible analysis and straightforward comparison between systems, simulation replicas, and structural forms.

# **Repository Contents**

# File Description
- **initial.pdb** (The initial structure of protein embedded in a lipid bilayer obtained after equilibration, used for production simulation.)
- **trj_final.pdb** (The final structure of the system after 1000 ns MD simulation.)
- **trj.xtc** (Compressed trajectory file containing the simulation trajectory.)

- # Simulation Details
## System A

### Monomer

- rep1
- rep2
- rep3

### Trimer

#### WT

- rep1
- rep2
- rep3

#### Mut

- rep1
- rep2
- rep3


- # **LAMP2A System**
- #   **Monomer**
- #      **Replica_1** 
- #      **Replica_2** 
- #      **Replica_3** 
------**Trimer**
          **Wild Type**
           **Replica_1** 
           **Replica_2** 
           **Replica_3** 
           **Replica_4**
           **Replica_5**
------**Trimer**
          **Mutant Type**
           **Replica_1** 
           **Replica_2** 
           **Replica_3** 

- # **LAMP2B System**
------**Monomer**
       **Replica_1** 
       **Replica_2** 
       **Replica_3** 
------**Trimer**
          **Wild Type**
           **Replica_1** 
           **Replica_2** 
           **Replica_3** 
           **Replica_4**
           **Replica_5**
------**Trimer**
          **Mutant Type**
           **Replica_1** 
           **Replica_2** 
           **Replica_3** 

- # **LAMP2C System**
------**Monomer**
       **Replica_1** 
       **Replica_2** 
       **Replica_3** 
------**Trimer**
          **Wild Type**
           **Replica_1** 
           **Replica_2** 
           **Replica_3** 
           **Replica_4**
           **Replica_5**
------**Trimer**
          **Mutant Type**
           **Replica_1** 
           **Replica_2** 
           **Replica_3**            
             


