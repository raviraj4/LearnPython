# special methods

class WatchList:
    def __init__(self, name, author, volumes):
        self.name = name
        self.author = author
        self.volumes = volumes
        
    def __str__(self):
        return f"{self.name} by {self.author}"
    
    def __len__(self):
        return self.volumes

    def __del__(self):
        print("Book has been deleted from watchlist")

ani = WatchList("Vagabond", "Inoue Takehiko", 37)
print(str(ani))
print(len(ani))
del ani
