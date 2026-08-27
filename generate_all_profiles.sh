#!/bin/bash
set -e

# CGMES profiles
cgmes_profiles=(
  core_equipment
  diagram_layout
  equipment_boundary
  geographical_location
  operation
  short_circuit
  state_variables
  steady_state_hypothesis
  topology
)

# Norwegian profiles
norwegian_profiles=(
  aviation_obstacle
  grid_capacity
  subsea_cable_info
)

for profile in "${cgmes_profiles[@]}"; do
  echo "=== Generating $profile (CGMES) ==="
  cim4 docs gen -s "$profile" -g "CGMES" --svg
done

for profile in "${norwegian_profiles[@]}"; do
  echo "=== Generating $profile (Norwegian Profiles) ==="
  cim4 docs gen -s "$profile" -g "Norwegian Profiles" --svg
done

echo "=== All profiles generated ==="
