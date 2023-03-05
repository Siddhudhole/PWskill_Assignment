#!/usr/bin/env python
# coding: utf-8

# Q1. How can you create a Bokeh plot using Python code?

# In[1]:


import bokeh 
import bokeh.io
import bokeh.plotting 


# In[2]:


bokeh.io.output_notebook()


# In[3]:


from bokeh.plotting import figure,output_file,show 


# In[4]:


x = [1,2,3,4,5]
y = [6,7,8,9,0]


# In[6]:


output_file('try.html')
p = figure(title='line Graph ')
p.xaxis.axis_label ='X-AXIS'
p.yaxis.axis_label = 'Y-AXIS'
p.line(x,y)
show(p) 


# Q2. What are glyphs in Bokeh, and how can you add them to a Bokeh plot? Explain with an example.

# In Bokeh, glyphs are graphical shapes used to represent data points, such as circles, squares, triangles, lines, and more. Glyphs can be added to a Bokeh plot using the glyph method of the figure object.

# In[8]:


output_file ('test2.html')
s = figure(title='circle')
s.xaxis.axis_label = 'X' 
s.yaxis.axis_label = 'Y'
s.circle(x,y)
show(s)


# Q3. How can you customize the appearance of a Bokeh plot, including the axes, title, and legend?

# In[9]:


output_file('test3.html')
d = figure(title='scatter')
d.xaxis.axis_label = 'x'
d.xaxis.axis_label_text_font_size = '10pt'
d.yaxis.axis_label = 'Y'
d.yaxis.axis_label_text_font_size = '10pt'
d.scatter(x,y)
show(d)


# Q4. What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
# real time?

# A Bokeh server is a way to create and deploy interactive Bokeh plots that can be updated in real time. The Bokeh server allows you to create web applications that generate Bokeh plots and update them dynamically in response to user input, such as clicking a button, sliding a slider, or selecting a value from a dropdown menu. The Bokeh server works by running a Python script on a web server that generates the plot and handles user interactions, and then sends the plot to a web browser for display.

# Q5. How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?

# In[ ]:


from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure

app = Flask(__name__)

@app.route('/')
def index():
   
    plot = figure()
    plot.circle([1, 2, 3], [4, 5, 6])

    
    script, div = components(plot)

    
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run()

