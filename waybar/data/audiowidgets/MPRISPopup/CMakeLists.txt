cmake_minimum_required(VERSION 3.10)

project(MPRISPopup C CXX)

find_package(PkgConfig REQUIRED)
pkg_check_modules(gtkmm REQUIRED IMPORTED_TARGET gtkmm-4.0 glibmm-2.68)
pkg_check_modules(playerctl REQUIRED IMPORTED_TARGET playerctl)

set(SRC 
  include/MPRISApplication.cc
)
set(INC 
  include/MPRISApplication.hpp
)

add_subdirectory(libraries/MPRISPopup)

# Crear el ejecutable para mpris-down
add_executable(mpris-up 
  ${SRC} ${INC} 
  src/mpris-up.cc)
target_link_libraries(mpris-up PUBLIC PkgConfig::gtkmm PkgConfig::playerctl MPRISPopup)

# Crear el ejecutable para mpris-down
add_executable(mpris-down 
  ${SRC} ${INC} 
  src/mpris-down.cc)
target_link_libraries(mpris-down PUBLIC PkgConfig::gtkmm PkgConfig::playerctl MPRISPopup)
