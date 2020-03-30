import numpy as np
#import matplotlib.pyplot as plt
import scipy.constants as c
 
# Code for radial wavefunction:
a = c.physical_constants['Bohr radius'][0]
 
 
###Code:
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return round(x, 5), round(y, 5), round(z, 5)
 
 
def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return round(r, 5), round(theta, 5), round(phi, 5)
 
 
# Test:
# assert statement will throw error if the result is wrong
# no output will be produced for correct results
 
### Code for angular wavefunction:
def angular_wave_func(m, l, theta, phi):
    def sqrt(v):
        return np.sqrt(v)
 
    def cos(v):
        return np.cos(v)
 
    def sin(v):
        return np.sin(v)
 
    def exp(v):
        return np.exp(v)
 
    pi = np.pi
    i = complex(0, 1)
 
    if l == 0 and m == 0:
        y = sqrt(1 / 4 / pi)
        return np.complex(np.round(y, 5))
    elif l == 1:
        if m == 0:
            y = sqrt(3 / 4 / pi) * cos(theta)
            return np.complex(np.round(y, 5))
        elif m == 1:
            y = - sqrt(3 / 8 / pi) * sin(theta) * exp(i * phi)
            return np.complex(np.round(y, 5))
        elif m == -1:
            y = sqrt(3 / 8 / pi) * sin(theta) * exp(-i * phi)
            return np.complex(np.round(y, 5))
        else:
            return -1
    elif l == 2:
        if m == 0:
            y = sqrt(5 / 16 / pi) * (3 * (cos(theta)) ** 2 - 1)
            return np.complex(np.round(y, 5))
        elif m == 1:
            y = - sqrt(15 / 8 / pi) * cos(theta) * sin(theta) * exp(i * phi)
            return np.complex(np.round(y, 5))
        elif m == -1:
            y = sqrt(15 / 8 / pi) * cos(theta) * sin(theta) * exp(-i * phi)
            return np.complex(np.round(y, 5))
        elif m == 2:
            y = sqrt(15 / 32 / pi) * (sin(theta)) ** 2 * exp(i * 2 * phi)
            return np.complex(np.round(y, 5))
        elif m == -2:
            y = sqrt(15 / 32 / pi) * (sin(theta)) ** 2 * exp(-i * 2 * phi)
            return np.complex(np.round(y, 5))
        else:
            return -1
    elif l == 3:
        if m == 0:
            y = sqrt(7 / 16 / pi) * (5 * (cos(theta)) ** 3 - 3 * cos(theta))
            return np.complex(np.round(y, 5))
        elif m == 1:
            y = -sqrt(21 / 64 / pi) * sin(theta) * (5 * (cos(theta) ** 2 - 1)) * exp(i * phi)
            return np.complex(np.round(y, 5))
        elif m == -1:
            y = sqrt(21 / 64 / pi) * sin(theta) * (5 * (cos(theta)) ** 2 - 1) * exp(-i * phi)
            return np.complex(np.round(y, 5))
        elif m == 2:
            y = sqrt(105 / 32 / pi) * cos(theta) * (sin(theta)) ** 2 * exp(i * 2 * phi)
            return np.complex(np.round(y, 5))
        elif m == -2:
            y = sqrt(105 / 32 / pi) * cos(theta) * (sin(theta)) ** 2 * exp(-i * 2 * phi)
            return np.complex(np.round(y, 5))
        elif m == 3:
            y = -sqrt(35 / 64 / pi) * (sin(theta)) ** 3 * exp(i * 3 * phi)
            return np.complex(np.round(y, 5))
        elif m == -3:
            y = sqrt(35 / 64 / pi) * (sin(theta)) ** 3 * exp(-i * 3 * phi)
            return np.round(y, 5)
        else:
            return -1
    else:
        return -1
 
 
