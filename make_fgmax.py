"""
Create fgmax_grid.txt and fgmax_transect input files 
"""


from clawpack.geoclaw import fgmax_tools


def make_fgmax_grid():
    fg = fgmax_tools.FGmaxGrid() 
    fg.point_style = 2       # will specify a 2d grid of points
    fg.x1 = -123.48      # west
    fg.x2 = -123.34     #east
    fg.y1 = 48.103      # south
    fg.y2 = 48.146       #north
    fg.dx = 0.000700        #resolution in degrees
    fg.tstart_max =  0     # when to start monitoring max values
    fg.tend_max = 1.e10       # when to stop monitoring max values
    fg.dt_check = 0         # target time (sec) increment between updating 
                               # max values
    fg.min_level_check = 4    # which levels to monitor max on
    fg.arrival_tol = 1.e-2    # tolerance for flagging arrival

    fg.input_file_name = 'InundationMap.txt' #White House
    fg.write_input_data()

  
    

if __name__ == "__main__":
    make_fgmax_grid()
