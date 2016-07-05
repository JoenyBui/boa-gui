
import uuid

import wx

from wx.lib.pubsub import pub

from threading import Thread

__author__ = 'jbui'


class ProgressDialog(wx.Dialog):
    """

    """
    def __init__(self, thread, *args, **kwargs):
        """

        :param thread:
        :param args:
        :param kwargs:
        :return:
        """
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
        """

        """
        btn = wx.Button(self, label="Cancel")
        btn.Bind(wx.EVT_BUTTON, self.on_cancel)

        BOTH_SIDES = wx.EXPAND | wx.ALL

        vsizer = wx.BoxSizer(wx.VERTICAL)

        vsizer.AddStretchSpacer()
        vsizer.Add(self.get_horizontal_size(self.field1_lbl), 0, BOTH_SIDES, 1)
        vsizer.AddSpacer(3)
        vsizer.Add(self.get_horizontal_size(self.field2_lbl), 0, BOTH_SIDES, 1)
        vsizer.AddSpacer(3)
        vsizer.Add(self.get_horizontal_size(self.progress), 0, BOTH_SIDES, 1)
        vsizer.AddSpacer(6)
        vsizer.Add(self.get_horizontal_size(btn), 0, BOTH_SIDES, 1)
        vsizer.AddStretchSpacer()

        self.SetSizer(vsizer)

    def get_horizontal_size(self, component):
        """
        Get the horizontal sizer

        :param component:
        :return: horizontal box sizer
        """
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.AddStretchSpacer()
        hsizer.Add(component, 0, wx.ALL | wx.EXPAND, 0)
        hsizer.AddStretchSpacer()

        return hsizer

    def on_cancel(self, event):
        """
        Cancel Thread.

        :param event:
        """
        self.thread.stop()

    def update_progress(self, value):
        """

        :param value:
        """
        lbl = "%d/%d" % (value, self.max_value)
        self.field2_lbl.SetLabelText(lbl)
        self.progress.SetValue(value)

    def destroy_progress(self):
        """
        Destroy the dialog.

        """
        self.Destroy()

    def end_modal(self):
        """
        """
        self.EndModal(retCode=wx.ID_OK)

    def ShowModal(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.thread.start()

        return wx.Dialog.ShowModal(self, *args, **kwargs)


class ProgressThread(Thread):
    """
    Progress Thread.

    """
    def __init__(self, max_value=10):
        """

        :param max_value:
        :return:
        """
        Thread.__init__(self)

        self.uuid = str(uuid.uuid4())
        self.max_value = max_value

    @property
    def update_name(self):
        """

        :return:
        """
        return self.uuid + 'UPDATE'

    @property
    def destroy_name(self):
        """

        :return:
        """
        return self.uuid + 'DESTROY'

    @property
    def end_name(self):
        """

        :return:
        """
        return self.uuid + 'END'

    def send_message(self, value):
        """

        :param value:
        :return:
        """
        wx.CallAfter(pub.sendMessage, self.update_name, value=value)

    def send_destroy(self):
        """

        :return:
        """
        wx.CallAfter(pub.sendMessage, self.destroy_name)

    def send_end(self):
        """
        Broadcast message to end the thread.

        :return:
        """
        wx.CallAfter(pub.sendMessage, self.end_name)

    def stop(self):
        """
        Kill Thread.

        """
        self.__stop = True

        self.send_destroy()
