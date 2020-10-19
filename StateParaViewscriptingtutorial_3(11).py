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
renderView1.ViewSize = [587, 164]
renderView1.AnnotationColor = [0.6666666666666666, 0.0, 0.0]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterAxesVisibility = 1
renderView1.OrientationAxesLabelColor = [0.6666666666666666, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.4980392156862745]
renderView1.CenterOfRotation = [0.0, 0.0, 0.07999992370605469]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 1.0, 51.119268546836174]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.07999992370605469]
renderView1.CameraParallelScale = 12.951115722667065
renderView1.Background = [0.0, 0.0, 0.0]
renderView1.Background2 = [0.0, 0.0, 0.6]
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

# create a new 'ExodusIIReader'
exodusIIReader1 = ExodusIIReader(FileName=['C:/Program Files/ParaView 5.6.0-Windows-msvc2015-64bit/examples/disk_out_ref.ex2'])
exodusIIReader1.PointVariables = ['Temp', 'V', 'Pres', 'AsH3', 'GaMe3', 'CH4', 'H2']
exodusIIReader1.NodeSetArrayStatus = []
exodusIIReader1.SideSetArrayStatus = []
exodusIIReader1.ElementBlocks = ['Unnamed block ID: 1 Type: HEX8']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from exodusIIReader1
exodusIIReader1Display = Show(exodusIIReader1, renderView1)

# get color transfer function/color map for 'Pres'
presLUT = GetColorTransferFunction('Pres')
presLUT.RGBPoints = [0.006785521749407053, 0.231373, 0.298039, 0.752941, 0.017802017042413354, 0.865003, 0.865003, 0.865003, 0.028818512335419655, 0.705882, 0.0156863, 0.14902]
presLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Pres'
presPWF = GetOpacityTransferFunction('Pres')
presPWF.Points = [0.006785521749407053, 0.0, 0.5, 0.0, 0.028818512335419655, 1.0, 0.5, 0.0]
presPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
exodusIIReader1Display.Representation = 'Surface'
exodusIIReader1Display.AmbientColor = [0.0, 0.0, 0.4980392156862745]
exodusIIReader1Display.ColorArrayName = ['POINTS', 'Pres']
exodusIIReader1Display.DiffuseColor = [0.0, 0.0, 1.0]
exodusIIReader1Display.LookupTable = presLUT
exodusIIReader1Display.Specular = 1.0
exodusIIReader1Display.SpecularPower = 128.0
exodusIIReader1Display.EdgeColor = [0.0, 0.0, 1.0]
exodusIIReader1Display.OSPRayScaleArray = 'AsH3'
exodusIIReader1Display.OSPRayScaleFunction = 'PiecewiseFunction'
exodusIIReader1Display.SelectOrientationVectors = 'AsH3'
exodusIIReader1Display.ScaleFactor = 2.015999984741211
exodusIIReader1Display.SelectScaleArray = 'AsH3'
exodusIIReader1Display.GlyphType = 'Arrow'
exodusIIReader1Display.GlyphTableIndexArray = 'AsH3'
exodusIIReader1Display.GaussianRadius = 0.10079999923706055
exodusIIReader1Display.SetScaleArray = ['POINTS', 'AsH3']
exodusIIReader1Display.ScaleTransferFunction = 'PiecewiseFunction'
exodusIIReader1Display.OpacityArray = ['POINTS', 'AsH3']
exodusIIReader1Display.OpacityTransferFunction = 'PiecewiseFunction'
exodusIIReader1Display.DataAxesGrid = 'GridAxesRepresentation'
exodusIIReader1Display.SelectionCellLabelFontFile = ''
exodusIIReader1Display.SelectionPointLabelFontFile = ''
exodusIIReader1Display.PolarAxes = 'PolarAxesRepresentation'
exodusIIReader1Display.ScalarOpacityFunction = presPWF
exodusIIReader1Display.ScalarOpacityUnitDistance = 1.3249258044319845

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
exodusIIReader1Display.DataAxesGrid.XTitleColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.DataAxesGrid.XTitleFontFile = ''
exodusIIReader1Display.DataAxesGrid.YTitleColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.DataAxesGrid.YTitleFontFile = ''
exodusIIReader1Display.DataAxesGrid.ZTitleColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.DataAxesGrid.ZTitleFontFile = ''
exodusIIReader1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.4980392156862745]
exodusIIReader1Display.DataAxesGrid.XLabelColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.DataAxesGrid.XLabelFontFile = ''
exodusIIReader1Display.DataAxesGrid.YLabelColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.DataAxesGrid.YLabelFontFile = ''
exodusIIReader1Display.DataAxesGrid.ZLabelColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
exodusIIReader1Display.PolarAxes.PolarAxisTitleColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.PolarAxes.PolarAxisTitleFontFile = ''
exodusIIReader1Display.PolarAxes.PolarAxisLabelColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.PolarAxes.PolarAxisLabelFontFile = ''
exodusIIReader1Display.PolarAxes.LastRadialAxisTextColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.PolarAxes.LastRadialAxisTextFontFile = ''
exodusIIReader1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.6666666666666666, 0.0, 0.0]
exodusIIReader1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for presLUT in view renderView1
presLUTColorBar = GetScalarBar(presLUT, renderView1)
presLUTColorBar.Title = 'Pres'
presLUTColorBar.ComponentTitle = ''
presLUTColorBar.TitleColor = [0.6666666666666666, 0.0, 0.0]
presLUTColorBar.TitleFontFile = ''
presLUTColorBar.LabelColor = [0.6666666666666666, 0.0, 0.0]
presLUTColorBar.LabelFontFile = ''

# set color bar visibility
presLUTColorBar.Visibility = 1

# show color legend
exodusIIReader1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(exodusIIReader1)
# ----------------------------------------------------------------