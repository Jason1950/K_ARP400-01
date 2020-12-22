
    ## ####################################
    ##      一行的濾波器 ， 比較簡易好用
    ## ####################################
    from scipy import signal
    def signal_filter(self,data,low_pass,high_pass):

        ## 3個選1個 ##
        b, a = signal.butter(8, low_pass, 'lowpass')   #配置濾波器 8 表示濾波器的階數
        b, a = signal.butter(8, high_pass, 'highpass')   #配置濾波器 8 表示濾波器的階數
        b, a = signal.butter(8, [low_pass,high_pass], 'bandpass')   #配置濾波器 8 表示濾波器的階數
        #############

        filtedData = signal.filtfilt(b, a, data)  #data為要過濾的訊號
        return filtedData





    ## ####################################
    ##       可調控較多參數 的 濾波器 !
    ## ####################################
    from scipy import signal
    def butter_bandpass(self, lowcut, highcut, fs, order):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        #b, a = signal.butter(order, [low, high], btype='band')
        b,a = signal.iirfilter(order, [low, high], rp=None, rs=None, btype='band', analog=False, ftype='butter', output='ba')
        return b, a

    def butter_bandpass_filter(self, data, lowcut, highcut, fs, order):
        b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
        y = signal.lfilter(b, a, data)
        return y    

