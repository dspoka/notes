
# coding: utf-8

# In[16]:

get_ipython().run_cell_magic(u'latex', u'', u'$$c = \\sqrt{a^2 + b^2}$$\n$$\\begin{array}{|c|c|c|}\n\\hline\\\\\n5&5&23523452\\\\\n\\hline\\\\\n5 & d & 3241\\\\\n\\hline\n\\end{array}$$')


# In[17]:

from IPython.core.display import Math
Math(r'$F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx$')


# In[2]:

get_ipython().run_cell_magic(u'latex', u'', u'$${\\bf worksheets.codalab.org}$$\n\\[ x^n + y^n = z^n \\]\n\\begin{equation}\n\n\\int \\sum \\prod\n< > \\subset \\supset \\subseteq \\supseteq\n\\\\\\int_{a}^{b} x^2 dx\n\\\\ \\sum_{i=1}^{\\infty} \\frac{1}{n^s} \n\\\\ \\prod_{i=1}^n\n\\end{equation}\n\n\n')


# ---
# 
# *Italics?*
# 
# There are some things you might want to consider before you build your solution and raise venture capital:
# 
# **Background:**
# 
# * item
# * item
# 
# As defined, an ocean current is a directed movement of ocean water. 
# 
# ---
# 
# ![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
# 
# 
# \- Daniel
# 
# **Resources:**
# 
# <a href="http://oceanservice.noaa.gov/education/tutorial_currents/welcome.html"> Ocean Service Currents Tutorial</a>
# <br>
# <a href="http://www.divediscover.whoi.edu/history-ocean/maury.html"> Dive Discover</a>
# <br>
# <a href="http://www.seasky.org/ocean-exploration/ocean-explorers-matthew-maury.html"> Sea Sky </a>
# <br>
# <a href="https://en.wikipedia.org/wiki/Matthew_Fontaine_Maury">Wiki Matthew Maury</a>
# <br>
# <a href="http://oceanmotion.org/html/background/timeline1800.html"> Ocean Motion Timeline</a>
# 
# 

# In[4]:

import pydot
example_graph = "1_example_graph.png"
graph = pydot.Dot(graph_type='digraph')
node_a = pydot.Node("Node A", style="filled", fillcolor="red")
node_b = pydot.Node("Node B", style="filled", fillcolor="green")
node_c = pydot.Node("Node C", style="filled", fillcolor="#0000ff")
node_d = pydot.Node("Node D", style="filled", fillcolor="#976856")
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
graph.add_node(node_d)
graph.add_edge(pydot.Edge(node_a, node_b))
graph.add_edge(pydot.Edge(node_b, node_c))
graph.add_edge(pydot.Edge(node_c, node_d))
graph.add_edge(pydot.Edge(node_d, node_a, label="and back we go again", labelfontcolor="#009933", fontsize="10.0", color="blue"))
graph.write_png(str(example_graph))


# ![Image of Yaktocat](./1_example_graph.png)
# 

# In[80]:

# throw this in terminal to kick cluster
# ipcluster start -n 4
import os
import ipyparallel as ipp

rc = ipp.Client()
ar = rc[:].apply_async(os.getpid)
pid_map = ar.get_dict()
print pid_map


# In[ ]:



