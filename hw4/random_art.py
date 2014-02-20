# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
import random
from math import *
import Image

def build_random_function(min_depth, max_depth):
	""" This produces a pseud-random function of functions of depth between min_depth and max_depth. Don't put in large numbers, and make sure that min_depth is smaller than max_depth"""
	xylist = [["x"],["y"]]
	if max_depth <=1:
		return xylist[random.randint(0,1)]
	f = build_random_function(min_depth-1,max_depth-1)
	g = build_random_function(min_depth-1,max_depth-1)
	prod = ["prod",f,g]
	cos_pi = ["cos_pi",f]
	sin_pi = ["sin_pi",f]
	cube = ["^3",f]
	square = ["^2",f]
	avg = ["avg",f,g]
	funclist = [prod,cos_pi,sin_pi,cube,square,avg,["x"],["y"]]
	if min_depth>1:
		return funclist[random.randint(0,5)]
	elif min_depth <=1:
		return funclist[random.randint(0,7)]

def evaluate_random_function(f, x, y):
	""" This function evaluate a "function" list created by build_random_function(min_depth,max_depth), and returns the value of this function at (x,y)."""
	func = f[0]
	if func == "x":
		return x
	if func == "y":
		return y
	if func  == "prod":
		return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
	if func == "cos_pi":
		return cos(pi*evaluate_random_function(f[1],x,y))
	if func  == "sin_pi":
		return sin(pi*evaluate_random_function(f[1],x,y))
	if func  == "^3":
		return (evaluate_random_function(f[1],x,y))**3
	if func == "^2":
		return (evaluate_random_function(f[1],x,y))**2
	if func == "avg":
		return (evaluate_random_function(f[1],x,y)+evaluate_random_function(f[2],x,y))/2
		


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    input_interval_start = float(input_interval_start)
    input_interval_end = float(input_interval_end)
    output_interval_start = float(output_interval_start)
    output_interval_end = float(output_interval_end)
    del1 = input_interval_end - input_interval_start
    del2 = output_interval_end - output_interval_start
    return (val - input_interval_start)* del2/del1 + output_interval_start

def drawing_build(sizex,sizey,min_depth,max_depth,number):
	sizex = int(sizex)
	sizey = int(sizey)
	red = build_random_function(min_depth,max_depth)
	blue = build_random_function(min_depth,max_depth)
	green = build_random_function(min_depth,max_depth)
	im = Image.new("RGB",(sizex,sizey))
	for i in range(sizex):
		x = remap_interval(i,0.0,float(sizex),-1.0,1.0)
		for j in range(sizey):
			y = remap_interval(j,0.0,float(sizey),-1.0,1.0)
			r = evaluate_random_function(red,x,y)
			g = evaluate_random_function(green,x,y)
			b = evaluate_random_function(blue,x,y)
			rmap = remap_interval(r,-1,1,0,255)
			bmap = remap_interval(b,-1,1,0,255)
			gmap = remap_interval(g,-1,1,0,255)
			im.putpixel((i,j),(int(rmap),int(gmap),int(bmap)))
	im.save("image" + str(number) + ".bmp")			
    
drawing_build(1600,900,3,15,2)
