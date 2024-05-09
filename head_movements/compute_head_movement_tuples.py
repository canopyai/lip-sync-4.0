def compute_head_movement_tuples(segments):
  head_movement_tuples = []
  first_segment_start = segments[0]['start']
  first_segment_end = segments[0]['end']

  first_segment_start_tuple = (first_segment_start, 0.5)
  second_segment_start_tuple = (first_segment_end, 0.25)

  head_movement_tuples.append(first_segment_start_tuple)
  head_movement_tuples.append(second_segment_start_tuple)

  index_of_stress = math.ceil(len(segments)/2)

  mid_tuple = (segments[index_of_stress]["start"], 0.7)
  head_movement_tuples.append(mid_tuple)

  remaining_indices = [i for i in range(len(segments))]
  remaining_indices.remove(0)
  remaining_indices.remove(1)
  remaining_indices.remove(index_of_stress)

  selected_list = [index for index in remaining_indices if random.random() < 2/5]

  for i in selected_list:
    sel = segments[i]
    head_movement_tuples.append((sel["start"], random.uniform(0.1, 0.25)))

  head_movement_tuples.sort(key=lambda x: x[0])


  return head_movement_tuples