def radial_wave_func(n, l, r):
    sigma = r / a
 
    def sqrt(v):
        return np.sqrt(v)
    def exp(v):
        return np.exp(v)
 
    if l == 0:
        if n == 1:
            r_1s = 2 * (1/ a) ** (1.5) * exp(-sigma)
            return round(r_1s, 5)
        elif n == 2:
            r_2s = 1 / sqrt(2) * (1 / a) ** (1.5) * (1 - sigma/2) * exp(-sigma / 2)
            return round(r_2s, 5)
        elif n == 3:
            r_3s = 2 / 81 / sqrt(3) * (1 / a) ** (1.5) * (27 - 18 * sigma + 2 * sigma ** 2) * exp(- sigma / 3)
            return round(r_3s, 5)
        elif n == 4:
            r_4s = 1 / 4 * (1 / a) ** (1.5) * (1 - 3 / 4 * sigma + 1 / 8 * sigma ** 2 - 1 / 192 * sigma ** 3) * exp(- sigma / 4)
            return round(r_4s, 5)
        else:
            return -1
    elif l == 1:
        if n == 2:
            r_2p = 1 / 2 / sqrt(6) * (1 / a) ** (1.5) * sigma * exp(- sigma / 2)
            return round(r_2p, 5)
        elif n == 3:
            r_3p = 8/ 27 / sqrt(6) * (1 / a) ** (1.5) * (sigma) * ( 1- sigma/6) * exp(- sigma / 3)
            return round(r_3p, 5)
        elif n == 4:
            r_4p = sqrt(5) / 16 / sqrt(3) * (1 / a) ** (1.5) * (sigma) * (1 - 1 / 4 * sigma + 1 / 80 * sigma ** 2) * exp(- sigma / 4)
            return round(r_4p, 5)
        else:
            return -1
    elif l == 2:
        if n == 3:
            r_3d = 4 / 81 / sqrt(30) * (1 / a) ** (1.5) * sigma ** 2 * exp(- sigma / 3)
            return round(r_3d, 5)
        elif n == 4:
            r_4d = 1 / 64 / sqrt(5) * (1 / a) ** (1.5) * sigma ** 2 * (1 - 1 / 12 * sigma) * exp(- sigma / 4)
            return round(r_4d, 5)
        else:
            return -1
    elif l == 3:
        if n == 4:
            r_4f = 1 / 768 / sqrt(35) * (1 / a) ** 1.5 * sigma ** 3 * exp(- sigma / 4)
            return round(r_4f, 5)
    else:
        return -1
 
 
def mgrid3d(xstart, xend, xpoints,
            ystart, yend, ypoints,
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0
 
    # calculate the step size for each axis
    xstep = (xend - xstart) / (xpoints - 1)
    ystep = (yend - ystart) / (ypoints - 1)
    zstep = (zend - zstart) / (zpoints - 1)
 
    while xcount < xpoints:
        # initialize y points
        # create temporary variable to store x, y and z list
        yval = ystart
        ycount = 0
 
        xrow = []
        yrow = []
        zrow = []
 
        while ycount < ypoints:
            # initialize z points
            # create temporary variable to store the inner x, y, and z list
            zval = zstart
            zcount = 0
 
            innerxrow = []
            inneryrow = []
            innerzrow = []
 
            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                innerxrow.append(xval)
                inneryrow.append(yval)
                innerzrow.append(zval)
 
                # increase z point
                zval += zstep
                zcount += 1
            # add the inner most lists to the second lists
            xrow.append(innerxrow)
            yrow.append(inneryrow)
            zrow.append(innerzrow)
 
            # increase y point
            yval += ystep
            ycount += 1
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)
 
        # increase x point
        xval += xstep
        xcount += 1
 
    return [xr, yr, zr]
 
 
