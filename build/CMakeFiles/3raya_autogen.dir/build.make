# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

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
CMAKE_SOURCE_DIR = /home/alvaro/Desktop/3inarow/c++

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alvaro/Desktop/3inarow/build

# Utility rule file for 3raya_autogen.

# Include any custom commands dependencies for this target.
include CMakeFiles/3raya_autogen.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/3raya_autogen.dir/progress.make

CMakeFiles/3raya_autogen: 3raya_autogen/timestamp

3raya_autogen/timestamp: /usr/lib/qt5/bin/moc
3raya_autogen/timestamp: CMakeFiles/3raya_autogen.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/alvaro/Desktop/3inarow/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC for target 3raya"
	/usr/bin/cmake -E cmake_autogen /home/alvaro/Desktop/3inarow/build/CMakeFiles/3raya_autogen.dir/AutogenInfo.json Debug
	/usr/bin/cmake -E touch /home/alvaro/Desktop/3inarow/build/3raya_autogen/timestamp

3raya_autogen: 3raya_autogen/timestamp
3raya_autogen: CMakeFiles/3raya_autogen
3raya_autogen: CMakeFiles/3raya_autogen.dir/build.make
.PHONY : 3raya_autogen

# Rule to build all files generated by this target.
CMakeFiles/3raya_autogen.dir/build: 3raya_autogen
.PHONY : CMakeFiles/3raya_autogen.dir/build

CMakeFiles/3raya_autogen.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/3raya_autogen.dir/cmake_clean.cmake
.PHONY : CMakeFiles/3raya_autogen.dir/clean

CMakeFiles/3raya_autogen.dir/depend:
	cd /home/alvaro/Desktop/3inarow/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alvaro/Desktop/3inarow/c++ /home/alvaro/Desktop/3inarow/c++ /home/alvaro/Desktop/3inarow/build /home/alvaro/Desktop/3inarow/build /home/alvaro/Desktop/3inarow/build/CMakeFiles/3raya_autogen.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/3raya_autogen.dir/depend

