with import <nixpkgs> {};

pkgs.mkShell {
  LD_LIBRARY_PATH = lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib libGL	];
#  X11];
# https://discourse.nixos.org/t/python-importerror-libstdc-so-6-cannot-open-shared-object-file-no-such-file-or-directory/36988
# https://github.com/NixOS/nixpkgs/issues/250898

# https://discourse.nixos.org/t/what-is-the-nix-way-to-specify-ld-library-path/6407/6
# https://discourse.nixos.org/t/what-package-provides-libstdc-so-6/18707/4


# https://nixos.wiki/wiki/Development_environment_with_nix-shell
# https://nixos.wiki/wiki/Packaging/Binaries
# https://nixos.org/manual/nix/stable/command-ref/nix-shell

# https://nixos.wiki/wiki/Python

}
