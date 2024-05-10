from head_movements.compute_head_movement_tuples import compute_head_movement_tuples
from head_movements.convert_tuples_to_curves import convert_tuples_to_curves
from head_movements.add_durations import add_durations
from head_movements.integrate_head_movements import integrate_head_movements
from head_movements.add_eyebrow_movements import add_eyebrow_movements
# from head_movements.calculate_eye_stabilisations import calculate_eye_stabilisations


def orchestrate_head_movement_curves(segments):
    mov_tups = compute_head_movement_tuples(segments)
    all_visemes = convert_tuples_to_curves(mov_tups)
    alvs = add_durations(all_visemes)
    int_alvs = integrate_head_movements(alvs)
    its = add_eyebrow_movements(int_alvs, "happy")
    return its
