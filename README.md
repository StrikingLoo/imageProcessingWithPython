Image processing projects in Python using PIL.

filters.py has two small methods that, given a picture, will either return its negative version or apply a filter that will turn all its pixels to a given hue, maintaining brightness.
For instance a picture of a grey circle on a darker grey background, given the 'blue' hue (0,0,255), will return a light-blue circle on a blue background.

compress.py is my first incursion into image compression algorithms, and applies the basic principle of Kolmogorov's Complexity to reduce the size of some images. Given the simplicity of the algorithm it will work really well for some images but awfully bad for others (even as bad as to return a heavier file than the supplied one!). Nonetheless this program does provide an elegant way of generating simple images from .txt files, which is what I wanted.

fractal.py generates Mandelbrot Fractals of a given resolution. It is a bit slow for a big enough resolution, since it is a computationally tasking process.


ultimateFractal.jpg was created with fractal.py, and it's negative version is just the result of applying the negative filter to it.
