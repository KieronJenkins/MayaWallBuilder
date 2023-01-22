# -------------------------- IMPORTS
from maya import cmds

# -------------------------- VARIABLES
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 515
WINDOW_TITLE = "Wall Builder"
WINDOW_CHECK = "mayaWallBuilder"

BRICK_COURSES = 0
WALL_DEFAULT_LENGTH = 0

# -------------------------- FUNCTIONS
# This function checks if the window specified by WINDOW_CHECK exists and if it does, it deletes it.  
def CheckWindowExists():
    if (cmds.window(WINDOW_CHECK, exists=True)):
        cmds.deleteUI(WINDOW_CHECK)

# This function updates the brick course and wall length input fields in the UI based on the values from the sliders.
def UpdateWallInputs(*args):
    try:
        course_value = cmds.floatSlider(brick_course_slider, query=True, value=True)
        cmds.text(brick_course_text, edit=True, label="" + str(round(course_value)))
        wall_length_value = cmds.floatSlider(wall_length_slider, query=True, value=True)
        cmds.floatField(wall_length_text, edit=True, value=round(wall_length_value, 2))
    except ValueError as e:
        cmds.warning("Invalid value entered for brick course or wall length: {}".format(e))
    except TypeError as e:
        cmds.warning("Invalid type entered for brick course or wall length: {}".format(e))

# This function creates a wall plane with the specified number of brick courses and wall length using the polyPlane command.
def CreateWallPlane(course_value, wall_length_value, *args): 
    if cmds.currentUnit(query=True, linear=True) != "centimeter":
        GetCurrentMeasurements()
        cmds.currentUnit(linear="centimeter")
    brick_course_amount = round(course_value)
    WALL_DEFAULT_LENGTH = round(wall_length_value, 2)
    BRICK_COURSES = brick_course_amount * float(7.5)

    name_value = cmds.textField(custom_plane_name, query=True, text=True)
    if name_value == "":
        name_value = "WallPlane_001"

    created_plane = cmds.polyPlane(name=name_value, subdivisionsX=1, subdivisionsY=1, h=BRICK_COURSES, w=WALL_DEFAULT_LENGTH)
    cmds.rotate(90, 0, 0, created_plane, relative=True)
    cmds.textField(custom_plane_name, edit=True, text="")
    cmds.currentUnit(linear=SCENE_MEASUREMENT_UNITS)


def GetCurrentMeasurements():
    try:
        SCENE_MEASUREMENT_UNITS = cmds.currentUnit(query=True, linear=True)
    except ValueError as e:
        cmds.warning("Invalid current measurement units: {}".format(e))
    except RuntimeError as e:
        cmds.warning("Error occured when getting the current measurement units: {}".format(e))



# -------------------------- EXISTING WINDOW CHECK
CheckWindowExists()
GetCurrentMeasurements()

builderWindow = cmds.window(WINDOW_CHECK, title=WINDOW_TITLE, widthHeight=(WINDOW_WIDTH, WINDOW_HEIGHT),
                            maximizeButton=False, resizeToFitChildren=True)

# -------------------------- WINDOW GUI LAYOUT
cmds.columnLayout(adjustableColumn=True)

cmds.separator(height=10, style='none')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
label = cmds.text(label="Brick Courses:", font='boldLabelFont')
cmds.separator(width=10, style='none')

cmds.setParent('..')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
brick_course_slider = cmds.floatSlider(min=1, max=120, value=60, step=1, dragCommand=UpdateWallInputs, width=450)
cmds.separator(width=10, style='none')
brick_course_text = cmds.text(label="60", font='boldLabelFont')
cmds.separator(width=10, style='none')

cmds.setParent('..')

cmds.separator(height=10, style='none')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
label = cmds.text(label="Wall Length:", font='boldLabelFont')
cmds.separator(width=10, style='none')

cmds.setParent('..')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
wall_length_slider = cmds.floatSlider(min=1, max=2000, value=1000, step=0.01, dragCommand=UpdateWallInputs, width=450)
cmds.separator(width=5, style='none')
wall_length_text = cmds.floatField(minValue=1, maxValue=2000, value=1000, precision=2, step=0.01, width=45)
cmds.separator(width=10, style='none')

cmds.setParent('..')

cmds.separator(height=5, style='none')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
cmds.text(label='Polygonal Plane Name: ', font='boldLabelFont')

cmds.setParent('..')

cmds.separator(height=5, style='none')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
custom_plane_name = cmds.textField(pht="Example: Ext_Wall_Mid_01", width=500)

cmds.setParent('..')

cmds.separator(height=10, style='none')
cmds.separator(width=450, style='double')
cmds.separator(height=10, style='none')

cmds.rowColumnLayout(numberOfRows=1)

cmds.separator(width=5, style='none')
cmds.button(label='Create Polygonal Plane', width=500, height=30,
            annotation="Creates a Polygonal Plane at 0, 0, 0 with the given Courses and Length", bgc=(105, 150, 246),
            command=lambda *args: CreateWallPlane(cmds.floatSlider(brick_course_slider, query=True, value=True),
                                                  cmds.floatSlider(wall_length_slider, query=True, value=True)))

cmds.setParent('..')

cmds.separator(height=5, style='none')

cmds.showWindow(builderWindow)
cmds.dockControl(area='right', floating=False, content=WINDOW_CHECK, width=WINDOW_WIDTH, label=WINDOW_TITLE)
