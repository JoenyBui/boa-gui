
import uuid

import wx

from wx.lib.pubsub import pub

from threading import Thread

__author__ = 'jbui'


class ProgressDialog(wx.Dialog):
    """

    """
    def __init__(self, thread, *args, **kwargs):
        wx.Dialog.__init__(self, None, **kwargs)

        self.count = 0
        self.max_value = thread.max_value


        # Make the labels
        self.field1_lbl = wx.StaticText(self, label="Loading")
        self.field2_lbl = wx.StaticText(self, label="")
        self.progress = wx.Gauge(self, id=wx.ID_ANY, range=self.max_value)

        self.do_layout()

        # Create a pubsub listener.
        pub.subscribe(self.update_progress, thread.update_name)
        pub.subscribe(self.destroy_progress, thread.destroy_name)
        pub.subscribe(self.end_modal, thread.end_name)

        self.thread = thread

    def do_layout(self):
        btn = wx.Button(self, label="Cancel")
        btn.Bind(wx.EVT_BUTTON, self.on_cancel)

        BOTH_SIDES = wx.EXPAND | wx.LEFT | wx.RIGHT

        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.AddStretchSpacer()
        vsizer.Add(self.get_horizontal_size(self.field1_lbl), 0, BOTH_SIDES | wx.TOP, 1)
        vsizer.AddSpacer(3)
        vsizer.Add(self.get_horizontal_size(self.field2_lbl), 0, BOTH_SIDES | wx.CENTER, 1)
        vsizer.AddSpacer(3)
        vsizer.Add(self.get_horizontal_size(self.progress), 0, BOTH_SIDES | wx.CENTER, 1)
        vsizer.AddSpacer(6)
        vsizer.Add(self.get_horizontal_size(btn), 0, BOTH_SIDES | wx.BOTTOM, 1)
        vsizer.AddStretchSpacer()

        self.SetSizer(vsizer)

    def get_horizontal_size(self, component):
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.AddStretchSpacer()
        hsizer.Add(component, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        hsizer.AddStretchSpacer()

        return hsizer

    def on_cancel(self, event):
        self.thread.stop()

    def update_progress(self, value):
        lbl = "%d/%d" % (value, self.max_value)
        self.field2_lbl.SetLabelText(lbl)
        self.progress.SetValue(value)

    def destroy_progress(self):
        self.Destroy()

    def end_modal(self):
        self.EndModal(retCode=wx.ID_OK)

    def ShowModal(self, *args, **kwargs):
        self.thread.start()

        return wx.Dialog.ShowModal(self, *args, **kwargs)


class ProgressThread(Thread):

    def __init__(self, max_value=10):
        Thread.__init__(self)

        self.uuid = str(uuid.uuid4())
        self.max_value = max_value

    @property
    def update_name(self):
        return self.uuid + 'UPDATE'

    @property
    def destroy_name(self):
        return self.uuid + 'DESTROY'

    @property
    def end_name(self):
        return self.uuid + 'END'

    def send_message(self, value):
        wx.CallAfter(pub.sendMessage, self.update_name, value=value)

    def send_destroy(self):
        wx.CallAfter(pub.sendMessage, self.destroy_name)

    def send_end(self):
        wx.CallAfter(pub.sendMessage, self.end_name)

    def stop(self):
        self.__stop = True

        print("Stop Thread")

        self.send_destroy()
