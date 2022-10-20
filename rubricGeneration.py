import numpy as np
import pandas as pd
import math  

def grade(score1, score2):
    grade100 = (((.65 * score1) + (.35 * score2))/(.65 * 9 + .35 * 6)) * 100
    grade15 = (((.65 * score1) + (.35 * score2))/(.65 * 9 + .35 * 6)) * 10
    return grade100

xRange = np.arange(0, 9, .3)
yRange = np.arange(0, 6, .2)

gradeOutput = [[x,y] for x in xRange for y in yRange]
for i in range(len(gradeOutput)):
    gradeOutput[i] = [gradeOutput[i][0], gradeOutput[i][1], grade(gradeOutput[i][0], gradeOutput[i][1])]

completeData = pd.DataFrame(gradeOutput, columns=['9-Point-Scale', '6-Point-Scale', 'Grade'])
completeData.to_csv('data.csv', index=False)

