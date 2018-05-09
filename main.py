import cmath
numberOfPoints=int(input("Please Input Number Of Points:\n"))
if(numberOfPoints==0 or numberOfPoints == 1 or numberOfPoints % 2 != 0):
  print("No solution")
  exit()
if(numberOfPoints ==2):
  print("Solution is radius: 0, with a center at either point")
  exit()
def getPointInput():
  tmpString = input("Please input 'x y' coordinate:\n")
  xy=[]
  
  xy.append(float(tmpString.split()[0]))
  xy.append((float(tmpString.split()[1])))
  return xy
#Input: P1 & p2 are x,y coordinates in an array  
def getCenterPoint(p1,p2):
  centerX=((p1[0]+p2[0])/2)
  centerY=((p1[0]+p2[0])/2)
  return [centerX,centerY]
def isPointInCircle(point,centerPoint,radius):
  pointDistance = getRadius(centerPoint,point)
  if(pointDistance<=radius):
    return True
  else:
    return False
def getRadius(centerPoint,point):
  dist =cmath.sqrt(((point[1]-centerPoint[1])**2)+((point[0]-centerPoint[0])**2)).real
  return dist
points=[]

availablePoints=[]
while(len(points)<numberOfPoints):
  points.append(getPointInput())
#getcircles with two points on edges

for point1index in range(0,len(points)-1):
  for point2index in range(point1index,len(points)):
    circleCenterPoint = getCenterPoint(points[point1index],points[point2index])
    radius = getRadius(points[point1index],circleCenterPoint)
    pointsInside=0
    for point in points:
      if(isPointInCircle(point,circleCenterPoint,radius)):
        pointsInside+=1
      else:
        pointsInside-=1
    if(pointsInside==0):
      availablePoints.append([radius,circleCenterPoint])
      
print(availablePoints)

#Make sure circles are in the square
toRemove=[]
for pointIndex in reversed(range(0,len(availablePoints))):
  centerPoint=availablePoints[pointIndex][1]
  radius=availablePoints[pointIndex][0]
  if(centerPoint[0]-radius<0 or centerPoint[0]+radius>1 or centerPoint[1]-radius<0 or centerPoint[1]+radius>1):
    del(availablePoints[pointIndex])

#get the smallest radius
if(len(availablePoints)==0):
  print("No Solution")
else:
  minPoint=availablePoints[0]
  for point in availablePoints:
    if point[0]<minPoint[0]:
      minPoint=point
  print(minPoint)
  print("The Smallest Radius Circle is:"+str(minPoint[0]))
  print("At [X,Y]:"+str(minPoint[1]))
