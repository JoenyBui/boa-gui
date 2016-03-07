
import uuid

import wx

from wx.lib.pubsub import pub

from threading import Thread

__author__ = 'jbui'


class ProgressDialog(wx.Dialog):

    def __init__(self, thread, *args, **kwargs):
        wx.Dialog.__init__(self, None, **kwargs)

        self.count = 0
        self.max_value = thread.max_value

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

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.progress, 0, wx.EXPAND)
        sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(sizer)

    def on_cancel(self, event):
        self.thread.stop()

    def update_progress(self, value):
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

        self.uuid = uuid.uuid4()
        self.max_value = max_value

    @property
    def update_name(self):
        return str(self.uuid) + 'UPDATE'

    @property
    def destroy_name(self):
        return str(self.uuid) + 'DESTROY'

    @property
    def end_name(self):
        return str(self.uuid) + 'END'

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
