# ======================================
# Chain A
# TM1 = resid 378 to 381
# TM2 = resid 397 to 400
# Output = tilt_angle_chainA.dat
# ======================================

set mol_id 0
set numframes [molinfo $mol_id get numframes]

set output_TM [open "tilt_angle_chainA.dat" w]

for {set frame 0} {$frame < $numframes} {incr frame} {

    set p_TM1 [atomselect $mol_id "protein and chain A and resid 378 to 381" frame $frame]
    set c_TM1 [measure center $p_TM1 weight mass]

    set p_TM2 [atomselect $mol_id "protein and chain A and resid 397 to 400" frame $frame]
    set c_TM2 [measure center $p_TM2 weight mass]

    set ax_TM [vecsub $c_TM2 $c_TM1]
    set lax_TM [veclength $ax_TM]

    set k {0 0 1}

    set dot_TM [vecdot $ax_TM $k]
    set cos_TM [expr {$dot_TM/$lax_TM}]
    set ang_rad_TM [expr {acos($cos_TM)}]
    set ang_deg_TM [expr {$ang_rad_TM*180.0/acos(-1)}]

    puts $output_TM "$frame $ang_deg_TM"

    $p_TM1 delete
    $p_TM2 delete
}

close $output_TM


# ======================================
# Chain B
# TM1 = resid 378 to 381
# TM2 = resid 397 to 400
# Output = tilt_angle_chainB.dat
# ======================================

set output_TM [open "tilt_angle_chainB.dat" w]

for {set frame 0} {$frame < $numframes} {incr frame} {

    set p_TM1 [atomselect $mol_id "protein and chain B and resid 378 to 381" frame $frame]
    set c_TM1 [measure center $p_TM1 weight mass]

    set p_TM2 [atomselect $mol_id "protein and chain B and resid 397 to 400" frame $frame]
    set c_TM2 [measure center $p_TM2 weight mass]

    set ax_TM [vecsub $c_TM2 $c_TM1]
    set lax_TM [veclength $ax_TM]

    set k {0 0 1}

    set dot_TM [vecdot $ax_TM $k]
    set cos_TM [expr {$dot_TM/$lax_TM}]
    set ang_rad_TM [expr {acos($cos_TM)}]
    set ang_deg_TM [expr {$ang_rad_TM*180.0/acos(-1)}]

    puts $output_TM "$frame $ang_deg_TM"

    $p_TM1 delete
    $p_TM2 delete
}

close $output_TM


# ======================================
# Chain C
# TM1 = resid 378 to 381
# TM2 = resid 397 to 400
# Output = tilt_angle_chainC.dat
# ======================================

set output_TM [open "tilt_angle_chainC.dat" w]

for {set frame 0} {$frame < $numframes} {incr frame} {

    set p_TM1 [atomselect $mol_id "protein and chain C and resid 378 to 381" frame $frame]
    set c_TM1 [measure center $p_TM1 weight mass]

    set p_TM2 [atomselect $mol_id "protein and chain C and resid 397 to 400" frame $frame]
    set c_TM2 [measure center $p_TM2 weight mass]

    set ax_TM [vecsub $c_TM2 $c_TM1]
    set lax_TM [veclength $ax_TM]

    set k {0 0 1}

    set dot_TM [vecdot $ax_TM $k]
    set cos_TM [expr {$dot_TM/$lax_TM}]
    set ang_rad_TM [expr {acos($cos_TM)}]
    set ang_deg_TM [expr {$ang_rad_TM*180.0/acos(-1)}]

    puts $output_TM "$frame $ang_deg_TM"

    $p_TM1 delete
    $p_TM2 delete
}

close $output_TM
