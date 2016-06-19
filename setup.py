#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012, Wolf Vollprecht <w.vollprecht@gmail.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE


##################################################################################
###################### YOU SHOULD MODIFY ONLY WHAT IS BELOW ######################
##################################################################################
from distutils.core import setup

setup(
    name='uberwriter',
    version='1.0',
    license='GPL-3',
    author='Wolf Vollprecht',
    author_email='w.vollprecht@gmail.com',
    description='A beautiful, simple and distraction free markdown editor.',
    long_description="""UberWriter, beautiful distraction free writing
 With UberWriter you get only one thing: An empty textbox, that is to 
 fill with your ideas. There are no settings, you don't have to choose a 
 font, it is only for writing.You can use markdown for all your markup 
 needs. PDF, RTF and HTML are generated with pandoc. For PDF generation it 
 is also required that you choose to install the texlive-luatex package.""",
    url='https://launchpad.com/uberwriter',
    # cmdclass={'install': InstallAndUpdateDataDirectory},
    package_dir = {
        # 'uberwriter': '.',
        # 'uberwriter_lib': '.'
        # 'gtkspellcheck': './uberwriter_lib/gtkspellcheck',
        # 'pylocales': './uberwriter_lib/pylocales'
    },
    packages=[
        "uberwriter_lib.gtkspellcheck",
        "uberwriter_lib.pylocales",
        # "uberwriter_lib.pressagio",
        "uberwriter_lib",
        "uberwriter"
    ],
    package_data={
        # 'uberwriter_lib.pylocales' : ['locales.db']
    },
    data_files=[
        ('bin/', ['bin/uberwriter']),
        ('uberwriter_lib/pylocales', ['uberwriter_lib/pylocales/locales.db']),
        ('share/glib-2.0/schemas', ['data/glib-2.0/schemas/net.launchpad.uberwriter.gschema.xml']),
        ('share/icons/hicolor/scalable/apps', ['data/media/uberwriter.svg'])
    ]
)
