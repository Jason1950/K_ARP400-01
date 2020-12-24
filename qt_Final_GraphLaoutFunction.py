## Add to the main class
## This function can't import from other class, because the update mechanism
## is come from qt.timer, which function can't pass the parameter 
    def initGUIPlotWidget(self):
        self.win = pg.GraphicsLayoutWidget()
        self.win.resize(800, 800) 
        self.win.show()  ## show widget alone in its own window
        self.win.setWindowTitle('pyqtgraph example: ImageItem')

        ## heart rate waveform
        self.first_Plt = self.win.addPlot(colspan=3)
        self.first_Plt.showGrid(x=True,y=False,alpha=1)
        self.first_Plt.setLabel('bottom', "First Signal - Heart Rate Waveform")
        self.first_Plt.setXRange(0,240,padding=0)

        ## rPPG signal
        self.win.nextRow()
        self.second_Plt = self.win.addPlot(colspan=3)
        self.second_Plt.setLabel('bottom', "Second Signal - Motion X/Y FFT")

        ## motion X/Y FFT
        self.win.nextRow()
        self.third_Plt = self.win.addPlot(colspan=3)
        self.third_Plt.showGrid(x=True,y=True,alpha=1)
        self.third_Plt.setYRange(0,200,padding=0.1)
        self.third_Plt.setLabel('bottom', "Third Signal - Motion X/Y FFT")

        ## Create image item
        self.win.nextRow()
        self.view = self.win.addPlot() # or use self.win.addViewBox()
        ## lock the aspect ratio so pixels are always square
        # view.setAspectLocked(True)
        self.img_spectrum = pg.ImageItem(border='w')
        self.view.addItem(self.img_spectrum)
        self.view.setLabel('bottom', "Real-time HR Spectrum")
        self.view.setLimits( yMin=0, yMax=40, xMin=0, xMax=self.arr_size) 

        ## create color histogram
        self.hist = pg.HistogramLUTItem() # Add a histogram with which to control the gradient of the image
        self.hist.setImageItem(self.img_spectrum)
        self.hist.setLevels(np.min(-5), np.max(5)) # Fit the min and max levels of the histogram to the data available
        self.hist.gradient.restoreState(  # This gradient is roughly comparable to the gradient used by Matplotlib # You can adjust it and then save it using hist.gradient.saveState()
                {'mode': 'rgb',
                'ticks': [(0.5, (0, 182, 188, 255)),
                        (1.0, (246, 111, 0, 255)),
                        (0.0, (75, 0, 113, 255))]})
        
        ##  qt update timer
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updatePlotWidget)
        self.timer.start(200)

    def updatePlotWidget(self):
        self.first_Plt.clear()
        self.second_Plt.clear()
        self.third_Plt.clear()

        if len(self.f_hr) > 0 :
            ## heart rate waveform
            self.f_hr = self.f_hr*60.
            self.first_Plt.plot(np.column_stack((self.f_hr,self.P_den_hr)))
            self.first_Plt.plot(np.column_stack((self.f_hr,self.P_den_filter)),pen='g')

            ## rPPG signal
            self.second_Plt.plot(self.hr_rPPG_signal)

            ## motion X/Y FFT
            self.third_Plt.plot(self.P_den_y,pen='b')
            self.third_Plt.plot(self.P_den_x,pen='r')
        
        if len(self.Sxx_arr) > 30:
            ## heart rate spectrum
            spectrumArray = np.array(self.Sxx_arr.copy())
            self.img_spectrum.setImage(spectrumArray)