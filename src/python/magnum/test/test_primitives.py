#
#   This file is part of Magnum.
#
#   Copyright © 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019
#             Vladimír Vondruš <mosra@centrum.cz>
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the "Software"),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#   in all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#   THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#

import unittest

from magnum import *
from magnum import primitives

class Cube(unittest.TestCase):
    def test_solid(self):
        a = primitives.cube_solid()
        self.assertEqual(a.primitive, MeshPrimitive.TRIANGLES)
        self.assertTrue(a.is_indexed())

    def test_solid_strip(self):
        a = primitives.cube_solid_strip()
        self.assertEqual(a.primitive, MeshPrimitive.TRIANGLE_STRIP)
        self.assertFalse(a.is_indexed())

    def test_wireframe(self):
        a = primitives.cube_wireframe()
        self.assertEqual(a.primitive, MeshPrimitive.LINES)
        self.assertTrue(a.is_indexed())

class Square(unittest.TestCase):
    def test_solid(self):
        a = primitives.square_solid(primitives.SquareTextureCoords.GENERATE)
        self.assertEqual(a.primitive, MeshPrimitive.TRIANGLE_STRIP)
        self.assertFalse(a.is_indexed())
        self.assertTrue(a.has_texture_coords2d())

        b = primitives.square_solid()
        self.assertEqual(b.primitive, MeshPrimitive.TRIANGLE_STRIP)
        self.assertFalse(b.is_indexed())
        self.assertFalse(b.has_texture_coords2d())

    def test_wireframe(self):
        a = primitives.square_wireframe()
        self.assertEqual(a.primitive, MeshPrimitive.LINE_LOOP)
        self.assertFalse(a.is_indexed())
