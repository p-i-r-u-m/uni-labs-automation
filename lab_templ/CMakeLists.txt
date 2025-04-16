cmake_minimum_required(VERSION 3.14)
project(lab)

# Enable compilation database generation
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Set default build type to 'Release' if not specified
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "" FORCE)
endif()
message(STATUS "CMAKE_BUILD_TYPE: ${CMAKE_BUILD_TYPE}")

# Define an interface library for common compiler settings
add_library(cxx_setup INTERFACE)

# Add standard compiler warnings and set C++17 requirement
target_compile_options(cxx_setup INTERFACE -Wall -Wpedantic -Wextra)
target_compile_features(cxx_setup INTERFACE cxx_std_17)

# Add the project source directory to the include path
target_include_directories(cxx_setup INTERFACE ${PROJECT_SOURCE_DIR})


# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  # reccomend updating the hash time to time
  URL URL https://github.com/google/googletest/archive/71815bbf7de6e10c11821d654a2fae2cf42de0f7.zip
)
FetchContent_MakeAvailable(googletest)


# Enable testing for this project
include(CTest)

# Automatically discover source files in 'src' directory
file(GLOB_RECURSE SRC_FILES "src/*.cpp")

# Define the main executable for the project (lab)
add_executable(lab ${SRC_FILES})
target_link_libraries(lab PUBLIC cxx_setup)

# If tests are enabled, add tests
if(BUILD_TESTING)
  # Automatically discover test files in 'tests' and 'src' directories
  file(GLOB_RECURSE TEST_FILES 
    "tests/*.cpp" 
    "src/*.cpp"
  )

  # Remove main.cpp from the list
  list(FILTER TEST_FILES EXCLUDE REGEX ".*main\\.cpp$")
  
  # Define unit_tests executable
  add_executable(unit_tests ${TEST_FILES})

  # Link GoogleTest and other necessary libraries to the unit tests
  target_link_libraries(unit_tests PRIVATE GTest::gtest_main cxx_setup)

  # Link the shared source files (the same as lab) for unit_tests
  #target_link_libraries(unit_tests PRIVATE ${SRC_FILES})

  # Discover tests and enable them
  include(GoogleTest)
  gtest_discover_tests(unit_tests)
endif()


# ---- Structure && UML Diagrams generation ----

# Add command to generate UML diagrams
add_custom_target(generate_uml_diagrams
    COMMAND clang-uml -c ${CMAKE_SOURCE_DIR}/clang-uml.yml
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Generating UML diagrams..."
)

# Convertation in PNG with PlantUML
add_custom_target(generate_uml_images
  COMMAND plantuml ${CMAKE_SOURCE_DIR}/report/diagram/class_diagram.puml
    DEPENDS generate_uml_diagrams
    COMMENT "Converting UML diagrams to PNG..."
)

# Ensure UML diagrams are generated before building the main executable
add_dependencies(lab generate_uml_images)

