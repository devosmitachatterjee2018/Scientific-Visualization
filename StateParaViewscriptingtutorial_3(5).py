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
renderView1.ViewSize = [617, 247]
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
sphere1 = Sphere()
sphere1.ThetaResolution = 16

# create a new 'Shrink'
shrink1 = Shrink(Input=sphere1)
shrink1.ShrinkFactor = 0.25

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from shrink1
shrink1Display = Show(shrink1, renderView1)

# trace defaults for the display properties.
shrink1Display.Representation = 'Surface'
shrink1Display.AmbientColor = [0.0, 0.0, 0.0]
shrink1Display.ColorArrayName = [None, '']
shrink1Display.OSPRayScaleArray = 'Normals'
shrink1Display.OSPRayScaleFunction = 'PiecewiseFunction'
shrink1Display.SelectOrientationVectors = 'None'
shrink1Display.ScaleFactor = 0.09669896364212037
shrink1Display.SelectScaleArray = 'None'
shrink1Display.GlyphType = 'Arrow'
shrink1Display.GlyphTableIndexArray = 'None'
shrink1Display.GaussianRadius = 0.004834948182106018
shrink1Display.SetScaleArray = ['POINTS', 'Normals']
shrink1Display.ScaleTransferFunction = 'PiecewiseFunction'
shrink1Display.OpacityArray = ['POINTS', 'Normals']
shrink1Display.OpacityTransferFunction = 'PiecewiseFunction'
shrink1Display.DataAxesGrid = 'GridAxesRepresentation'
shrink1Display.SelectionCellLabelFontFile = ''
shrink1Display.SelectionPointLabelFontFile = ''
shrink1Display.PolarAxes = 'PolarAxesRepresentation'
shrink1Display.ScalarOpacityUnitDistance = 0.3558549949189315

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
shrink1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.XTitleFontFile = ''
shrink1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.YTitleFontFile = ''
shrink1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.ZTitleFontFile = ''
shrink1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.XLabelFontFile = ''
shrink1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.YLabelFontFile = ''
shrink1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
shrink1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.PolarAxisTitleFontFile = ''
shrink1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.PolarAxisLabelFontFile = ''
shrink1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.LastRadialAxisTextFontFile = ''
shrink1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(shrink1)
# ----------------------------------------------------------------