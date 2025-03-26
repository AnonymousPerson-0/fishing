WIDTH = 800
HEIGHT = 600

probabilities = {0 : [0.7, 0.9, 1]}
fishByStage = {0 : ["Normal Fish", "Rare Fish", "Elongated Fish"]}

objects = {"Normal Fish": ["Your average fish.", 2, "Fish", "NONE"], 
           "Rare Fish": ["Slightly more valuable fish.", 5, "Fish", "NONE"],
           "Elongated Fish":["A fish that contains a valuable medicinal ingredient that can be used to cure PNEUMONIA or help treat CORRUPTION.", 10, "Key Fish", "Can be sacrificed."]
}
# each array is [string descriptor, value, category, effects]
storeRects = [[0, 0, WIDTH, HEIGHT], [WIDTH - 50, 0, 50, 50]] # topleft x, y, w, h
scenes = [[[], [], []], []] # Array of arrays containing arrays denoting the different scenes in the different phases.
