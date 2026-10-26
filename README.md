# LAMP2A_VS_LAMP2B_and_LAMP2C

# **Isoform-specific stabilization of LAMP2A oligomers provides a structural basis for chaperone-mediated autophagy**

---

## Overview

This repository contains molecular dynamics (MD) simulation datasets for three isoforms of lysosome-associated membrane protein 2, **LAMP2A, LAMP2B, and LAMP2C**, in both monomeric and trimeric forms.

For each isoform, simulations were performed for monomeric systems and trimeric wild-type and mutant variants within a biologically relevant lysosomal membrane environment. Independent replicas were generated to ensure reproducibility and robust statistical sampling, with production trajectories extending to **1,000 ns per replica**, where applicable.

Each replica includes the initial structure (`initial.pdb`) obtained after equilibration, the final structure (`trj_final.pdb`), and the corresponding production trajectory (`trj.xtc`). The repository also provides GROMACS topology files, simulation parameter files, and analysis scripts.

All simulations were performed using **GROMACS** under consistent simulation protocols, providing a framework for comparing the structural and dynamical behavior of the three LAMP2 isoforms across different oligomeric states and variants.

---

## **Study Highlights**

- **Three LAMP2 isoforms:** LAMP2A, LAMP2B, and LAMP2C.
- **Oligomeric states:** Monomeric and trimeric systems.
- **Wild-type and mutant variants:** Comparative analysis of trimeric assemblies.
- **Long-timescale simulations:** Production trajectories extending to 1,000 ns per replica, where applicable.
- **Independent replicas:** Multiple simulation replicas to support reproducibility and statistical analysis.
- **Free-energy calculations:** Umbrella sampling along a selected reaction coordinate.
- **Membrane-associated analysis:** Characterization of protein–lipid interactions, trimer cavity properties, lipid insertion, and protein orientation.

---

## **Repository Contents**

### **1. Structural and Trajectory Files**

- **`initial.pdb`**: Initial structure of the protein embedded in the lipid bilayer after equilibration, used to initiate the production simulation.

- **`trj_final.pdb`**: Final structure of the system after the production molecular dynamics simulation.

- **`trj.xtc`**: Compressed GROMACS trajectory containing time-dependent molecular coordinates.

- **`system.tpr`**: Compiled GROMACS run input file generated using `gmx grompp`, containing simulation parameters, topology information, and starting coordinates.

### **2. Molecular Topology Files**

- **`topol.top`**: Main GROMACS topology file defining the molecular composition of the system and including the required force-field and molecular topology files.

- **`forcefield.itp`**: Force-field include file defining the force-field parameters and settings required for the molecular system.

- **`BMGP.itp`, `CHL1.itp`, `CLA.itp`, `LSM.itp`, `PLPC.itp`, `PLPE.itp`, `PROA.itp`, `PROB.itp`, `PROC.itp`, `PSM.itp`, `SAPC.itp`, `SAPE.itp`, `SAPI.itp`, `SAPS.itp`, `SDPC.itp`, `SDPI.itp`, `SDPS.itp`, `SOD.itp`, and `TIP3.itp`**: GROMACS topology include files defining the molecular topology of the corresponding molecular species and system components. These files provide atom types, bonded interactions, and other relevant topology parameters, as applicable, and are included in `topol.top`.

### **3. Molecular Dynamics Parameter Files (`.mdp`)**

The repository includes separate molecular dynamics parameter files for standard MD simulations and umbrella sampling.

#### **Standard Molecular Dynamics — `Standard_MD/`**

- **`step_minimization.mdp`**: Defines the parameters for energy minimization to optimize the initial system geometry and relieve unfavorable atomic contacts.

- **`step1.1_equilibration.mdp` – `step1.6_equilibration.mdp`**: Define the parameters for sequential equilibration stages used to stabilize the system before production simulation.

- **`step_production.mdp`**: Specifies the simulation parameters for the production molecular dynamics run.


