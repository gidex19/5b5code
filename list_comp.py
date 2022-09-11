

scores = [20, 30, 40, 50, 60]

# new_scores = [ j + 10  for i,j in enumerate(scores) if i == 4 ]
new_scores = [score + 20  for score in scores if score< 60  ]
print(new_scores)


# names =["micheal jackson", "michael jordan", "wizkid", "davido"]
# create a new list from the list above using list comprehension such
#  that its value will be "i love" + the current value of the previous list


