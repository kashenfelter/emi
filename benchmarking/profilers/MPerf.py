
# wrapper around memory_profiler

from memory_profiler import profile

class MPerf( ):
    ''' 
    global state object to hold all benchmark functions, plus some utility
    methods for running and formatting according to line by line profiling
    '''    
    
    def __init__(self, function, out="logging.out"):
        ''' registers a function in the overall state object '''
        self.func = function

    def __call__( self, *args ):
        ''' instance of class getting called triggers this, i.e. a decorated function '''
        self.func = profile(selffunc)
        self.func( )
        self.printCSVInstance(elapsed, args[0])

    def printCSVInstance( self, output, outfile ):
        with open( outfile, "w" ) as f:
            # output = "elapsed time was: " + str(output)
            f.write(output)