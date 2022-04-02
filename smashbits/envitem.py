class EnvItem:
    """
    Purpose: a class that holds the basic information for the enviroment items (platforms)

    """

    def __init__(self, rect, blocking, color):
        """
        Purpose: create the attributes and base variables of the class
        Parameters:
            self - an instance of the attributes of the player class
            rect - rectangle object
            blocking - true or false if it blocks player movement through
            color - the color of the platforms
        Return:
            none 
        """
        self.rect = rect
        self.blocking = blocking
        self.color = color