#### **Umbrella Sampling — `Umbrella_Sampling_MD/`**

- **`equilibration_umbrella.mdp`**: Defines the equilibration parameters for the umbrella sampling windows before production sampling.

- **`pull.mdp`**: Specifies the pulling parameters used to generate configurations along the selected reaction coordinate.

- **`production_umbrella.mdp`**: Defines the production simulation parameters for individual umbrella windows used to collect sampling data for subsequent potential of mean force (PMF) calculations.

---

## **Simulation Details**

The simulation datasets are organized by LAMP2 isoform, oligomeric state, and variant. Each replica represents an independent simulation run.

### **LAMP2A System**

#### **Monomer**
- `Replica_1`
- `Replica_2`
- `Replica_3`

#### **Trimer — Wild Type**
- `Replica_1`
- `Replica_2`
- `Replica_3`
- `Replica_4`
- `Replica_5`

#### **Trimer — Mutant**
- `Replica_1`
- `Replica_2`
- `Replica_3`

### **LAMP2B System**

#### **Monomer**
- `Replica_1`
- `Replica_2`
- `Replica_3`

#### **Trimer — Wild Type**
- `Replica_1`
- `Replica_2`
- `Replica_3`
- `Replica_4`
- `Replica_5`

#### **Trimer — Mutant**
- `Replica_1`
- `Replica_2`
- `Replica_3`

### **LAMP2C System**

#### **Monomer**
- `Replica_1`
- `Replica_2`
- `Replica_3`

#### **Trimer — Wild Type**
- `Replica_1`
- `Replica_2`
- `Replica_3`
- `Replica_4`
- `Replica_5`

#### **Trimer — Mutant**
- `Replica_1`
- `Replica_2`
- `Replica_3`

---

## **Analysis Tools**

- **GROMACS**: Molecular dynamics simulations and trajectory analysis.
- **VMD**: Molecular visualization and Tcl-based structural analysis.
- **UCSF ChimeraX**: Molecular structure visualization and inspection.
- **DSSP**: Protein secondary-structure assignment.
- **Python**: Custom trajectory analysis and quantitative data processing.

---

## **Analysis Scripts**

- **`tilt_angle_analysis.tcl`**: VMD Tcl script for analyzing the protein trimer tilt angle relative to the membrane plane or a defined reference axis.

- **`trimer_cavity_and_lipid_insertion_analysis.py`**: Python script for analyzing the trimer cavity and lipid insertion, enabling characterization of lipid penetration and cavity-associated structural features during molecular dynamics simulations.

---

## **Objective and Scientific Significance**

This study systematically compares the monomeric and trimeric assemblies of **LAMP2A, LAMP2B, and LAMP2C** to investigate the structural determinants that may contribute to isoform-specific chaperone-mediated autophagy (CMA).

Using **33 μs of all-atom molecular dynamics simulations**, umbrella sampling-based free-energy calculations, and computational protein redesign, we investigate differences in oligomeric stability, protein–lipid interactions, and trimer-associated structural features across the three isoforms.

The findings indicate that **LAMP2A exhibits a greater propensity to form stable trimeric assemblies than LAMP2B and LAMP2C**, providing a structural framework for investigating the molecular determinants of LAMP2 isoform specificity in CMA.

---

## **Reproducibility and Data Usage**

1. Select the relevant LAMP2 isoform, oligomeric state, variant, and simulation replica.
2. Use the corresponding molecular structures, topology files, force-field dependencies, and `.mdp` parameter files.
3. Ensure that a compatible version of **GROMACS** is installed.
4. Use the provided trajectories and analysis scripts to perform structural and dynamical analyses.

> **Note:** The `.mdp` files specify simulation settings, whereas the `.tpr` file contains compiled simulation inputs generated during GROMACS preprocessing. The `.xtc` file contains trajectory coordinates and may require an appropriate structure or topology file for analysis.

