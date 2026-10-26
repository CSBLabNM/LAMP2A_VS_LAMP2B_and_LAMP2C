import MDAnalysis as mda
import numpy as np
import pandas as pd

from scipy.spatial import Delaunay
from collections import defaultdict

############################################################
# USER INPUT
############################################################

PDB = "trj.pdb"
XTC = "trj.xtc"

LIPID_NAMES = [
    "PLPC",
    "SAPC",
    "SDPC",
    "PLPE",
    "SAPE",
    "SAPI",
    "SDPI",
    "SAPS",
    "SDPS",
    "PSM",
    "LSM",
    "CHL1",
    "BMGP"
]

GRID_SPACING = 1.0
PADDING = 5.0

############################################################
# LOAD
############################################################

u = mda.Universe(PDB, XTC)

############################################################
# TRIMER SELECTION
############################################################

CA_SEL = """
(segid A and resid 10:32 and name CA) or
(segid B and resid 52:74 and name CA) or
(segid C and resid 94:116 and name CA)
"""



############################################################
# OUTPUT STORAGE
############################################################

lipid_events = []

occupancy_summary = []

residence_counter = defaultdict(int)

############################################################
# SNAPSHOT FRAMES
############################################################

snapshot_frames = set([
    0,
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800
])

############################################################
# MAIN LOOP
############################################################

for ts in u.trajectory:

    frame = ts.frame

    print(f"Processing frame {frame}")

    ########################################################
    # BUILD CAVITY
    ########################################################

    ca = u.select_atoms(CA_SEL)

    coords = ca.positions

    tri = Delaunay(coords)

    xmin, ymin, zmin = coords.min(axis=0) - PADDING
    xmax, ymax, zmax = coords.max(axis=0) + PADDING

    x = np.arange(xmin, xmax, GRID_SPACING)
    y = np.arange(ymin, ymax, GRID_SPACING)
    z = np.arange(zmin, zmax, GRID_SPACING)

    grid = np.array(
        np.meshgrid(x, y, z)
    ).T.reshape(-1, 3)

    inside = tri.find_simplex(grid) >= 0

    cavity_points = grid[inside]

    cavity_volume = len(cavity_points) * GRID_SPACING**3

    ########################################################
    # SAVE SNAPSHOTS
    ########################################################

    if frame in snapshot_frames:

        print(f"Saving cavity snapshot for frame {frame}")

        ####################################################
        # PROTEIN + LIPID PDB
        ####################################################

        system_sel = (
            "protein or resname "
            + " ".join(LIPID_NAMES)
        )

        system_atoms = u.select_atoms(system_sel)

        system_atoms.write(
            f"system_frame_{frame}.pdb"
        )

        ####################################################
        # CAVITY PDB
        ####################################################

        with open(
            f"cavity_frame_{frame}.pdb",
            "w"
        ) as f:

            for i, p in enumerate(
                cavity_points,
                start=1
            ):

                f.write(
                    "HETATM{:5d}  CAV CAV A{:4d}    "
                    "{:8.3f}{:8.3f}{:8.3f}  1.00  0.00\n".format(
                        i,
                        i,
                        p[0],
                        p[1],
                        p[2]
                    )
                )

            f.write("END\n")

    ########################################################
    # LIPID PENETRATION
    ########################################################

    lipids_inside_this_frame = set()

    for residue in u.residues:

        if residue.resname not in LIPID_NAMES:
            continue

        atom_positions = residue.atoms.positions

        simplex = tri.find_simplex(
            atom_positions
        )

        inside_atoms = np.where(
            simplex >= 0
        )[0]

        if len(inside_atoms) == 0:
            continue

        ####################################################
        # FIRST ATOM INSIDE
        ####################################################

        first_idx = inside_atoms[0]

        atom = residue.atoms[first_idx]

        lipid_events.append([
            frame,
            residue.resname,
            residue.resid,
            atom.name,
            atom.index,
            cavity_volume
        ])

        lipids_inside_this_frame.add(
            (
                residue.resname,
                residue.resid
            )
        )

        residence_counter[
            (
                residue.resname,
                residue.resid
            )
        ] += 1

    ########################################################
    # OCCUPANCY SUMMARY
    ########################################################

    occupancy_summary.append([
        frame,
        len(lipids_inside_this_frame),
        cavity_volume
    ])

############################################################
# WRITE CSV FILES
############################################################

events_df = pd.DataFrame(
    lipid_events,
    columns=[
        "frame",
        "lipid_name",
        "lipid_resid",
        "first_atom_inside",
        "atom_index",
        "cavity_volume_A3"
    ]
)

events_df.to_csv(
    "lipid_events.csv",
    index=False
)

occupancy_df = pd.DataFrame(
    occupancy_summary,
    columns=[
        "frame",
        "n_lipids_inside",
        "cavity_volume_A3"
    ]
)

occupancy_df.to_csv(
    "occupancy_timeseries.csv",
    index=False
)

############################################################
# RESIDENCE TABLE
############################################################

residence_rows = []

for key, count in residence_counter.items():

    resname, resid = key

    residence_rows.append([
        resname,
        resid,
        count
    ])

residence_df = pd.DataFrame(
    residence_rows,
    columns=[
        "lipid_name",
        "lipid_resid",
        "total_frames_inside"
    ]
)

residence_df.to_csv(
    "lipid_residence.csv",
    index=False
)

############################################################
# VOLUME TABLE
############################################################

volume_df = occupancy_df[
    ["frame", "cavity_volume_A3"]
]

volume_df.to_csv(
    "cavity_volume.csv",
    index=False
)

############################################################
# DONE
############################################################

print("\nAnalysis complete\n")

print("Generated files:")
print("  lipid_events.csv")
print("  occupancy_timeseries.csv")
print("  lipid_residence.csv")
print("  cavity_volume.csv")
print("  system_frame_*.pdb")
print("  cavity_frame_*.pdb")
