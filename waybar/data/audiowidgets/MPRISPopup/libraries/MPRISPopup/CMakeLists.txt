add_library(MPRISPopup SHARED
  MPRISPopup.hpp
  MPRISPopup.cc)

find_package(PkgConfig REQUIRED)
pkg_check_modules(gtkmm REQUIRED IMPORTED_TARGET gtkmm-4.0 glibmm-2.68)


target_include_directories(MPRISPopup PUBLIC 
  ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries(MPRISPopup PUBLIC PkgConfig::gtkmm)