###Code:
def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
    xr, yr, zr = mgrid3d(-roa, roa, Nx, -roa, roa, Ny, -roa, roa, Nz)
    density = []
 
    i = complex(0, 1)
    for h in range(Nx):
        outerrow = []
        for i in range(Ny):
            innerrow = []
            for j in range(Nz):
                xx = xr[h][i][j]
                yy = yr[h][i][j]
                zz = zr[h][i][j]
 
                r, theta, phi = cartesian_to_spherical(xx, yy, zz)
                Y_lm = angular_wave_func(m, l, theta, phi)
                Y_lm_neg = angular_wave_func(-m, l, theta, phi)
 
                if m < 0:
                    Y = (i / np.sqrt(2)) * (Y_lm_neg + Y_lm)
                elif m == 0:
                    Y = Y_lm
                elif m > 0:
                    Y = (1 / np.sqrt(2)) * (Y_lm_neg - Y_lm)
 
                Y = Y
                R_nl = radial_wave_func(n, l, r * a) * Y
                probdensity = np.real(R_nl ** 2)
                wave = round(probdensity, 5)
                innerrow.append(wave)
            outerrow.append(innerrow)
        density.append(outerrow)
    x = np.array(xr)
    y = np.array(yr)
    z = np.array(zr)
    mag = np.array(density)
    return x, y, z, mag
 
 
# Code to save the data to a file so that
# you don't have to keep on computing it:
 
print('Test ')
x, y, z, mag = hydrogen_wave_func(4, 3, -3, 40, 100, 100, 100)
print('x, y, z:')
print(x, y, z)
print('mag:')
print(mag)
print(x, y, z, mag)
x.dump('x_test.dat')
y.dump('y_test.dat')
z.dump('z_test.dat')
mag.dump('den_test.dat')
 
# Mayavi code:
 
from mayavi import mlab
 
mu, sigma = 0, 0.1
x = np.load('x_test.dat', allow_pickle=True)
y = np.load('y_test.dat', allow_pickle=True)
z = np.load('z_test.dat', allow_pickle=True)
 
density = np.load('den_test.dat', allow_pickle=True)
figure = mlab.figure('DensityPlot')
pts = mlab.contour3d(density, contours=40, opacity=0.4)
mlab.axes()
mlab.show()
 
###Volume slicer code:
import numpy as np
 
from traits.api import HasTraits, Instance, Array, \
    on_trait_change
from traitsui.api import View, Item, HGroup, Group
 
from tvtk.api import tvtk
from tvtk.pyface.scene import Scene
 
from mayavi import mlab
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MayaviScene, \
                                MlabSceneModel
 
################################################################################
# Create some data
data = np.load('den_test.dat')
 
