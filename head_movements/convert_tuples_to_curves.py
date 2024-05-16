import random


def convert_tuples_to_curves(tuples):
  visemes=[]
  polarisations = [random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1])]
  for tup in tuples:

    start, strength = tup

    weights_array = [0]*6
    selections = [random.randint(0, 1) for _ in range(3)]
    weights = [random.uniform(0, 0.25) for _ in range(2)]

    # Generate one random number between 0.75 and 1
    weights.append(random.uniform(0.75, 1))

    polarisations = [_*-1 for _ in polarisations]
    magnitude = random.uniform(0.1, 0.5)

    weights = [x * magnitude * polarisations[i] for i, x in enumerate(weights)]

    # Shuffle the list twice
    random.shuffle(weights)
    random.shuffle(weights)

    if(selections[0]==0):
      weights_array[0] = weights[0]
    else:
      weights_array[1] = weights[0]

    if(selections[1]==0):
      weights_array[2] = weights[1]
    else:
      weights_array[3] = weights[1]

    if(selections[2]==0):
      weights_array[4] = weights[2]
    else:
      weights_array[5] = weights[2]

    vis_dict = {
        "deltas":[_ * strength for _ in weights_array],
        "start":start
    }

    visemes.append(vis_dict)

  return visemes
