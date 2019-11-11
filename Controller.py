import win32gui


class Controller:

    @staticmethod
    def set_top_window(window_caption):
        window_handle = win32gui.FindWindow(None, window_caption)
        print("-> Activate the app: " + window_caption + " @ Handle: ", window_handle)
        # win32gui.SetActiveWindow(window_handle)
        win32gui.SetForegroundWindow(window_handle)


if __name__ == '__main__':
    Controller.set_top_window("Unity 2019.1.8f1 - mainScene.unity - Learn unity editor script - PC, Mac & Linux Standalone <DX11>")



