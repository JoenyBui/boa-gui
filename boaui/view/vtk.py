import wx

import vtk

from .wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor

__author__ = 'Joeny'


class VtkViewer(wx.Panel):
    """
    Vtk Viewer

    """
    def __init__(self, parent):
        """

        :param parent:
        :return:
        """
        wx.Panel.__init__(self, parent)

        # To Interact with the scene using the mouse use an instance of vtkRender.
        self.widget = wxVTKRenderWindowInteractor(self, -1)
        self.widget.Enable(1)
        self.widget.AddObserver()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.widget, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Layout()

        self.ren = vtk.vtkRenderer()

        self.filename = ''
        self.isploted = False

    def renderthis(self):
        """

        :return:
        """
        # open a window and create a renderer
        self.widget.GetRenderWindow().AddRenderer(self.ren)

        # open file
        openFileDialog = wx.FileDialog(self, "Open STL file", "", self.filename,
                                   "*.stl", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.filename = openFileDialog.GetPath()
        # render the data
        reader = vtk.vtkSTLReader()
        reader.SetFileName(self.filename)

        # To take the polygonal data from the vtkConeSource and
        # create a rendering for the renderer.
        coneMapper = vtk.vtkPolyDataMapper()
        coneMapper.SetInput(reader.GetOutput())

        # create an actor for our scene
        if self.isploted:
            coneActor=self.ren.GetActors().GetLastActor()
            self.ren.RemoveActor(coneActor)

        coneActor = vtk.vtkActor()
        coneActor.SetMapper(coneMapper)
        # Add actor
        self.ren.AddActor(coneActor)
        # print self.ren.GetActors().GetNumberOfItems()

        if not self.isploted:
            axes = vtk.vtkAxesActor()
            self.marker = vtk.vtkOrientationMarkerWidget()
            self.marker.SetInteractor( self.widget._Iren )
            self.marker.SetOrientationMarker( axes )
            self.marker.SetViewport(0.75, 0, 1, 0.25)
            self.marker.SetEnabled(1)

        self.ren.ResetCamera()
        self.ren.ResetCameraClippingRange()
        cam = self.ren.GetActiveCamera()
        cam.Elevation(10)
        cam.Azimuth(70)
        self.isploted = True
        self.ren.Render()
