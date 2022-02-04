import maya.cmds as cmds
import maya.OpenMaya as om

brick_courses_default = 0 # Defaults
wall_length_default = 0


class WC_Window(object):
        
    #constructor
    def __init__(self):
            
        self.window = "WC_Window" # Start of Window 
        self.title = "Maya Wall Maker"
            
        
        if cmds.window(self.window, exists = True): # close old window is open
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=(200, 200)) # Window Settings
        
        cmds.rowColumnLayout() # Start of Textfields and Buttons
        cmds.separator( style='none', h=5 )
        cmds.setParent('..')
        cmds.rowColumnLayout( numberOfColumns=3, columnAttach=(1, 'right', 0), columnWidth=[(1, 80), (2, 5), (3, 175)] ) 
        cmds.text( label='Brick Courses: ' )
        cmds.separator( style='none', w=5 )
        brick_courses_default = cmds.textField("BC_Check", pht="e.g. 60")
        cmds.separator( style='none', h=5 )
        cmds.setParent('..')
        cmds.rowColumnLayout( numberOfColumns=3, columnAttach=(1, 'right', 0), columnWidth=[(1, 75), (2, 10), (3, 175)] )
        cmds.text( label='Wall Length: ' )
        cmds.separator( style='none', w=5 )
        wall_length_default = cmds.textField("WL_Check", pht="e.g. 1400")
        cmds.setParent('..')
        cmds.columnLayout( adjustableColumn=True )
        cmds.separator( style='none', h=15 )
        cmds.button( label="CREATE WALL", align='center', w=100, h=50, command=functions.create_wall_btn)
        cmds.separator( style='none', h=5 )
        cmds.button( label="CREATE GUIDE", align='center', w=100, h=25, command=functions.guide_wall_btn )
        cmds.separator( style='none', h=3 )
        cmds.setParent('..')
        cmds.rowColumnLayout()
        cmds.button( label="Duplicate", align='center', w=60, h=25, ann="Duplicate Wall", command=functions.duplicate_wall_btn )
        
        

        #display new window
        cmds.showWindow()
        
        
class functions:
    
    @staticmethod
    def create_wall_btn(wall_length_default, *args):
        cmds.currentUnit(linear = "centimeter") # Changes scene to CM
        brick_courses_default = cmds.textField("BC_Check", q=True, text=True) # Sets brick_courses_default to the textfield input of BC_Check
        wall_length_default = cmds.textField("WL_Check", q=True, text=True)
        wall_height = int(brick_courses_default) * float(7.5) # Multiplies the brick course amount by 7.5 to get wall height
        wall_length = float(wall_length_default) # Converts wall_length to a float
        functions.last_wall_save = [wall_height, wall_length] # Saves them out to store for duplicate button
        cmds.polyCube( n='HouseWall_001', sx=1, sy=1, sz=1, h=wall_height, w=wall_length, d=1 ) # Creates cube with the height and length
        om.MGlobal.displayWarning("Wall made with " + str(wall_height) + "cm height and " + str(wall_length) + "cm length") # Displays message
        cmds.textField("WL_Check", edit=True, text="") # Deletes text in textfield
        cmds.textField("BC_Check", edit=True, text="")
        
    @staticmethod
    def guide_wall_btn(wall_length_default, *args):
        cmds.currentUnit(linear = "centimeter") # Changes scene to CM
        brick_courses_default = cmds.textField("BC_Check", q=True, text=True)
        wall_length_default = cmds.textField("WL_Check", q=True, text=True)
        wall_height = int(brick_courses_default) * float(7.5)
        wall_length = float(wall_length_default)
        functions.last_wall_save = [wall_height, wall_length]
        cmds.polyCube( n='GuideWall_001', sx=1, sy=1, sz=1, h=wall_height, w=wall_length, d=1,  )
        om.MGlobal.displayWarning("Guide made with " + str(wall_height) + "cm height and " + str(wall_length) + "cm length") # Displays message
        cmds.textField("WL_Check", edit=True, text="")
        cmds.textField("BC_Check", edit=True, text="")
        
        
        
    @staticmethod
    def duplicate_wall_btn(*args):
        cmds.polyCube( n='DuplicatedWall_001', sx=1, sy=1, sz=1, h=functions.last_wall_save[0], w=functions.last_wall_save[1], d=1 ) # Grabs the saved data from above to use as height and length
        om.MGlobal.displayInfo("Duplicate Made") # Displays message
          
                                   
myWindow = WC_Window()
# Made by Kieron
