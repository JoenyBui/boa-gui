import wx.propgrid as wxpg

__author__ = 'jbui'


class PropGrid(wxpg.PropertyGrid):

    def __init__(self, *args, **kwargs):
        wxpg.PropertyGrid.__init__(self, *args, **kwargs)

        self.Append( wxpg.FileProperty("Parts File", "parset", value='step2mesh.csv'))
        self.SetPropertyHelpString("parset", "This csv is used to define the paramters of each part.")

        self.Append( wxpg.PropertyCategory("Element Quality Parameters") )
        self.Append( wxpg.FloatProperty("Element Size (15.0)", "elem_size", value=15.0))
        self.SetPropertyHelpString("elem_size", "Defines the mesh size.")

        self.Append( wxpg.BoolProperty("Process Holes (False)", "holes", value=False))
        self.SetPropertyAttribute("holes", "UseCheckbox", True)
        self.SetPropertyHelpString("holes", "Specifies whether or not explicit hole meshing will take place.")

        self.Append( wxpg.FloatProperty("Minimum Hold Diameter (6.35)", "min_hole", value=6.35))
        self.SetPropertyHelpString("min_hole", "All holes smaller than this diameter will not be meshed.")

        self.Append( wxpg.FloatProperty("Maximum Hold Diameter (25.4)", "max_hole", value=25.4))
        self.SetPropertyHelpString("max_hole", "All holes larger than this diameter are treated as cutouts.")

        self.Append( wxpg.FloatProperty("Merge Tolerance Factor (0.15)", "merge", value=0.15))
        self.SetPropertyHelpString("merge", "Used to fuse mesh segments of the same part together.")

        self.Append( wxpg.FloatProperty("Maximum Deviation (0.1)", "deviation", value=0.1))
        self.SetPropertyHelpString("deviation", "Specifies the max deviation to use in a rigid mesh.")

        self.Append( wxpg.FloatProperty("Volume Ratio Tolerance (0.75)", "vol_ratio", value=0.75))
        self.SetPropertyHelpString("vol_ratio", "Specifies allowable difference in volume ratio (Geometric/Meshed).")
