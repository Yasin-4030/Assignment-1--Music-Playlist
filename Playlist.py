from Song import Song

class Playlist:  #this class is a linked list
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    node = self.__first_song  
    if not node: # if no song (node) at all, then ...
      self.__first_song = Song(title)
    else: # if there is already a node (song)
      while node:      
        if node.get_next_song() == None:
          newNode = Song(title)
          node.set_next_song(newNode)   
          break
      node = node.get_next_song()



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
  # The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

  def find_song(self, title):
    node = self.__first_song
    count = 0
    while node:
      if count == title:
        return node.get_title
      count += 1
      node = node.set_next_song

    assert(False)
    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    node = self.__first_song
    while node:
      if node.get_title == title:
        node = node.get_next_song()
  

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    if not self.__first_song: 
      return 0
    node = self.__first_song 
    counter = 1 
    while node:
      node = node.get_next_song()
      if node:
        counter += 1        
     
    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    node = self.__first_song 
    counter = 0
    while node:
      counter += 1
      print(str(counter) + '.', node.get_title())
      node = node.get_next_song()