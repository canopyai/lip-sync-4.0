def get_eyebrow_selection_movement(emotion):
  if (emotion == "happy"):
    return [0,0.8,0,0.8]
  elif (emotion == "neutral"):
    return [0.7,0,0,0]
  elif (emotion == "sad"):
    return [1,0,0,0]
  elif (emotion == "fear"):
    return [1,0,0,0]
  elif (emotion == "excitement"):
    return [1,0,0,0]
  elif (emotion == "disgust"):
    return [1,0,0,0]
  elif (emotion == "concerned"):
    return [1,0,0,0]
  elif (emotion == "angry"):
    return [0,0,0.8,0]