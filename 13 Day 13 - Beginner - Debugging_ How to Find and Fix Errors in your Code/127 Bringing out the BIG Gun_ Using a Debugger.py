############DEBUGGING#####################

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # this line was out of indent in for-loop
  print(b_list)

mutate([1,2,3,5,8,13])