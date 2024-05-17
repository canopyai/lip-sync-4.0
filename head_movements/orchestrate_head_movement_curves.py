from head_movements.compute_head_movement_tuples import compute_head_movement_tuples
from head_movements.convert_tuples_to_curves import convert_tuples_to_curves
from head_movements.add_durations import add_durations
from head_movements.integrate_head_movements import integrate_head_movements
from head_movements.interpolate_with_easing import interpolate_with_cumulative_easing
from head_movements.add_eyebrow_movements import add_eyebrow_movements
# from head_movements.calculate_eye_stabilisations import calculate_eye_stabilisations


def orchestrate_head_movement_curves(segments):
    mov_tups = compute_head_movement_tuples(segments)
    all_visemes = convert_tuples_to_curves(mov_tups)
    all_visemes_copy = all_visemes.copy()
    alvs = all_visemes
    
    alvs = add_durations(alvs)
    # print("add_durations", alvs)
    

    # print("interpolate_with_cumulative_easing", len(alvs))
    
    int_alvs = integrate_head_movements(alvs)
    print("int_alvs", int_alvs)
    # int_alvs = interpolate_with_cumulative_easing(int_alvs) 
    # print("integrate_head_movements", len(int_alvs))

   

    alvs_copy = add_durations(all_visemes_copy)
    int_alvs_copy = integrate_head_movements(alvs_copy)
    int_alvs_copy = add_eyebrow_movements(int_alvs_copy, "happy")
    return int_alvs, int_alvs_copy
