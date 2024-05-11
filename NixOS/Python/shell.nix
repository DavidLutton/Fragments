with import <nixpkgs> {};

pkgs.mkShell {
  LD_LIBRARY_PATH = lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib libGL	];
#  X11];

}
