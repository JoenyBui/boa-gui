import wx
import wx.lib.agw.customtreectrl as ct

__author__ = 'jbui'


class ProjectTree(ct.CustomTreeCtrl):
    """
    Project Tree Structure
    """

    def __init__(self, parent, controller, project=None, **kwargs):
        id = kwargs.get('id', -1)
        ct.CustomTreeCtrl.__init__(self, parent, size=kwargs.get('size', wx.Size(200, 150)), id=id, agwStyle=wx.TR_DEFAULT_STYLE)

        self.project = project
        self.controller = controller

        self.refresh_model()

    def refresh(self):
        if self.project:
            pass

    def refresh_model(self):
        root = self.AddRoot("The Root Item")

        # Create an image list to add icons next to an item
        il = wx.ImageList(16, 16)
        fldridx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN,wx.ART_OTHER, (16, 16)))
        fileidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))

        self.SetImageList(il)

        self.SetItemImage(root, fldridx, wx.TreeItemIcon_Normal)
        self.SetItemImage(root, fldropenidx, wx.TreeItemIcon_Expanded)

        for x in range(15):
            child = self.AppendItem(root, "Item %d" % x)
            self.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
            self.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Expanded)

            for y in range(5):
                last = self.AppendItem(child, "item %d-%s" % (x, chr(ord("a")+y)))
                self.SetItemImage(last, fldridx, wx.TreeItemIcon_Normal)
                self.SetItemImage(last, fldropenidx, wx.TreeItemIcon_Expanded)

                for z in range(5):
                    item = self.AppendItem(last,  "item %d-%s-%d" % (x, chr(ord("a")+y), z))
                    self.SetItemImage(item, fileidx, wx.TreeItemIcon_Normal)
                    # self.SetItemImage(item, smileidx, wx.TreeItemIcon_Selected)

        self.Expand(root)
