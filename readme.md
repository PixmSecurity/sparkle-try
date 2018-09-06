For building the code :
- sudo rm -rf dist
- sudo rm -rf build
- To create build : sudo pyinstaller --clean --onefile --windowed run.spec

The above step will generate an app build in dist folder :
- In info.plist make below entries
<key>SUPublicDSAKeyFile</key>
<string>dsa_pub.pem</string>
<key>CFBundleVersion</key>
<string>1.0.0</string>




- To test app is running : open ./dist/run.app/Contents/MacOS/run
- To generate keys : ./bin/generate_keys
- To create zip file : ditto -c -k --sequesterRsrc --keepParent source_app_file dest_zip_file_for_signing
- To sign the buidl: ./bin/sign_update ./dest_zip_file_for_signing.zip dsa_priv.pem

The above steps creates a signed build for me




