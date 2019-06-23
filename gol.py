#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from tkinter import *
from tkinter import filedialog
import threading
import math

GSIZE = 50

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

class Point:
    def __init__(self, ix):
        pass


class FileReader:

    def parsePoints(self, fin):
        p = set()
        for line in fin.readlines():
            tmp = line.split(',')
            p.add((int(tmp[0]), int(tmp[1])))
        return p

    def openState(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\\Users\\W\\Documents\\repos\\gameOfLife\\Presets"
        # the filetype mask (default is all files)
        mask = \
            [("Game Of Life files (.gol)", "*.gol"),
             ("All files", "*.*")]
        fin = filedialog.askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
        return (self.parsePoints(fin))

    def saveState(self, points):
        """open a file and write"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\\Users\\W\\Documents\\repos\\gameOfLife\\Presets"
        # the filetype mask (default is all files)
        mask = \
            [("Game Of Life files (.gol)", "*.gol"),
             ("All files", "*.*")]
        fin = filedialog.asksaveasfilename(initialdir=initial_dir, filetypes=mask)
        if (not fin.endswith(".gol")):
            fin = fin + ".gol"
        mfile = open(fin, 'w')
        for p in points:
            mfile.write(str(p[0]) + "," + str(p[1])+"\n")
        mfile.close()


class Board(FileReader):

    _activePos = set()
    _potentialPos = set()
    _frameRate = 2
    _tFrame = _frameRate / 2
    _running = 0
    color = ""
    allColours = False
    colourCycle = 0

    def __init__(self, b, size, c):
        self._activePos = b
        self._size = size
        self._frames = []
        self._defBoard = b.copy()
        self._potentialPos = b
        self._colour = c
        self._colours = COLORS
        self.hiLim = int(size / 2 - 1)
        self.loLim = int(-size / 2)

    def SaveBoard(self):
        if self._running:
            return
        self.saveState(self._activePos)

    def LoadBoard(self):
        if self._running:
            return
        points = self.openState()
        if points:
            self.CleanBoard()
            self._activePos = points
            self._potentialPos = points.copy()
            self.printBoard()



    def SetColour(self, event):
        colour = event.widget.curselection()
        if colour[0] == 0:
            self.allColours = True
            return
        else:
            self.allColours = False
            self._colour = self._colours[colour[0]]
            print(colour[0])

    def ResetBoard(self):
        if self._running:
            self._running = 0
        if (self._activePos):
            for p in self._activePos:
                if self.point2ix(p) in range(0, self._size * self._size):
                    self._frames[self.point2ix(p)].configure(bg="white")
            self._activePos.clear()
        self._activePos = self._potentialPos = self._defBoard.copy()
        self.printBoard()

    def CleanBoard(self):
        if self._running:
            self._running = 0
        if self._activePos:
            self.printBoard(True)
            self._activePos.clear()

    def addFrame(self, frame):
        self._frames.append(frame)

    def lClick(self, event):
        frame = event.widget
        ix = self._frames.index(frame)
        p = self.ix2point(ix)
        print("ix ", ix)
        print("point ", p)
        if p in self._activePos:
            frame.configure(bg="white")
            self._activePos.remove(p)
        else:
            frame.configure(bg=self._colour)
            self._activePos.add(p)

    #This is probably broken
    def point2ix(self, point):
        x, y = point
        x = x + self._size / 2 - 1
        y = y + self._size / 2
        ix = x + y * self._size + 1
        return int(ix)

    def ix2point(self, ix):
        y = int(math.floor(ix / self._size) - self._size / 2)
        x = int(ix % self._size - self._size / 2)
        return (x,y)

    def NeighboursAndSelf(self, point):
        x, y = point
        yield (x-1, y-1)
        yield (x, y-1)
        yield (x+1, y-1)
        yield (x-1, y)
        yield (x+1, y)
        yield (x-1, y+1)
        yield (x, y+1)
        yield (x+1, y+1)
        #yield (x,y)

    def NewEmptyBoard(self):
        newBoard = set()
        for l in self._activePos:
            neighbourGen = self.NeighboursAndSelf(l)
            for p in neighbourGen:
                newBoard.add(p)
        self._potentialPos = newBoard.union(self._activePos)

    def evolve(self):
        nextBoard = set()
        self.NewEmptyBoard()
        for p in self._potentialPos:
            nActive = 0
            neighbourGen = self.NeighboursAndSelf(p)
            for op in neighbourGen:
                if (op in self._activePos):
                    nActive = nActive + 1
            # print(p," has " , nActive," n of neighbors")
            if ((nActive == 3 or (nActive == 2 and (p in self._activePos))) and op[0] in range(self.loLim+1, self.hiLim+2) and op[1] in range(self.loLim+1, self.hiLim+2)):
                nextBoard.add(p)
        self._activePos = nextBoard

    def printBoard(self, clean=False):
        if self.allColours:
            self._colour = self._colours[self.colourCycle]
            self.colourCycle = self.colourCycle + 1
            if self.colourCycle > len(self._colours) - 1:
                self.colourCycle = 0
        if clean:
            for po in self._activePos:
                self._frames[self.point2ix(po)].configure(bg="white")
            return
        for tp in self._potentialPos:
            ix = self.point2ix(tp)
            if ix < len(self._frames) - 1:
                if tp in self._activePos:
                    self._frames[ix].configure(bg=self._colour)
                else:
                    self._frames[ix].configure(bg="white")


    def RunEvolution(self):
        while(self._running):
            self.evolve()
            self.printBoard()
            time.sleep(self._tFrame)
        print("Done")

    def Start(self, frames):
        #frames[1].configure(bg="yellow")
        if (not self._running):
            self._running = 1
            to = threading.Thread(target=self.RunEvolution, args=(), daemon=True)
            to.start()
            print("Evolution started")

    def StopEvolution(self):
        self._running = 0

    def GetFrameRate(self):
        return self._frameRate

    def SetFrameRate(self, val):
        self._frameRate = int(val)
        self._tFrame = 1 / self._frameRate

    def GetBoard(self):
        return self._activePos


def main():
    gridSize = GSIZE
    nPixelsPerBtn = 18

    win = Tk()
    win.title("Game of life")
    winSize = str(gridSize * nPixelsPerBtn ) + "x" + str(gridSize * nPixelsPerBtn+50)
    win.resizable(False, False)
    win.geometry(winSize)

    Grid.rowconfigure(win, 0, weight=1)
    Grid.columnconfigure(win, 0, weight=1)
    frame = Frame(win, background="gray20")
    frame.grid(sticky=N+E+W)
    frameLower = Frame(win)
    frameLower.grid(sticky=S+W)

    frames = []
    b = Board(set([(0, 0), (-1,0), (1, 0), (0, 1)]), gridSize, "blue2")
    print(Board.point2ix(b, (-15, -7)))

    for y in range(1,gridSize+1):
        pass
        Grid.rowconfigure(frame, y, weight=1)
        for x in range(1,gridSize+1):
            Grid.columnconfigure(frame, x, weight=1)
            fr = Frame(frame, width=nPixelsPerBtn, height=nPixelsPerBtn, bg="white")
            fr.grid(row=y, column=x, padx=0.6, pady=0.6)
            fr.bind("<Button-1>", b.lClick)
            b.addFrame(fr)
    b.printBoard()

    btnWidth = 14
    Button(frameLower, text="Start", width=btnWidth, command=lambda: b.Start(frames)).grid(row=0, column=0, sticky=W)
    Button(frameLower, text="Pause", width=btnWidth, command=b.StopEvolution).grid(row=0, column=1, sticky=W)
    Button(frameLower, text="Reset", width=btnWidth, command=b.ResetBoard).grid(row=0, column=2, sticky=W)
    Button(frameLower, text="Save", width=btnWidth, command=b.SaveBoard).grid(row=0, column=3, sticky=W)
    Button(frameLower, text="Load", width=btnWidth, command=b.LoadBoard).grid(row=0, column=4, sticky=W)

    Button(frameLower, text="Clean", width=btnWidth, command=b.CleanBoard).grid(row=1, column=2, sticky=W)



    Grid.columnconfigure(frameLower, 5, pad= str(gridSize* nPixelsPerBtn - 3 * btnWidth*10))

    Button(frameLower, text="Exit", width=btnWidth, command=win.quit).grid(row=2, column=4, sticky=E)
    listbox = Listbox(frameLower, height=4, width=14)
    listbox.insert(END,'Special')

    for item in COLORS:
        listbox.insert(END, item)
    listbox.grid(row = 2, column = 1)
    listbox.bind("<<ListboxSelect>>", b.SetColour)
    slider = Scale(frameLower, from_=1, to=15, orient=HORIZONTAL, command=b.SetFrameRate, showvalue=0, label="Speed")
    slider.grid(row=2, column=0, sticky=W)
    slider.set(b.GetFrameRate())

    win.mainloop()


main()
