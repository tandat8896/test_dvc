{
  description = "DVC testing environment with uv";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          uv
        ];

        shellHook = ''
          if [ ! -f pyproject.toml ]; then
            uv init --no-readme
            uv add dvc
          fi
          source .venv/bin/activate 2>/dev/null || uv sync
          echo "DVC env ready. Run: dvc --version"
        '';
      };
    };
}
