# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2019.3.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2019.3.3\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/STL_Algorithms.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/STL_Algorithms.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/STL_Algorithms.dir/flags.make

CMakeFiles/STL_Algorithms.dir/main.cpp.obj: CMakeFiles/STL_Algorithms.dir/flags.make
CMakeFiles/STL_Algorithms.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/STL_Algorithms.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\STL_Algorithms.dir\main.cpp.obj -c "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\main.cpp"

CMakeFiles/STL_Algorithms.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/STL_Algorithms.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\main.cpp" > CMakeFiles\STL_Algorithms.dir\main.cpp.i

CMakeFiles/STL_Algorithms.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/STL_Algorithms.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\main.cpp" -o CMakeFiles\STL_Algorithms.dir\main.cpp.s

# Object files for target STL_Algorithms
STL_Algorithms_OBJECTS = \
"CMakeFiles/STL_Algorithms.dir/main.cpp.obj"

# External object files for target STL_Algorithms
STL_Algorithms_EXTERNAL_OBJECTS =

STL_Algorithms.exe: CMakeFiles/STL_Algorithms.dir/main.cpp.obj
STL_Algorithms.exe: CMakeFiles/STL_Algorithms.dir/build.make
STL_Algorithms.exe: CMakeFiles/STL_Algorithms.dir/linklibs.rsp
STL_Algorithms.exe: CMakeFiles/STL_Algorithms.dir/objects1.rsp
STL_Algorithms.exe: CMakeFiles/STL_Algorithms.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable STL_Algorithms.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\STL_Algorithms.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/STL_Algorithms.dir/build: STL_Algorithms.exe

.PHONY : CMakeFiles/STL_Algorithms.dir/build

CMakeFiles/STL_Algorithms.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\STL_Algorithms.dir\cmake_clean.cmake
.PHONY : CMakeFiles/STL_Algorithms.dir/clean

CMakeFiles/STL_Algorithms.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms" "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms" "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\cmake-build-debug" "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\cmake-build-debug" "C:\Users\CORE i5\Desktop\Nueva carpeta\Competitive-Programming\STL Algorithms\cmake-build-debug\CMakeFiles\STL_Algorithms.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/STL_Algorithms.dir/depend
