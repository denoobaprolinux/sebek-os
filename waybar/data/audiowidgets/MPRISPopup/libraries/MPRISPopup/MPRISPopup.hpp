#ifndef MPRISPOPUP
#define MPRISPOPUP

#include <gtkmm-4.0/gtkmm.h>
#include <playerctl/playerctl.h>
#include <string>

class MPRISPopup : public Gtk::Window {
public:
  MPRISPopup();
  virtual ~MPRISPopup();

protected:
  void load_pywal_colors();
  void set_style();
  void init_playerctl();
  void update_info();
  void on_volume_changed();
  void on_previous();
  void on_play_pause();
  void on_next();
  int get_volume();
  static void on_metadata_changed(PlayerctlPlayer *player, GParamSpec *,
                                  gpointer user_data);

private:
  Gtk::Label label_title, label_artist, label_album;
  Gtk::Scale scale_volume;
  PlayerctlPlayer *player;
  std::string bg_color, fg_color, accent_color;

  // String utilizados en load_pywal_colors
  std::string line{};
  const std::string wal_colors_path{
      (std::string(std::getenv("HOME")) + "/.cache/wal/colors").c_str()};
};

#endif
