#include "../include/MPRISApplication.hpp"

int main(int argc, char *argv[]) {
  auto app = MPRISApplication("sebekos.mpris.up");
  return app.run(argc, argv);
}
