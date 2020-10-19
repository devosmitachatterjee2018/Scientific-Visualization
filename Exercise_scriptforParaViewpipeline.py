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
renderView1.ViewSize = [1073, 220]
renderView1.AnnotationColor = [0.6666666666666666, 0.0, 0.0]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterAxesVisibility = 1
renderView1.OrientationAxesLabelColor = [0.6666666666666666, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.4980392156862745]
renderView1.CenterOfRotation = [1.100000023841858, 0.20499999821186066, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.0694834987622972, -0.01878785237158377, 10000.0]
renderView1.CameraFocalPoint = [1.0694834987622972, -0.01878785237158377, 0.0]
renderView1.CameraParallelScale = 1.118939252917222
renderView1.Background = [1.0, 0.6901960784313725, 0.3764705882352941]
renderView1.UseGradientBackground = 1
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
renderView1.AxesGrid.XLabelColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Xdmf3ReaderS'
pressurexdmf = Xdmf3ReaderS(FileName=['D:\\M.SC. prog. in Engineering Mathematics and Computational Science\\Scientific Visualization\\pressure.xdmf'])
pressurexdmf.PointArrays = ['pres']

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(Input=pressurexdmf)
warpByScalar1.Scalars = ['POINTS', 'pres']
warpByScalar1.ScaleFactor = 0.1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from warpByScalar1
warpByScalar1Display = Show(warpByScalar1, renderView1)

# get color transfer function/color map for 'pres'
presLUT = GetColorTransferFunction('pres')
presLUT.AutomaticRescaleRangeMode = 'Never'
presLUT.RGBPoints = [-1.2, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 1.2, 0.705882, 0.0156863, 0.14902]
presLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'pres'
presPWF = GetOpacityTransferFunction('pres')
presPWF.Points = [-1.2, 0.0, 0.5, 0.0, 0.015189931503376775, 0.296875, 0.5, 0.0, 0.26582280581270323, 0.40625, 0.5, 0.0, 0.26582280581270323, 0.9375, 0.5, 0.0, 0.6227848681795951, 0.203125, 0.5, 0.0, 0.7822784568592638, 0.390625, 0.5, 0.0, 1.2, 1.0, 0.5, 0.0]
presPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
warpByScalar1Display.ColorArrayName = ['POINTS', 'pres']
warpByScalar1Display.LookupTable = presLUT
warpByScalar1Display.EdgeColor = [0.0, 0.0, 1.0]
warpByScalar1Display.OSPRayScaleArray = 'pres'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 227.2398681640625
warpByScalar1Display.SelectScaleArray = 'pres'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'pres'
warpByScalar1Display.GaussianRadius = 11.361993408203125
warpByScalar1Display.SetScaleArray = ['POINTS', 'pres']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'pres']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.SelectionCellLabelFontFile = ''
warpByScalar1Display.SelectionPointLabelFontFile = ''
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = presPWF
warpByScalar1Display.ScalarOpacityUnitDistance = 136.78494261796828

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
warpByScalar1Display.DataAxesGrid.XTitleColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.XTitleFontFile = ''
warpByScalar1Display.DataAxesGrid.YTitleColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.YTitleFontFile = ''
warpByScalar1Display.DataAxesGrid.ZTitleColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.ZTitleFontFile = ''
warpByScalar1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
warpByScalar1Display.DataAxesGrid.XLabelColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.XLabelFontFile = ''
warpByScalar1Display.DataAxesGrid.YLabelColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.YLabelFontFile = ''
warpByScalar1Display.DataAxesGrid.ZLabelColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
warpByScalar1Display.PolarAxes.PolarAxisTitleColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.PolarAxes.PolarAxisTitleFontFile = ''
warpByScalar1Display.PolarAxes.PolarAxisLabelColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.PolarAxes.PolarAxisLabelFontFile = ''
warpByScalar1Display.PolarAxes.LastRadialAxisTextColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.PolarAxes.LastRadialAxisTextFontFile = ''
warpByScalar1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.6666666666666666, 0.0, 0.0]
warpByScalar1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for presLUT in view renderView1
presLUTColorBar = GetScalarBar(presLUT, renderView1)
presLUTColorBar.Title = 'pres'
presLUTColorBar.ComponentTitle = ''
presLUTColorBar.TitleColor = [0.6666666666666666, 0.0, 0.0]
presLUTColorBar.TitleFontFile = ''
presLUTColorBar.LabelColor = [0.6666666666666666, 0.0, 0.0]
presLUTColorBar.LabelFontFile = ''

# set color bar visibility
presLUTColorBar.Visibility = 1

# show color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(None)
# ----------------------------------------------------------------