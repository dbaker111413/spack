##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os


class PrunersNinja(AutotoolsPackage):

    """NINJA: Noise Inject agent tool to expose subtle and unintended message 
       races."""
    homepage = "https://github.com/PRUNERS/NINJA"
    url      = "https://github.com/PRUNERS/NINJA/archive/v0.1.0.tar.gz"
    
    version("0.1.0", "9c207c494635d98d1568ed41c0feb715")
    version('0.1.1b', git='https://github.com/PRUNERS/NINJA.git',
            commit='7757dc98634577199b0e9e02a567697de6d9babe')

    depends_on("mpi")
    depends_on("autoconf", type='build')
    depends_on("automake", type='build')
    depends_on("libtool", type='build')

    def autoreconf(self, spec, prefix):
        if os.path.exists('autogen.sh'):
            # Bootstrap with autotools
            bash = which('bash')
            bash('./autogen.sh')

