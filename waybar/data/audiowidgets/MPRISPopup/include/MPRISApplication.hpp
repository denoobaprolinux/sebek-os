#ifndef MPRISAPPLICATION
#define MPRISAPPLICATION

#include <gtkmm-4.0/gtkmm.h>

class MPRISApplication : public Gtk::Application {
public:
  MPRISApplication(char const *application_id);

protected:
  void on_activate() override;
};

#endif
