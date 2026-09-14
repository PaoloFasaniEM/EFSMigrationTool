@echo off
echo Cleaning previous build...
rmdir /s /q build
rmdir /s /q dist
del /f /q EFSMigrationTool.spec

echo.
echo Building EFS Migration Tool...

pip install pyinstaller --quiet

pyinstaller --onedir --windowed ^
  --icon=resources/icon.png ^
  --add-data "resources;resources" ^
  --add-data "ui;ui" ^
  --name "EFSMigrationTool" ^
  main.py

echo.
echo Done! Folder is in dist\EFSMigrationTool\
pause