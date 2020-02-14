import re
import os

class ProcessMidiFiles:
    def __init__(self,pieces_dict):
        print("initializedd")
        self.pieces_dict = pieces_dict

    def rename_files(self,directory,grade):
        print "almostt"
        for root, dirs, song_files in os.walk(directory):
            for filename in song_files:
                if(filename[0]!="."):
                    print "fileee to rename: "+str(filename)
                    start = filename[0:len(filename)-4]
                    print "start: "+start
                    end = filename[len(filename)-4:]
                    print "end: "+end
                    new_start = start+"("+str(grade)+")"
                    print "new_start: "+new_start
                    new_name = new_start+end
                    print "new name: ",new_name

                    print "originalll directory: ",directory+str(filename)
                    print "new directory: ",directory+"Songs/"+new_name

                    os.rename(directory+str(filename),"/Users/arturobarrios/Documents/"+"Songs/"+new_name)
            



