from bgl import *

# Widget options
BGUI_NONE = 0
BGUI_CENTERX = 1
BGUI_CENTERY = 2
BGUI_NORMALIZED = 4

BGUI_DEFUALT = BGUI_NORMALIZED

class Widget:
	"""The base widget class"""

	def __init__(self, parent, name, size=[0, 0], pos=[0, 0],
			options=BGUI_DEFUALT):
		"""The Widget constructor

		Arguments:

		parent -- the widget's parent
		name -- the name of the widget
		size -- a tuple containing the wdith and height
		pos -- a tuple containing the x and y position
		options -- various other options

		"""

		self.name = name
		self.on_click = None

		# Setup the parent
		parent._attach_widget(self)

		# A dictionary to store children widgets
		self.children = {}

		# Setup the widget's position
		self.position = [None]*4

		if options & BGUI_NORMALIZED:
			pos[0] *= parent.size[0]
			pos[1] =  parent.size[1] - (parent.size[1] * pos[1])

			size[0] *= parent.size[0]
			size[1] *= parent.size[1]

		if options & BGUI_CENTERX:
			pos[0] = parent.size[0]/2 - size[0]/2

		if options & BGUI_CENTERY:
			pos[1] = parent.size[1]/2 + size[1]/2

		x = pos[0] + parent.position[0]
		y = parent.position[1] + pos[1]
		width = size[0]
		height = size[1]
		self.size = (width, height)

		# The "friendly" position
		self.position = (x, y)

		# OpenGL starts at the bottom left and goes counter clockwise
		self.gl_position = [
					[x, y-height],
					[x+width, y-height],
					[x+width, y],
					[x, y]
					]

	def _on_click(self):
		"""Runs the on_click callback"""

		if self.on_click:
			self.on_click(self)

	def _attach_widget(self, widget):
		"""Attaches a widget to this widget"""

		if not isinstance(widget, Widget):
			raise TypeError("Expected a Widget object")

		if widget in self._widgets:
			raise ValueError("%s is attached to the system" %s (widget.name))

		self.children[widget.name] = widget

	def _draw(self):
		"""Draws the widget and the widget's children"""

		# This base class has nothing to draw, so just draw the children

		for child in self.children:
			self.children[child]._draw()