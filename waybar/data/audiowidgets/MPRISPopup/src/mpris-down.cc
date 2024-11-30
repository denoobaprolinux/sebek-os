#include "../include/MPRISApplication.hpp"

int main(int argc, char *argv[]) {
  auto app = MPRISApplication("sebekos.mpris.down");
  return app.run(argc, argv);
}
