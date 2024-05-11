with import <nixpkgs> {};

pkgs.mkShell {
  LD_LIBRARY_PATH = lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib libGL	];
#  X11];
# https://discourse.nixos.org/t/python-importerror-libstdc-so-6-cannot-open-shared-object-file-no-such-file-or-directory/36988
# https://github.com/NixOS/nixpkgs/issues/250898

}
