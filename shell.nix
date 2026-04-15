let
    nixpkgs = fetchTarball "https://channels.nixos.org/nixpkgs-unstable/nixexprs.tar.xz";
    pkgs = import nixpkgs { 
        config = {
            allowUnfree = true;
        }; 
        overlays = []; 
    };
in
pkgs.mkShellNoCC {
    packages = with pkgs; [
        # Define system dependencies here. They'll be installed in a hermetically sealed environment.
        # If you don't use nix-direnv, just install the packages listed below however you prefer.
        docker
        uv
    ];
}