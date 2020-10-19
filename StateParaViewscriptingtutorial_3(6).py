# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [425, 247]
renderView1.AnnotationColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterAxesVisibility = 1
renderView1.OrientationAxesLabelColor = [0.6666666666666666, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.4980392156862745]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.2116775049056625, 2.3184465355294925, -0.7482321413931913]
renderView1.CameraViewUp = [-0.6040512787517719, 0.3442719813400311, -0.7187481168688782]
renderView1.CameraParallelScale = 0.8516115354228021
renderView1.Background = [1.0, 0.6901960784313725, 0.3764705882352941]
renderView1.UseGradientBackground = 1
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Sphere'
sphere2 = Sphere()
sphere2.ThetaResolution = 360
sphere2.PhiResolution = 180

# create a new 'Sphere'
sphere1 = Sphere()
sphere1.ThetaResolution = 16

# create a new 'Shrink'
shrink1 = Shrink(Input=sphere1)
shrink1.ShrinkFactor = 0.25

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(Input=sphere1)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(Input=[shrink1, extractEdges1])

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from groupDatasets1
groupDatasets1Display = Show(groupDatasets1, renderView1)

# trace defaults for the display properties.
groupDatasets1Display.Representation = 'Surface'
groupDatasets1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
groupDatasets1Display.ColorArrayName = [None, '']
groupDatasets1Display.EdgeColor = [0.0, 0.0, 1.0]
groupDatasets1Display.OSPRayScaleArray = 'Normals'
groupDatasets1Display.OSPRayScaleFunction = 'PiecewiseFunction'
groupDatasets1Display.SelectOrientationVectors = 'None'
groupDatasets1Display.ScaleFactor = 0.1
groupDatasets1Display.SelectScaleArray = 'None'
groupDatasets1Display.GlyphType = 'Arrow'
groupDatasets1Display.GlyphTableIndexArray = 'None'
groupDatasets1Display.GaussianRadius = 0.005
groupDatasets1Display.SetScaleArray = ['POINTS', 'Normals']
groupDatasets1Display.ScaleTransferFunction = 'PiecewiseFunction'
groupDatasets1Display.OpacityArray = ['POINTS', 'Normals']
groupDatasets1Display.OpacityTransferFunction = 'PiecewiseFunction'
groupDatasets1Display.DataAxesGrid = 'GridAxesRepresentation'
groupDatasets1Display.SelectionCellLabelFontFile = ''
groupDatasets1Display.SelectionPointLabelFontFile = ''
groupDatasets1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
groupDatasets1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.XTitleFontFile = ''
groupDatasets1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.YTitleFontFile = ''
groupDatasets1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.ZTitleFontFile = ''
groupDatasets1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.XLabelFontFile = ''
groupDatasets1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.YLabelFontFile = ''
groupDatasets1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
groupDatasets1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.PolarAxisTitleFontFile = ''
groupDatasets1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.PolarAxisLabelFontFile = ''
groupDatasets1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.LastRadialAxisTextFontFile = ''
groupDatasets1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
groupDatasets1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(sphere2)
# ----------------------------------------------------------------