################################################################################
# The object implementing the dialog
class VolumeSlicer(HasTraits):
    # The data to plot
    data = Array()
 
    # The 4 views displayed
    scene3d = Instance(MlabSceneModel, ())
    scene_x = Instance(MlabSceneModel, ())
    scene_y = Instance(MlabSceneModel, ())
    scene_z = Instance(MlabSceneModel, ())
 
    # The data source
    data_src3d = Instance(Source)
 
    # The image plane widgets of the 3D scene
    ipw_3d_x = Instance(PipelineBase)
    ipw_3d_y = Instance(PipelineBase)
    ipw_3d_z = Instance(PipelineBase)
 
    _axis_names = dict(x=0, y=1, z=2)
 
 
    #---------------------------------------------------------------------------
    def __init__(self, **traits):
        super(VolumeSlicer, self).__init__(**traits)
        # Force the creation of the image_plane_widgets:
        self.ipw_3d_x
        self.ipw_3d_y
        self.ipw_3d_z
 
 
    #---------------------------------------------------------------------------
    # Default values
    #---------------------------------------------------------------------------
    def _data_src3d_default(self):
        return mlab.pipeline.scalar_field(self.data,
                            figure=self.scene3d.mayavi_scene)
 
    def make_ipw_3d(self, axis_name):
        ipw = mlab.pipeline.image_plane_widget(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        plane_orientation='%s_axes' % axis_name)
        return ipw
 
        def _ipw_3d_x_default(self):
            return self.make_ipw_3d('x')
 
    def _ipw_3d_y_default(self):
        return self.make_ipw_3d('y')
 
    def _ipw_3d_z_default(self):
        return self.make_ipw_3d('z')
 
    #---------------------------------------------------------------------------
    # Scene activation callbaks
    #---------------------------------------------------------------------------
    @on_trait_change('scene3d.activated')
    def display_scene3d(self):
        outline = mlab.pipeline.outline(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        )
        self.scene3d.mlab.view(40, 50)
        # Interaction properties can only be changed after the scene
        # has been created, and thus the interactor exists
        for ipw in (self.ipw_3d_x, self.ipw_3d_y, self.ipw_3d_z):
            # Turn the interaction off
            ipw.ipw.interaction = 0
        self.scene3d.scene.background = (0, 0, 0)
        # Keep the view always pointing up
        self.scene3d.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleTerrain()
 
 
    def make_side_view(self, axis_name):
        scene = getattr(self, 'scene_%s' % axis_name)
 
        # To avoid copying the data, we take a reference to the
        # raw VTK dataset, and pass it on to mlab. Mlab will create
        # a Mayavi source from the VTK without copying it.
        # We have to specify the figure so that the data gets
        # added on the figure we are interested in.
        outline = mlab.pipeline.outline(
                            self.data_src3d.mlab_source.dataset,
                            figure=scene.mayavi_scene,
                            )
        ipw = mlab.pipeline.image_plane_widget(
                            outline,
                            plane_orientation='%s_axes' % axis_name)
        setattr(self, 'ipw_%s' % axis_name, ipw)
 
        # Synchronize positions between the corresponding image plane
        # widgets on different views.
        ipw.ipw.sync_trait('slice_position',
                            getattr(self, 'ipw_3d_%s'% axis_name).ipw)
 
        # Make left-clicking create a crosshair
        ipw.ipw.left_button_action = 0
        # Add a callback on the image plane widget interaction to
        # move the others
        def move_view(obj, evt):
            position = obj.GetCurrentCursorPosition()
            for other_axis, axis_number in self._axis_names.items():
                if other_axis == axis_name:
                    continue
                ipw3d = getattr(self, 'ipw_3d_%s' % other_axis)
                ipw3d.ipw.slice_position = position[axis_number]
 
        ipw.ipw.add_observer('InteractionEvent', move_view)
        ipw.ipw.add_observer('StartInteractionEvent', move_view)
 
        # Center the image plane widget
        ipw.ipw.slice_position = 0.5*self.data.shape[
                    self._axis_names[axis_name]]
 
        # Position the view for the scene
        views = dict(x=( 0, 90),
                     y=(90, 90),
                     z=( 0,  0),
                     )
        scene.mlab.view(*views[axis_name])
        # 2D interaction: only pan and zoom
        scene.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleImage()
        scene.scene.background = (0, 0, 0)
 
 
    @on_trait_change('scene_x.activated')
    def display_scene_x(self):
        return self.make_side_view('x')
 
    @on_trait_change('scene_y.activated')
    def display_scene_y(self):
        return self.make_side_view('y')
 
    @on_trait_change('scene_z.activated')
    def display_scene_z(self):
        return self.make_side_view('z')
       
 
    #---------------------------------------------------------------------------
    # The layout of the dialog created
    #---------------------------------------------------------------------------
    view = View(HGroup(
                  Group(
                       Item('scene_y',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene_z',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                  Group(
                       Item('scene_x',
                            editor=SceneEditor(scene_class=Scene),
                            height=250, width=300),
                       Item('scene3d',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       show_labels=False,
                  ),
                ),
                resizable=True,
                title='Volume Slicer',
                )
 
 
m = VolumeSlicer(data=data)
m.configure_traits()
