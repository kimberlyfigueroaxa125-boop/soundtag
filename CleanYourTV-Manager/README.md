# CleanYourTV Manager

A community-made Windows GUI for managing CleanYourTV on Android TV.

> **Unofficial community project.** This project is not affiliated with or endorsed by the CleanYourTV maintainers. CleanYourTV: https://github.com/Gathin23/cleanyourtv

## Goals

- Qt Designer `.ui` XML interface
- ADB connection and device diagnostics
- CleanYourTV installation/update workflow
- Theme browser and installer
- Add-on browser and installer
- Package cleanup with safety checks
- Backup and restore support
- Visible command log
- Windows `.exe` builds through GitHub Actions

## Safety

The manager must never silently disable Android system packages. Live TV / tuner packages such as `com.mediatek.tvinput` and `com.mediatek.wwtv.tvcenter` should be protected by default. Changes to the Home launcher must require confirmation and provide recovery instructions.

## Project status

Early development scaffold. Test on real hardware before using production releases.

## Development

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app/main.py
```

The UI is stored as Qt Designer XML under `app/ui/`.

## License

This project is separate from CleanYourTV. Review upstream licensing before redistributing upstream code or assets.