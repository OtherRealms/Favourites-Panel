# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Tool_Shelf",
    "author" : "Pablo Tochez A.",
    "description" : "Favourites and nodes ui",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "3D view 'n' Panel & node editor-> nodes",
    "warning" : "",
    "category" : "Interface"
}
import bpy

class SHELF_PT_favourites(bpy.types.Panel):
    bl_label = "Quick Favourites"
    bl_idname = "SHELF_PT_favourites"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category  = 'Quick Favourites'

    def draw(self,context):
        layout= self.layout
        flow = layout.grid_flow(row_major=False, columns=0, even_columns=False, even_rows=False, align=False)
        flow.scale_x = 0.7
        flow.menu_contents('SCREEN_MT_user_menu')

class SHELF_PT_nodes(bpy.types.Panel):
    bl_label = "Nodes"
    bl_idname = "SHELF_PT_nodes"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category  = 'Nodes'

    def draw(self,context):
        layout= self.layout
        layout.menu('SCREEN_MT_user_menu')
        layout.menu_contents('NODE_MT_add')


def register():
    bpy.utils.register_class(SHELF_PT_favourites)
    bpy.utils.register_class(SHELF_PT_nodes)



def unregister():
    bpy.utils.unregister_class(SHELF_PT_favourites)
    bpy.utils.unregister_class(SHELF_PT_nodes)