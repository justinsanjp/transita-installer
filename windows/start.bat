@echo off
chcp 65001
title Transita Magnifico Installer
echo.
echo Willkommen zum Installer! Bevor du fortfahren kannst, stelle bitte sicher, dass du Python 3 und alle notwendigen Abhängigkeiten installiert hast.
echo Falls Python 3 bereits installiert ist, führe bitte die Datei "pip-install.bat" im Installationsordner aus.
echo.
echo Drücke die Enter-Taste, um fortzufahren.
pause >NUL
cls
goto install

:install
python app.py
echo.
echo Falls du eine Fehlermeldung erhalten hast,
echo drücke bitte Enter, um eine alternative Startmethode zu verwenden.
echo.
echo Falls du keine Fehlermeldung erhalten hast, war die Installation vermutlich erfolgreich. Du kannst dieses Fenster nun schließen.
echo.
pause >NUL
cls
echo.
echo Versuch 2
py app.py
echo.
echo Falls du erneut eine Fehlermeldung erhältst,
echo kontaktiere uns bitte über Discord und sende uns den Log. Kopiere einfach die Fehlermeldung und teile sie mit uns.
echo.
echo Drücke Enter, um das Programm zu beenden.
pause >NUL
