import wx
import wx.lib.agw.customtreectrl as ct

from ..controller.tree import TreeController

__author__ = 'jbui'


class ProjectTree(ct.CustomTreeCtrl):
    """
    Project Tree Structure
    """

    def __init__(self, parent, controller, project=None, **kwargs):
        id = kwargs.get('id', -1)
        ct.CustomTreeCtrl.__init__(self, parent, size=kwargs.get('size', wx.Size(200, 150)), id=id, agwStyle=wx.TR_DEFAULT_STYLE)

        self.controller = TreeController(controller, self)

        # Create an image list to add icons next to an item
        self.il = wx.ImageList(16, 16)
        self.fldridx = self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
        self.fldropenidx = self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN,wx.ART_OTHER, (16, 16)))
        self.fileidx = self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))

        self.SetImageList(self.il)

    def add_root(self, directory):

        for key, item in directory.items():
            if isinstance(item, dict):
                root = self.AddRoot(key)

                self.SetItemImage(root, self.fldridx, wx.TreeItemIcon_Normal)
                self.SetItemImage(root, self.fldropenidx, wx.TreeItemIcon_Expanded)

                self.add_item(item, root)

    def add_item(self, items, parent):
        for key, item in items.items():
            if key == '.git':
                continue

            child = self.AppendItem(parent, key)

            if isinstance(item, dict):
                self.SetItemImage(child, self.fldridx, wx.TreeItemIcon_Normal)
                self.SetItemImage(child, self.fldropenidx, wx.TreeItemIcon_Expanded)

                self.add_item(item, child)
            else:
                self.SetItemImage(child, self.fileidx, wx.TreeItemIcon_Normal)

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
