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
CMAKE_SOURCE_DIR = "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/C_Create_the_Teams.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/C_Create_the_Teams.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/C_Create_the_Teams.dir/flags.make

CMakeFiles/C_Create_the_Teams.dir/main.cpp.obj: CMakeFiles/C_Create_the_Teams.dir/flags.make
CMakeFiles/C_Create_the_Teams.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/C_Create_the_Teams.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\C_Create_the_Teams.dir\main.cpp.obj -c "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\main.cpp"

CMakeFiles/C_Create_the_Teams.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/C_Create_the_Teams.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\main.cpp" > CMakeFiles\C_Create_the_Teams.dir\main.cpp.i

CMakeFiles/C_Create_the_Teams.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/C_Create_the_Teams.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\main.cpp" -o CMakeFiles\C_Create_the_Teams.dir\main.cpp.s

# Object files for target C_Create_the_Teams
C_Create_the_Teams_OBJECTS = \
"CMakeFiles/C_Create_the_Teams.dir/main.cpp.obj"

# External object files for target C_Create_the_Teams
C_Create_the_Teams_EXTERNAL_OBJECTS =

C_Create_the_Teams.exe: CMakeFiles/C_Create_the_Teams.dir/main.cpp.obj
C_Create_the_Teams.exe: CMakeFiles/C_Create_the_Teams.dir/build.make
C_Create_the_Teams.exe: CMakeFiles/C_Create_the_Teams.dir/linklibs.rsp
C_Create_the_Teams.exe: CMakeFiles/C_Create_the_Teams.dir/objects1.rsp
C_Create_the_Teams.exe: CMakeFiles/C_Create_the_Teams.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable C_Create_the_Teams.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\C_Create_the_Teams.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/C_Create_the_Teams.dir/build: C_Create_the_Teams.exe

.PHONY : CMakeFiles/C_Create_the_Teams.dir/build

CMakeFiles/C_Create_the_Teams.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\C_Create_the_Teams.dir\cmake_clean.cmake
.PHONY : CMakeFiles/C_Create_the_Teams.dir/clean

CMakeFiles/C_Create_the_Teams.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams" "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams" "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\cmake-build-debug" "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\cmake-build-debug" "C:\Users\CORE i5\Desktop\Universidad\ICPC\C-Create the Teams\cmake-build-debug\CMakeFiles\C_Create_the_Teams.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/C_Create_the_Teams.dir/depend

