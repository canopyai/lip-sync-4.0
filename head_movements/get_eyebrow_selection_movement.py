def get_eyebrow_selection_movement(emotion):
  if (emotion == "happy"):
    return [1,0,0,0]
  elif (emotion == "neutral"):
    return [0.7,0,0,0]
  elif (emotion == "sad"):
    return [0,0,1,0]
  elif (emotion == "fear"):
    return [0,0,0.5,0.5]
  elif (emotion == "excitement"):
    return [1,0,0,0]
  elif (emotion == "disgust"):
    return [0,0.3,0,0.7]
  elif (emotion == "concerned"):
    return [0,0,0.8,0.3]
  elif (emotion == "angry"):
    return [0,0,0.8,0.3]