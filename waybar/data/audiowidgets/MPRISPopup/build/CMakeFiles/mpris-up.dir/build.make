# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.31

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build

# Include any dependencies generated for this target.
include CMakeFiles/mpris-up.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/mpris-up.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/mpris-up.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mpris-up.dir/flags.make

CMakeFiles/mpris-up.dir/codegen:
.PHONY : CMakeFiles/mpris-up.dir/codegen

CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o: CMakeFiles/mpris-up.dir/flags.make
CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o: /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/include/MPRISApplication.cc
CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o: CMakeFiles/mpris-up.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o -MF CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o.d -o CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o -c /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/include/MPRISApplication.cc

CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/include/MPRISApplication.cc > CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.i

CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/include/MPRISApplication.cc -o CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.s

CMakeFiles/mpris-up.dir/src/mpris-up.cc.o: CMakeFiles/mpris-up.dir/flags.make
CMakeFiles/mpris-up.dir/src/mpris-up.cc.o: /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/src/mpris-up.cc
CMakeFiles/mpris-up.dir/src/mpris-up.cc.o: CMakeFiles/mpris-up.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/mpris-up.dir/src/mpris-up.cc.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/mpris-up.dir/src/mpris-up.cc.o -MF CMakeFiles/mpris-up.dir/src/mpris-up.cc.o.d -o CMakeFiles/mpris-up.dir/src/mpris-up.cc.o -c /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/src/mpris-up.cc

CMakeFiles/mpris-up.dir/src/mpris-up.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/mpris-up.dir/src/mpris-up.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/src/mpris-up.cc > CMakeFiles/mpris-up.dir/src/mpris-up.cc.i

CMakeFiles/mpris-up.dir/src/mpris-up.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/mpris-up.dir/src/mpris-up.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/src/mpris-up.cc -o CMakeFiles/mpris-up.dir/src/mpris-up.cc.s

# Object files for target mpris-up
mpris__up_OBJECTS = \
"CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o" \
"CMakeFiles/mpris-up.dir/src/mpris-up.cc.o"

# External object files for target mpris-up
mpris__up_EXTERNAL_OBJECTS =

mpris-up: CMakeFiles/mpris-up.dir/include/MPRISApplication.cc.o
mpris-up: CMakeFiles/mpris-up.dir/src/mpris-up.cc.o
mpris-up: CMakeFiles/mpris-up.dir/build.make
mpris-up: CMakeFiles/mpris-up.dir/compiler_depend.ts
mpris-up: libraries/MPRISPopup/libMPRISPopup.so
mpris-up: /usr/lib/libplayerctl.so
mpris-up: /usr/lib/libgtkmm-4.0.so
mpris-up: /usr/lib/libharfbuzz.so
mpris-up: /usr/lib/libpango-1.0.so
mpris-up: /usr/lib/libcairo-gobject.so
mpris-up: /usr/lib/libglib-2.0.so
mpris-up: /usr/lib/libvulkan.so
mpris-up: /usr/lib/libgraphene-1.0.so
mpris-up: /usr/lib/libgobject-2.0.so
mpris-up: /usr/lib/libgio-2.0.so
mpris-up: /usr/lib/libsigc-3.0.so
mpris-up: /usr/lib/libcairo.so
mpris-up: /usr/lib/libpangomm-2.48.so
mpris-up: /usr/lib/libgiomm-2.68.so
mpris-up: /usr/lib/libcairomm-1.16.so
mpris-up: /usr/lib/libpangocairo-1.0.so
mpris-up: /usr/lib/libgdk_pixbuf-2.0.so
mpris-up: /usr/lib/libgtk-4.so
mpris-up: /usr/lib/libglibmm-2.68.so
mpris-up: CMakeFiles/mpris-up.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable mpris-up"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mpris-up.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/mpris-up.dir/build: mpris-up
.PHONY : CMakeFiles/mpris-up.dir/build

CMakeFiles/mpris-up.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mpris-up.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mpris-up.dir/clean

CMakeFiles/mpris-up.dir/depend:
	cd /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build /home/rafa/programs/dotfiles/sebek-os/waybar/data/audiowidgets/MPRISPopup/build/CMakeFiles/mpris-up.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/mpris-up.dir/depend

