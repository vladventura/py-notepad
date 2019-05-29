class Notepad:

    brain = list()

    def read_file(self):
        try:
            with open("save.dat", "rt") as file:
                # print("File opened to read")
                for line in file.readlines():
                    self.brain.append(line.replace("\n", ""))
                # print("Read loop exited")
            # print("Message(s) read")
        except FileNotFoundError:
            # print("File wasn't there, so I'll make a new one")
            f = open("save.dat", "wt")
            f.close()


    def buffer(self, info):
        if f"{info}" not in self.brain:
            self.brain.append(f"{info}")
            # print("Message added to buffer successfully")


    def remove(self, info):
        try:
            del self.brain[int(info) - 1]
            # print("Message removed from buffer successfully")
        except IndexError:
            print("This item is not available")
        except ValueError:
            try:
                self.brain.remove(info)
            except ValueError:
                print("This message is not in the buffer")


    def write_to_file(self):
        with open("save.dat", "wt") as file:
            # print("File to write to is open")
            for lines in self.brain:
                file.write(lines)
                file.write("\n")
        # print("List written to file")


    def show_text(self):
        for lines in self.brain:
            print(f"[{self.brain.index(lines) + 1}]{lines}")
        print("\n")