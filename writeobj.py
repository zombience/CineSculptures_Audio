import time
import audioscape

class WriteOBJ:

    def __init__(self, audioscapein):

        self.ascape = audioscapein
        self.vertices = self.ascape.vertices
        self.faces = self.ascape.faces

        self.vn = (0, 1, 0)

    def write(self, filename):

        # referenced from https://blender.stackexchange.com/questions/32468/how-to-write-a-simple-wavefront-obj-exporter-in-python

        f = open(filename, 'w')

        t = time.time()

        # header
        f.write("OBJ File:\n")

        # write vertices
        for smpl in range(len(self.vertices)):
            for freq in range(len(self.vertices[0])):
                line = "v {} {} {}\n".format(
                        smpl, self.vertices[smpl][freq][1], self.vertices[smpl][freq][0])
                f.write(line)

        # write faces
        for face in range(len(self.faces)-1):
            line = "f {} {} {} {}\n".format(
                    self.faces[face][0], self.faces[face][1],
                    self.faces[face][2], self.faces[face][3])
            f.write(line)

        f.close()

        print("Wrote", filename, "in:", time.time()-t, "seconds.")