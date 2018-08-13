# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class GliConan(ConanFile):
    name = 'gli'
    version = '0.8.2.0'
    description = 'GLI provides classes and functions to load image files (KTX and DDS), facilitate graphics APIs texture creation, compare textures, access texture texels, sample textures, convert textures, generate mipmaps, etc.'
    url = 'https://github.com/birsoyo/conan-gli'
    homepage = 'https://github.com/g-truc/gli'
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = 'Happy Bunny License (Modified MIT) or MIT License'

    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def requirements(self):
        self.requires('glm/0.9.8.5@g-truc/stable')

    def source(self):
        source_url = 'https://github.com/g-truc/gli'
        tools.get(f'{source_url}/archive/{self.version}.tar.gz')
        extracted_dir = self.name + '-' + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, 'gli')
        self.copy(pattern='LICENSE', dst='license', src=self.source_subfolder)
        self.copy(pattern='*', dst='include/gli', src=include_folder)

    def package_info(self):
        self.cpp_info.defines = ['GLM_ENABLE_EXPERIMENTAL']

    def package_id(self):
        self.info.header_only()
