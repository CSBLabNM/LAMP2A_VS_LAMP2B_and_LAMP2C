# LAMP2A_VS_LAMP2B_and_LAMP2C
# **Isoform-specific stabilization of LAMP2A oligomers provides a structural basis for chaperone-mediated autophagy**
# Overview
This repository contains molecular dynamics (MD) simulation datasets for three isoforms of Lysosome-Associated Membrane Protein, **LAMP2A**, **LAMP2B**, and **LAMP2C**, in both their monomeric and trimeric forms. For each system, simulations were performed for the monomer as well as the trimeric wild-type and mutant variants within a biologically relevant lysosomal membrane environment. Independent replicas were generated for every simulation to ensure reproducibility and robust statistical sampling with trajectories extending to 1000 ns per replica. Each replica contains the initial structure (.pdb) obtained after equilibration, the final structure (.pdb) and the corresponding production trajectory (.xtc). All simulations were performed using GROMACS under identical simulation protocols, providing a consistent framework for comparing the structural and dynamical behavior of the three systems across different monomeric and trimeric states and variants. This repository is organized to facilitate reproducible analysis and straightforward comparison between systems, simulation replicas, and structural forms.

# **Repository Contents**

# File Description
- **initial.pdb** (The initial structure of protein embedded in a lipid bilayer obtained after equilibration, used for production simulation.)
- **trj_final.pdb** (The final structure of the system after 1000 ns MD simulation.)
- **trj.xtc** (Compressed trajectory file containing the simulation trajectory.)
- **topol.top** (GROMACS topology file defining the molecular composition, force-field parameters, and topology include files required for the simulation.)
- **system.tpr** (Compiled GROMACS run input file generated using gmx grompp, containing the simulation parameters, topology information, and starting coordinates required to run the simulation.)
- **forcefiled.itp** (Force-field include file defining the force-field parameters and settings required for the molecular system.)
- **BMGP.itp, CHL1.itp, CLA.itp, LSM.itp, PLPC.itp, PLPE.itp, PROA.itp, PROB.itp, PROC.itp, PSM.itp, SAPC.itp, SAPE.itp, SAPI.itp, SAPS.itp, SDPC.itp, SDPI.itp, SDPS.itp, SOD.itp, and TIP3.itp** (GROMACS topology include files defining the molecular topology of the corresponding lipid species, protein components, ions, and water model present in the simulated system. These files provide the relevant atom types, bonded interactions, and other topology parameters, as applicable, and are included in topol.top to describe the molecular composition of the system.)
- ### Molecular Dynamics Parameter Files (`.mdp`)

- **`Standard_MD/`**: Contains the GROMACS molecular dynamics parameter files used for energy minimization, system equilibration, and production simulations.
  - **`step_minimization.mdp`**: Defines the parameters for energy minimization to optimize the initial system geometry and relieve unfavorable atomic contacts.
  - **`step1.1_equilibration.mdp` – `step1.6_equilibration.mdp`**: Define the parameters for the sequential equilibration stages used to stabilize the system before production simulation.
  - **`step_production.mdp`**: Specifies the simulation parameters for the production molecular dynamics run.
  - **`mdout.mdp`**: Contains the processed molecular dynamics parameters generated during GROMACS preprocessing.

- **`Umbrella_Sampling_MD/`**: Contains the GROMACS parameter files used for umbrella sampling simulations to investigate the free-energy profile along a selected reaction coordinate.
  - **`equilibration_umbrella.mdp`**: Defines the equilibration parameters for the umbrella sampling windows before production sampling.
  - **`pull.mdp`**: Specifies the pulling parameters used to generate configurations along the selected reaction coordinate for umbrella sampling.
  - **`production_umbrella.mdp`**: Defines the production simulation parameters for collecting sampling data in individual umbrella windows for subsequent potential of mean force (PMF) calculations.

- # Simulation Details
## LAMP2A System

### Monomer
- Replica_1
- Replica_2
- Replica_3

### Trimer

#### Wild Type
- Replica_1
- Replica_2
- Replica_3
- Replica_4
- Replica_5

#### Mutant

- Replica_1
- Replica_2
- Replica_3


## LAMP2B System

### Monomer
- Replica_1
- Replica_2
- Replica_3

### Trimer

#### Wild Type
- Replica_1
- Replica_2
- Replica_3
- Replica_4
- Replica_5

#### Mutant

- Replica_1
- Replica_2
- Replica_3


## LAMP2C System

### Monomer
- Replica_1
- Replica_2
- Replica_3

### Trimer

#### Wild Type
- Replica_1
- Replica_2
- Replica_3
- Replica_4
- Replica_5

#### Mutant

- Replica_1
- Replica_2
- Replica_3

- # Analysis Tools

- **GROMACS** (Trajectory analysis)

- **VMD/ChimeraX/PyMOL** (Structural visualization)

- **PyLipID** (Lipid interaction analysis)

- **DSSP** (Secondary structure analysis)

- **python** (Trajectory analysis)

- ### Analysis Scripts

- **`tilt_angle_analysis.tcl`**: VMD Tcl script for analyzing the protein trimer tilt angle relative to the membrane plane or a defined reference axis.

- **`trimer_cavity_and_lipid_insertion_analysis.py`**: Python script for analyzing the trimer cavity and lipid insertion, enabling the characterization of lipid penetration and cavity-associated structural features during molecular dynamics simulations.

# Objective and Significance
This study systematically compare the monomeric and trimeric assemblies of all three LAMP2 isoforms to elucidate the structural basis of CMA specificity. Using 33 μs of all-atom molecular dynamics simulations, free-energy calculations based on umbrella sampling, and computational protein redesign approach, we demonstrate that LAMP2A exhibits a significantly greater propensity to form stable trimeric assemblies compared to the LAMP2B and LAMP2C.

