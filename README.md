# 3D-Engine-OpenGL
This project utilizes the Modern Gl library and PyGame to create a 3D engine that can render objects when given a .obj, .mtl, and texture file. In this project, most of the code logic is abstracted into separate classes, making it extremely easy to add extra objects to the 3D rendered space. To render the scene, simply run the main.py file. When you enter the rendered space, you can use the wasd keys to move your camera around and adjust your height using the q and e keys. You can also adjust the camera settings and adjust your movement velocitym, foc, etc. in the 3D space. To exit the rendered space, press the escape key.


![turtle_render](https://user-images.githubusercontent.com/64037087/188527839-19473710-2ed2-4b5b-9cf2-663b289bad66.jpg)


## Advantages of using ModernGL compared to PyOpenGL:
* Simpler and faster than PyOpenGL
* Can render without a window
* 100% Pythonic


## OpenGL Rendering PipeLine
Vertices -> Vertex Shader -> Primitive Assembly -> Rasterization -> Fragment Shader -> Tests -> FrameBuffer


## Project Dependencies
- ModernGl
- Pygame
- Numpy
- pywavefront
