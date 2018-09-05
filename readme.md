
- sudo rm -rf dist
- sudo rm -rf build
- sudo pyinstaller --clean --onefile --windowed run.spec
Run app : open ./dist/run.app/Contents/MacOS/run


./bin/generate_keys
./bin/sign_update ./run.app.zip dsa_priv.pem


ditto -c -k --sequesterRsrc --keepParent source dest

