{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages (ps: [
        ps.requests
        # tests
        ps.setuptools
        ps.pytest
        ps.mock
        ps.requests-mock
        ps.pandas
      ])
    )
  ];

  shellHook = ''
    echo
    echo '# blockfrost-python development shell'
    echo
    echo '## to run unit tests, use'
    echo 'pytest'
    echo
    echo '## to run integration tests, use'
    echo 'export BLOCKFROST_PROJECT_ID_MAINNET=mainnet..'
    echo 'pytest'
  '';
}
