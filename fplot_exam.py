#!/usr/bin/env python

"""python script for plotting a function

Author: Jinyun Tang <jinyuntang@gmail.com>

"""



from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
from matplotlib.backends.backend_pdf import PdfPages

pdf=PdfPages('foo.pdf')
fig = plt.figure()
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
pdf.savefig(fig)
pdf.close()
