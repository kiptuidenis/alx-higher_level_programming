def update(self, *args):
        """This method assigns an argument to each attribute
        """
        len_of_tuple = len(args)
        while(len_of_tuple != 0):
                if len_of_tuple == 1:
                    self.id = args[0]
                    self.width = self.width
                    self.height = self.height
                    self.x = self.x
                    self.y = self.y
                elif len_of_tuple == 2:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = self.height
                    self.x = self.x
                    self.y = self.y
                elif len_of_tuple == 3:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = self.x
                    self.y = self.y
                elif len_of_tuple == 4:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = self.y
                elif len_of_tuple == 5:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = args[4]
                len_of_tuple -= 1
