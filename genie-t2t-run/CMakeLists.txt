cmake_minimum_required(VERSION 3.14)
project(genie-t2t-run)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

# QAIRT SDK path from environment
if(DEFINED ENV{QAIRT_SDK})
    set(QAIRT_SDK $ENV{QAIRT_SDK})
else()
    message(FATAL_ERROR "QAIRT_SDK environment variable not set")
endif()

# Create genie-t2t-run
add_executable(genie-t2t-run main.cpp)
target_include_directories(genie-t2t-run PRIVATE ${QAIRT_SDK}/include/Genie)
target_link_directories(genie-t2t-run PRIVATE ${QAIRT_SDK}/lib/aarch64-android)
target_link_libraries(genie-t2t-run PRIVATE Genie)