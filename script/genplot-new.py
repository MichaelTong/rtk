#!/usr/bin/python

import sys
import os

folder = sys.argv[1]
raws = os.listdir("raw/" + folder);

plot_header = """
set term postscript eps color 20
set key right bottom
set xlabel "Latency (ms)"
set size 0.5, 0.65
set tics out
set key bot right
"""

plot_title = 'set title "{}"\n'
plot_xrange = 'set xrange [{}]\n'
plot_yrange = 'set yrange [{}]\n'
plot_ytics = 'set ytics ({})\n'
plot_output = 'set output "eps/{}"\n'#.format(folder.eps)
plot_files = 'plot \\\n'
plot_file_path = "'dat/{}/{}' u ($1/1000):2 " #.format(folder, file.dat)
plot_file_format = 't "{}" w l lc rgb "{}" lw {} dt {}, \\\n'#.format(title, color, lw, dt)
#'set xrange [0:100]'
#'set yrange [0.9:1]'
#'set ytics ("1"   1,    ".99" 0.99, ".98" 0.98, ".97" 0.97, ".96" 0.96, \
#           ".95" 0.95, ".94" 0.94, ".93" 0.93, ".92" 0.92, ".91" 0.91, \
#           ".90" 0.90)'
#20161220_1136-1-warmup-s1
alter = folder.split('-')[2]
altered = '-'.join(folder.split('-')[3:])
tics = """ "1"   1,    ".99" 0.99, ".98" 0.98, ".97" 0.97, ".96" 0.96, \\
            ".95" 0.95, ".94" 0.94, ".93" 0.93, ".92" 0.92, ".91" 0.91, \\
            ".90" 0.90 """

plot_title = plot_title.format(alter + ": " + altered)
plot_xrange = plot_xrange.format("0:100")
plot_yrange = plot_yrange.format("0.9:1")
plot_ytics = plot_ytics.format(tics)
plot_output = plot_output.format(folder + ".eps")

#print folder
for r in raws:
  if r.endswith(".log"):
    datfile = r[:-4] + ".dat"
    if "def" in datfile:
      title = "def"
      color = "red"
    elif "gct" in datfile:
      title = "gct"
      color = "blue"
    elif "ebusy" in datfile:
      title = "ebusy"
      color = "green"
    elif "nogc" in datfile:
      title = "nogc"
      color = "gray"
    lw = 8
    dt = 1
    plot_files += plot_file_path.format(folder, datfile) + plot_file_format.format(title, color, lw, dt)

plot_fp = open("plot/" + folder + ".plot", "wb")
plot_fp.write(plot_header)
plot_fp.write(plot_title)
plot_fp.write(plot_xrange)
plot_fp.write(plot_yrange)
plot_fp.write(plot_ytics)
plot_fp.write(plot_output)
plot_fp.write(plot_files)
plot_fp.close()


