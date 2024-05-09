def add_durations(all_visemes):
  visemes = [{
      "duration":all_visemes[0]["start"],
      "deltas":[0]*6
  }]
  for i, v in enumerate(all_visemes):
    if i < len(all_visemes)-1:
      visemes.append({
          "duration":all_visemes[i+1]["start"] - v["start"],
          "deltas":v["deltas"]
      })


  return visemes
