#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:25:26 2023

###################################
#                                 #
#      GRAFICADOR GENERICO        #
#      MODULO PARA IMPORTAR       #  
#                                 #
###################################

@author: Franco Neme
"""

# %% LIBRERÍAS DEL MÓDULO
# =======================

# import decimal
# from matplotlib import ticker
# from matplotlib.ticker import AutoMinorLocator
# import numpy as np
# import pandas as pd
# import os

import matplotlib.pyplot as plt




#%% 

class Graficas:
    
    def __init__(self):
        
        # Atributos de Clase
        # -------------------
        
        # ___Tamaño y calidad

        self.Alto = 9/2.54 #plg
        self.Ancho = 9/2.54 #plg
        self.cal = 300 #dpi

        # ___Posición de bordes del subplot, con respecto a tamaño total ancho o alto

        self.fb_top = 0.92
        self.fb_bot = 0.28
        self.fb_left = 0.17
        self.fb_right = 1 - self.fb_left

        # ___Tamaño general de fuente

        self.fnt_gen = 12 #pt
        
        # ___Tamaño y color de las lineas/marcas por default

        self.mrk_sze = 6
        self.col = 'k'
        
        # ___Titulo del eje de la absisa

        self.X_fmt = "{x:.0f}"	# Formato en string.
        
        # ___Titulo del eje de la ordenada
        
        self.Y_fmt = "{x:.1f}"	# Formato en string.
        
        # ___Limite inferior en x

        self.X_min = 0
        
        # ___Limite inferior en y
        
        self.Y_min = 0
                    
        # ___Valores por default de la funcion grf
        
        self.tit_x = 'x'
        self.tit_y = 'y'
        self.ln = True
        self.pt = False
        self.lnsty = 'solid'
        self.mrk = 'None'
        self.fig_name = ''
        
        self.vr = {'tit_x': self.tit_x, 'tit_y': self.tit_y, 'ln': self.ln, 'pt': self.pt, 'fig_name': self.fig_name}
       
        
    def grf(self, x, y, **kwargs):
        '''
        **kwargs: tit_x = str(), tit_y = str(), ln = bool(), pt = bool(), fig_name = str().
        Por default: pt = False, ln = True, fig_name = ''.
        '''
        
        if kwargs:
            
            for i in kwargs:
                
                if i in self.vr:
                    
                    self.vr[i] = kwargs[i]
        
        
        if self.vr['pt'] == True:
            
            self.mrk = 'x'
        
        if self.vr['ln'] == False:
            
            self.lnsty = 'None'

        fig, ax = plt.subplots(figsize=(self.Ancho, self.Alto))  # Create a figure and an axes.
        
        plt.subplots_adjust(left=self.fb_left, top=self.fb_top) # Posición de bordes del subplot, fracción de ancho/alto total.
        plt.subplots_adjust(right=self.fb_right, bottom=self.fb_bot) # Posición de bordes del subplot, fracción de ancho/alto total. bottom=0.15 sin leyenda afuera, abajo.
        
        
        ax.plot(x, y, marker=self.mrk, color=self.col, linestyle = self.lnsty, markersize=self.mrk_sze, markeredgecolor=self.col)
        

        ax.set_xlabel(self.vr['tit_x'], fontsize = self.fnt_gen, fontweight='bold')
        ax.set_ylabel(self.vr['tit_y'], fontsize = self.fnt_gen, fontweight='bold')
        
        x_tit = self.vr['tit_x'].split(' ')
        y_tit = self.vr['tit_y'].split(' ')
        
        ax.set_title(y_tit[0] + ' vs ' + x_tit[0], fontsize = self.fnt_gen, fontweight='bold')
        
        # ___Absisas

        # plt.xlim(self.X_min)
        # ax.xaxis.set_major_locator(plt.MultipleLocator(self.X_Lmaj))
        # ax.xaxis.set_major_formatter(ticker.StrMethodFormatter( self.X_fmt ))
        # ax.xaxis.set_minor_locator(plt.MultipleLocator(self.X_Lmin))
        # ax.xaxis.set_minor_locator(AutoMinorLocator(2))
        
        # ___Ordenada

        # ax.set_ylim(self.Y_min)
        # ax.yaxis.set_minor_locator(AutoMinorLocator(2))

        # ___Formato de los minor y major ticks

        # ax.xaxis.set_ticks_position('bottom')
        # ax.yaxis.set_ticks_position('left')
        # ax.tick_params(axis='x', labelsize=6)
        # ax.tick_params(axis='y', labelsize=6)
        
        # ax.tick_params(which='both', direction='inout')
        # ax.tick_params(which='major', width=1.00/1.5, length=5/1.5)
        # ax.tick_params(which='minor', width=0.75/1.5, length=2.5/1.5, labelsize=5/1.5)    
        
        self.lnsty = 'solid'
        self.mrk = 'None'


        if len(self.vr['fig_name']) > 0:

            self.figure = plt.gcf()

            plt.savefig(self.vr['fig_name'], dpi=self.cal, bbox_inches='tight')
        
        
        p = plt.show()
        
        self.vr = {'tit_x': self.tit_x, 'tit_y': self.tit_y, 'ln': self.ln, 'pt': self.pt, 'fig_name': self.fig_name}

        return p


#%%   
