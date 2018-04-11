def checkerboard():
  
  for index in range (0, 8):
    if index % 2 != 0:
      print '* ' * 8
    else:
      print ' *' * 8
checkerboard()