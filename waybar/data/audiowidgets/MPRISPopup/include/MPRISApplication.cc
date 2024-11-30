#include "MPRISApplication.hpp"
#include "MPRISPopup.hpp"

MPRISApplication::MPRISApplication(char const *application_id)
    : Gtk::Application(application_id) {}

void MPRISApplication::on_activate() {
  auto win = new MPRISPopup();
  add_window(*win);
  win->present();
}
