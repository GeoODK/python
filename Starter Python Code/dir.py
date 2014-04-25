from tkCommonDialog import Dialog

class Chooser(Dialog):

    command = "tk_chooseDirectory"

    def _fixresult(self, widget, result):
        if result:
            # keep directory until next time
            self.options["initialdir"] = result
        self.directory = result # compatibility
        return result

#
# convenience stuff

def askdirectory(**options):
    "Ask for a directory name"

    return apply(Chooser, (), options).show()

# --------------------------------------------------------------------
# test stuff

if __name__ == "__main__":

    print "directory"
