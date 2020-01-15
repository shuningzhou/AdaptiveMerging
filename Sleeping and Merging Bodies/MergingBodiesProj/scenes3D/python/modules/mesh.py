import xml.etree.ElementTree as ET
import general

class Mesh():

    def __init__(self, root, obj, name="mesh", position="0 0 0", orientation="0. -1 0. 0.", velocity="0. 0. 0.", omega="0. 0. 0.", scale="1", st=None, pinned="false", magnetic="false", density="1", restitution=None, friction=None, color=None):
        # Fixed body
        self.body = general.body(root, "mesh", name, position, orientation, velocity=velocity, omega=omega, obj=obj, scale=scale, pinned=pinned, magnetic=magnetic, density=density, restitution=restitution, friction=friction, color=color)

    def addSpring(self, positionB="0 0 0", k="100", d="10", body2=None, positionW=None, positionB2=None):
        spring = ET.SubElement(self.body, 'spring')
        spring.set('pB', positionB)
        spring.set('k', k)
        spring.set('d', d)

        if (body2!=None and positionB2!=None):
            spring.set('body2', body2)
            spring.set('pB2', positionB2)

        if (positionW!=None):
            spring.set('pW', positionW)

    def get(self):
        return self.body
